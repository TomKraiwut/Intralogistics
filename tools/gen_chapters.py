# -*- coding: utf-8 -*-
"""Generates every chapter page and the section hub pages.
Run after gen_site.py (reuses its templates by importing it).

Each chapter's content lives in its own file, tools/chapters/<section>_<NN>.py, which defines
  OBJECTIVES = ["...", ...]   # 2-4 learning goals
  TOPICS = ["...", ...]       # topics of the course document covered here (shown while BODY is missing)
  BODY = f'''...'''           # page HTML, may use screenshot()/step_list()/side_by_side() -- optional
A chapter without BODY (or without a file) shows its topics and a "coming soon" note."""
import sys, os
import importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (SECTIONS, SECTION_ORDER, section_title, PTS_VERSION, page_html, chapter_filename, chapter_numbers,
                      chapter_title, chapter_label, chapter_kind, chapter_download, DOWNLOAD_BASE,
                      KIND_TEXT, QUIZ_PAGES, hub_page, write)

CHAPTER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chapters")


def load_chapter(section, idx):
    path = os.path.join(CHAPTER_DIR, f"{section}_{idx:02d}.py")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(f"chapter_{section}_{idx}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def coming_soon(topics):
    topics_html = ""
    if topics:
        items = "\n".join(f"  <li>{t}</li>" for t in topics)
        topics_html = f'''
<h2>หัวข้อในบทนี้</h2>
<ul>
{items}
</ul>'''
    return f'''{topics_html}
<div class="note">
<strong>กำลังจัดทำ:</strong> บทนี้กำลังเรียบเรียงบน {PTS_VERSION} พร้อมภาพหน้าจอทีละขั้นและไฟล์ตัวอย่าง
</div>'''


def _neighbour(section, idx, step):
    """(href, label) of the previous (step=-1) or next (step=+1) page in reading order:
    the next section is entered through its hub; going back lands on the previous section's last chapter."""
    numbers = chapter_numbers(section)
    pos = numbers.index(idx) + step
    if 0 <= pos < len(numbers):
        n = numbers[pos]
        return chapter_filename(section, n), f"{chapter_label(section, n)} {chapter_title(section, n)}"
    sec_pos = SECTION_ORDER.index(section) + step
    if not 0 <= sec_pos < len(SECTION_ORDER):
        return None
    other = SECTION_ORDER[sec_pos]
    if step < 0:
        n = chapter_numbers(other)[-1]
        return chapter_filename(other, n), f"{chapter_label(other, n)} {chapter_title(other, n)}"
    return SECTIONS[other]["hub"], section_title(other)


def chapter_page(section, idx):
    title = chapter_title(section, idx)
    label = chapter_label(section, idx)
    mod = load_chapter(section, idx)
    objs = getattr(mod, "OBJECTIVES", []) if mod else []
    body = getattr(mod, "BODY", None) if mod else None
    body_content = (body if body else coming_soon(getattr(mod, "TOPICS", []) if mod else [])).strip()

    kind = KIND_TEXT.get(chapter_kind(section, idx), "")
    kind_html = (f'\n        <p class="lead">{section_title(section)} · ภาค{kind}</p>' if kind
                 else f'\n        <p class="lead">{section_title(section)}</p>')

    objs_html = ""
    if objs:
        items = "\n".join(f"          <li>{o}</li>" for o in objs)
        objs_html = f'''
        <div class="objectives">
          <p>วัตถุประสงค์การเรียนรู้</p>
          <ol>
{items}
          </ol>
        </div>
'''

    download_html = ""
    spp = chapter_download(section, idx)
    if spp:
        download_html = f'''
        <div class="download">
          <a class="download-btn" href="{DOWNLOAD_BASE}{spp}">⬇ ดาวน์โหลดไฟล์ของบท</a>
          <p><code>{spp}</code> — บันทึกจาก {PTS_VERSION}
          · เปิดไฟล์แล้วดับเบิลคลิก Frame ใน Class Library › Models</p>
        </div>
'''

    # the course starts at the pre-test and ends at the post-test
    prev = _neighbour(section, idx, -1)
    prev_href, prev_label = prev if prev else ("pre-test.html", QUIZ_PAGES["pre-test.html"]["title"])
    nxt = _neighbour(section, idx, +1)
    next_html = (f'<a href="{nxt[0]}">ถัดไป: {nxt[1]} →</a>' if nxt
                 else f'<a href="post-test.html">ถัดไป: {QUIZ_PAGES["post-test.html"]["title"]} →</a>')

    body = f'''        <h1>{label} {title}</h1>{kind_html}
{objs_html}{download_html}
{body_content}

        <div class="page-nav">
          <a href="{prev_href}">← ก่อนหน้า: {prev_label}</a>
          {next_html}
        </div>'''
    return page_html(f"{label} {title}", body, expand_section=section, active_top=section, active_chapter=idx)


if __name__ == "__main__":
    for sec in SECTION_ORDER:
        for i in chapter_numbers(sec):
            write(chapter_filename(sec, i), chapter_page(sec, i))
        write(SECTIONS[sec]["hub"], hub_page(sec))
