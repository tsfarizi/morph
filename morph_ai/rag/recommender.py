import re
import difflib
from morph_lesson.models import Lesson

TRIGGERS = ["pelajari", "lanjut ke", "belajar", "sarankan", "topik berikutnya"]

def _close_enough(needle: str, haystack: str, threshold=0.75) -> bool:
    return difflib.SequenceMatcher(None, needle.lower(), haystack.lower()).ratio() >= threshold

def detect_recommendation(answer: str):
    ans_lower = answer.lower()
    matched_lesson = None

    for lesson in Lesson.objects.all():
        if lesson.title.lower() in ans_lower and any(trig in ans_lower for trig in TRIGGERS):
            matched_lesson = lesson
            break

    patterns = [
        r"([a-zA-Z]+)\s+halaman\s+(\d+)\s*[·|:\-]\s*(.+?)(?:\.|\n|$)",  
        r"halaman\s+(\d+)\s+tentang\s+(.+?)(?:\.|\n|$)",               
    ]

    for pattern in patterns:
        page_match = re.search(pattern, answer, re.IGNORECASE)
        if page_match:
            if len(page_match.groups()) == 3:
                lesson_title = page_match.group(1).strip()
            elif len(page_match.groups()) == 2 and matched_lesson:
                lesson_title = matched_lesson.title
            else:
                continue

            for lesson in Lesson.objects.all():
                if lesson.title.lower() == lesson_title.lower():
                    matched_lesson = lesson
                    break
        if matched_lesson:
            break

    if not matched_lesson:
        for lesson in Lesson.objects.prefetch_related("pages"):
            for page in lesson.pages.all():
                if _close_enough(page.title, answer):
                    matched_lesson = lesson
                    break
            if matched_lesson:
                break

    if matched_lesson:
        return {"lesson": matched_lesson}

    return None
