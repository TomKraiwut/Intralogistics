# -*- coding: utf-8 -*-
"""Pre-test and post-test pages. The tests themselves are Google Forms (answer keys and form
scripts stay in _No_Upload/, never committed); these pages explain the test and embed the form
whose link is set in gen_site.QUIZ_PAGES."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (QUIZ_PAGES, SECTIONS, SECTION_ORDER, page_html, write, chapter_filename,
                      chapter_numbers, chapter_title, chapter_label)


def form_block(url):
    if not url:
        return '''
<div class="note"><strong>ยังไม่เปิดให้ทำ:</strong> แบบทดสอบนี้กำลังเตรียม — ผู้สอนจะแจ้งเมื่อเปิดให้ทำ</div>'''
    embed = url + ("&" if "?" in url else "?") + "embedded=true"
    return f'''
<div class="download">
  <a class="download-btn" href="{url}" target="_blank" rel="noopener">เปิดแบบทดสอบในหน้าต่างใหม่</a>
  <p>แนะนำบนมือถือ หรือถ้าฟอร์มด้านล่างไม่แสดง</p>
</div>
<div class="form-embed">
  <iframe src="{embed}" title="แบบทดสอบ" loading="lazy">กำลังโหลด…</iframe>
</div>'''


def pre_body(info):
    sec = SECTION_ORDER[0]
    first = chapter_numbers(sec)[0]
    return f'''        <h1>{info["title"]}</h1>
        <p class="lead" style="max-width:46em;">ก่อนเริ่มเรียน ทำแบบทดสอบสั้น ๆ เพื่อวัดความรู้เดิม
        ยังไม่ต้องรู้คำตอบทุกข้อ ตอบตามความเข้าใจตอนนี้</p>

<div class="tip"><strong>สำคัญ:</strong> ใช้อีเมลเดียวกันตอนทำ<a href="post-test.html">แบบทดสอบหลังเรียน</a>
เพื่อเทียบคะแนนก่อน–หลังเรียน</div>
{form_block(info["form"])}

        <div class="page-nav">
          <a href="index.html">← หน้าแรก</a>
          <a href="{chapter_filename(sec, first)}">ถัดไป: {chapter_label(sec, first)} {chapter_title(sec, first)} →</a>
        </div>'''


def post_body(info):
    sec = SECTION_ORDER[-1]
    last = chapter_numbers(sec)[-1]
    return f'''        <h1>{info["title"]}</h1>
        <p class="lead" style="max-width:46em;">เรียนครบแล้ว ทำแบบทดสอบหลังเรียนชุดเดียวกับก่อนเรียน
        และประเมินความพึงพอใจต่อหลักสูตร ความเห็นของคุณช่วยปรับปรุงหลักสูตรรอบต่อไป</p>

<div class="tip"><strong>สำคัญ:</strong> ใช้อีเมลเดียวกับตอนทำ<a href="pre-test.html">แบบทดสอบก่อนเรียน</a></div>
{form_block(info["form"])}

        <div class="page-nav">
          <a href="{chapter_filename(sec, last)}">← ก่อนหน้า: {chapter_label(sec, last)} {chapter_title(sec, last)}</a>
          <a href="index.html">กลับหน้าแรก</a>
        </div>'''


if __name__ == "__main__":
    for name, build in (("pre-test.html", pre_body), ("post-test.html", post_body)):
        info = QUIZ_PAGES[name]
        write(name, page_html(info["title"], build(info), active_top=name))
