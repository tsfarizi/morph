import os
import django
from pathlib import Path
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "morph.settings")
django.setup()

from morph_lesson.models import Lesson, Page

MEDIA_DIR = Path("media/lessons") 

def extract_page_number(filename):
    match = re.match(r'^(\d+)', filename)
    return int(match.group(1)) if match else 0

def extract_title(filename):
    name = re.sub(r'^\d+\.', '', filename)
    name = re.sub(r'\.md$', '', name)
    return name.replace('_', ' ').strip()

def build_file_path(lesson_title, filename):
    return f"/media/lessons/{lesson_title.lower()}/{filename}"

def load_lessons():
    for lesson_folder in MEDIA_DIR.iterdir():
        if lesson_folder.is_dir():
            lesson_title = lesson_folder.name.capitalize()
            lesson, _ = Lesson.objects.get_or_create(title=lesson_title)
            Page.objects.filter(lesson=lesson).delete()

            for file in sorted(lesson_folder.glob("*.md")):
                filename = file.name
                page_num = extract_page_number(filename)
                title = extract_title(filename)
                file_url = build_file_path(lesson_folder.name, filename)

                Page.objects.create(
                    lesson=lesson,
                    page=page_num,
                    title=title,
                    filename=filename,
                    file_url=file_url
                )

    print("✅ Data lesson dan page berhasil dimuat ulang dari media.")

if __name__ == "__main__":
    load_lessons()
