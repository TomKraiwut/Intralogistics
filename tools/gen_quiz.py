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
        <p class="lead" style="max-width:46em;">ก่อนเริ่มเรียน ทำ<strong>แบบสอบถามความคาดหวัง</strong>
        (ประสบการณ์ หัวข้อที่อยากเรียน งานที่อยากนำไปใช้) และ<strong>แบบทดสอบ 20 ข้อ</strong>เพื่อวัดความรู้เดิม
        ใช้เวลาประมาณ 15 นาที — ยังไม่ต้องรู้คำตอบทุกข้อ ตอบตามความเข้าใจตอนนี้</p>

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
        <p class="lead" style="max-width:46em;">เรียนครบแล้ว ทำแบบทดสอบหลังเรียน <strong>100 คะแนน</strong>
        ตรวจอัตโนมัติ <strong>ผ่านเมื่อได้ 60 คะแนนขึ้นไป</strong> แล้วประเมินความพึงพอใจท้ายฟอร์ม</p>
<table>
<tr><th rowspan="2">หมวดวิชา</th><th>ภาคทฤษฎี (ภาคความรู้)</th><th>ภาคปฏิบัติ (ภาคทักษะ)</th></tr>
<tr><th>ข้อละ 1 คะแนน</th><th>คำถามการใช้โปรแกรม ข้อละ 2 คะแนน</th></tr>
<tr><td>หลักการจัดการโลจิสติกส์ (บท 1.1–1.4)</td><td>5 ข้อ · 5 คะแนน</td><td>10 ข้อ · 20 คะแนน</td></tr>
<tr><td>การจัดการเชิงกลยุทธ์และการตัดสินใจ (บท 4.1–4.2)</td><td>5 ข้อ · 5 คะแนน</td><td>10 ข้อ · 20 คะแนน</td></tr>
<tr><td>การจัดการสินค้าคงคลังและสร้างแบบจำลอง (บท 2.1–2.8)</td><td>5 ข้อ · 5 คะแนน</td><td>10 ข้อ · 20 คะแนน</td></tr>
<tr><td>การใช้แบบจำลองเสมือนจริงวิเคราะห์ (บท 3.1–3.3)</td><td>5 ข้อ · 5 คะแนน</td><td>10 ข้อ · 20 คะแนน</td></tr>
<tr><td><strong>รวม</strong></td><td><strong>20 คะแนน</strong></td><td><strong>80 คะแนน</strong></td></tr>
</table>

<div class="tip"><strong>สำคัญ:</strong> ใช้อีเมลเดียวกับตอนทำ<a href="pre-test.html">แบบทดสอบก่อนเรียน</a> ·
หลังส่ง ฟอร์มจะบอกเหตุผลของคำตอบที่ถูกและบทที่ควรทบทวน</div>
{form_block(info["form"])}

        <div class="page-nav">
          <a href="{chapter_filename(sec, last)}">← ก่อนหน้า: {chapter_label(sec, last)} {chapter_title(sec, last)}</a>
          <a href="index.html">กลับหน้าแรก</a>
        </div>'''


if __name__ == "__main__":
    for name, build in (("pre-test.html", pre_body), ("post-test.html", post_body)):
        info = QUIZ_PAGES[name]
        write(name, page_html(info["title"], build(info), active_top=name))
