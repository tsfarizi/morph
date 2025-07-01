from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, AIMessage
from langchain.chains import LLMChain
from morph_auth.models import ChatLog  
from .vector_store import get_retriever, LANGUAGE_MAP
from .prompts import BASE_TEMPLATE
from .recommender import detect_recommendation
from django.utils import timezone
import time
from transformers import AutoTokenizer  

retriever = get_retriever()
llm = ChatOllama(model="gemma3:4b")

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=BASE_TEMPLATE
)

llm_chain = LLMChain(llm=llm, prompt=prompt)  

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def build_context(user, docs) -> str:
    lesson_ctx, prog_lines = "", []

    progress_qs = user.lesson_progress.all()
    for e in progress_qs:
        prog_lines.append(f"- {e.title}, halaman {e.page} (terakhir {e.date})")

    if prog_lines:
        lesson_ctx += "Riwayat belajar pengguna:\n" + "\n".join(prog_lines) + "\n"

    latest_progress = progress_qs.first()
    if latest_progress:
        lesson_ctx += (
            f"Pelajaran terakhir yang dipelajari: {latest_progress.title}. "
            f"Pengguna terakhir berada di halaman: {latest_progress.page}. "
        )

    keywords = ", ".join(LANGUAGE_MAP.values())
    doc_ctx = "\n\n".join([d.page_content for d in docs])

    return f"{lesson_ctx}\n\nTopik yang diizinkan: {keywords}.\n\n{doc_ctx}"

def run_chat(user, question: str, timestamp=None) -> tuple[str, dict | None]:
    timestamp = timestamp or timezone.now()

    t_start_total = time.time()

    t_start_retrieval = time.time()
    docs = retriever.invoke(question)
    t_end_retrieval = time.time()

    logs = user.chat_logs.order_by('-timestamp')[:10][::-1]
    chat_hist = []
    for log in logs:
        if log.role == "user":
            chat_hist.append(HumanMessage(content=log.content))
        elif log.role == "ai":
            chat_hist.append(AIMessage(content=log.content))

    t_start_context = time.time()
    context = build_context(user, docs)
    t_end_context = time.time()

    t_start_llm = time.time()
    result = llm_chain.invoke({
        "question": question,
        "context": context
    })
    t_end_llm = time.time()

    response = result.get("text") or result.get("content") or str(result)

    ChatLog.objects.create(user=user, role="user", content=question, timestamp=timestamp)
    ChatLog.objects.create(user=user, role="ai", content=response, timestamp=timezone.now())

    rec = detect_recommendation(response)
    rec_data = None
    if rec and "lesson" in rec:
        rec_data = {
            "title": rec["lesson"].title
        }

    t_end_total = time.time()
    num_tokens = len(tokenizer.encode(response))
    llm_duration = t_end_llm - t_start_llm
    tokens_per_sec = num_tokens / llm_duration if llm_duration else 0

    print("\n--- PERFORMANCE METRICS ---")
    print(f"Total time       : {t_end_total - t_start_total:.2f}s")
    print(f"Retrieval time   : {t_end_retrieval - t_start_retrieval:.2f}s")
    print(f"Context build    : {t_end_context - t_start_context:.2f}s")
    print(f"LLM gen time     : {llm_duration:.2f}s")
    print(f"Tokens generated : {num_tokens}")
    print(f"Tokens/sec       : {tokens_per_sec:.2f}")
    print("---------------------------\n")

    return (response, rec_data)
