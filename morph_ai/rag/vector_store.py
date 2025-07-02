from pathlib import Path
import os, re
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

__all__ = ["get_retriever", "LANGUAGE_MAP"]

DATA_DIR = Path(__file__).resolve().parent / "data"
MD_FILES = [f for f in os.listdir(DATA_DIR) if f.endswith(".md")]
LANGUAGE_MAP = {
    f.replace(".md", "").lower(): f.replace(".md", "").capitalize()
    for f in MD_FILES
}

VDB_DIR = Path(__file__).resolve().parent / "vectordb"
INDEX_FILE = VDB_DIR / "chroma.sqlite3"
EMBEDDING = OllamaEmbeddings(model="nomic-embed-text:latest")

def _detect_language(fname: str) -> str:
    lower = fname.lower()
    for key in LANGUAGE_MAP:
        if key in lower:
            return LANGUAGE_MAP[key]
    return "Unknown"

def _order_from_fname(fname: str) -> int:
    m = re.search(r'(\d+)', fname)
    return int(m.group(1)) if m else 999

def _extract_metadata(text: str, fname: str) -> dict:
    metadata = {
        "source": fname,
        "language": _detect_language(fname),
        "order": _order_from_fname(fname),
    }

    lines = text.splitlines()
    title = ""
    if lines and lines[0].startswith("#"):
        title = lines[0].replace("#", "").strip()
    metadata["title"] = title

    halaman_titles = []
    for line in lines:
        if line.strip().lower().startswith("## halaman"):
            halaman_titles.append(line.strip())

    if halaman_titles:
        metadata["pages"] = str(halaman_titles)

    return metadata

def _build_store() -> None:
    VDB_DIR.mkdir(parents=True, exist_ok=True)
    print("[INFO] Building vector store from markdown files…")

    docs = []

    for fname in MD_FILES:
        path = DATA_DIR / fname
        text = path.read_text(encoding="utf-8")

        meta = _extract_metadata(text, fname)
        docs.append(Document(page_content=text, metadata=meta))

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    Chroma.from_documents(
        chunks,
        embedding=EMBEDDING,
        persist_directory=str(VDB_DIR)
    ).persist()

def get_retriever():
    if not INDEX_FILE.exists():
        _build_store()
    return Chroma(
        persist_directory=str(VDB_DIR),
        embedding_function=EMBEDDING
    ).as_retriever(search_type="mmr", search_kwargs={"k": 6, "fetch_k": 12})
