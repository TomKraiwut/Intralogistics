# -*- coding: utf-8 -*-
"""Home page: course facts from the DSD course document + one card group per section."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (SECTIONS, SECTION_ORDER, section_no, section_title, QUIZ_PAGES, PTS_VERSION, page_html, write, chapter_numbers,
                      card_html, HUB_CARD_DESC)


def quiz_card(page, badge, desc):
    return f'''        <div class="card-grid">
          <a href="{page}" class="card">
            <div class="icon number">{badge}</div>
            <h3>{QUIZ_PAGES[page]["title"]}</h3>
            <p>{desc}</p>
          </a>
        </div>'''


def cards(section):
    return "\n".join(card_html(section, i, HUB_CARD_DESC[section][n])
                     for n, i in enumerate(chapter_numbers(section)))


def subject_rows():
    rows = []
    for sec in SECTION_ORDER:
        info = SECTIONS[sec]
        if "hours" not in info:
            continue
        t, p = (x.strip() for x in info["hours"].split(":"))
        rows.append(f'<tr><td>{section_no(sec)}</td><td><a href="{info["hub"]}">{info["label"]}</a></td>'
                    f'<td>{t}</td><td>{p}</td></tr>')
    return "\n".join(rows)


def section_blocks():
    out = []
    for sec in SECTION_ORDER:
        info = SECTIONS[sec]
        out.append(f'''        <h2><a href="{info["hub"]}">{section_title(sec)}</a></h2>
        <div class="card-grid">
{cards(sec)}
        </div>''')
    return "\n\n".join(out)


BODY = f'''        <section id="banner">
          <h1>ระบบการจัดการคลังสินค้าอัตโนมัติ (Intralogistics)</h1>
          <p class="tagline">เรียนรู้คลังสินค้าอัตโนมัติด้วยแบบจำลองเสมือนจริง {PTS_VERSION} และ AI — ภาษาไทย</p>
          <p class="intro">
            เริ่มจากหลักการโลจิสติกส์และการจัดการคลังสินค้า คำนวณสินค้าคงคลัง แล้วสร้างแบบจำลองคลังสินค้าด้วยตัวเอง
            จนถึงระบบขนถ่ายอัตโนมัติ — Forklift, AGV, AMR, AS/RS และโรงงาน / คลังสินค้า 3D — จากนั้นใช้ AI กับผลของแบบจำลอง
            หาค่าที่เหมาะสม และประเมินการลงทุนเพื่อเสนอผู้บริหาร
          </p>
        </section>

        <h2>เกี่ยวกับหลักสูตร</h2>
        <p>เนื้อหาเว็บนี้ตรงกับหลักสูตรการฝึกยกระดับฝีมือ <strong>ระบบการจัดการคลังสินค้าอัตโนมัติ (INTRALOGISTICS)</strong>
        ของกรมพัฒนาฝีมือแรงงาน · ระยะเวลา 18 ชั่วโมง</p>
        <p><strong>เรียนจบแล้วจะสามารถ</strong></p>
        <ol>
          <li>ประยุกต์ใช้ระบบการจัดการคลังสินค้าอัตโนมัติในการออกแบบและบริหารคลังสินค้าขององค์กรได้อย่างถูกต้องและมีประสิทธิภาพมากขึ้น</li>
          <li>วิเคราะห์ข้อมูลจากแบบจำลองเสมือนจริงด้วยปัญญาประดิษฐ์ (AI) เพื่อประกอบการตัดสินใจลงทุนและการลดคาร์บอนของคลังสินค้า</li>
          <li>เพิ่มประสิทธิภาพในการบริหารจัดการซัพพลายเชนในยุคดิจิทัล</li>
        </ol>

        <table>
        <tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทฤษฎี (ชม.)</th><th>ปฏิบัติ (ชม.)</th></tr>
{subject_rows()}
        <tr><td></td><td><strong>รวม</strong></td><td><strong>6</strong></td><td><strong>12</strong></td></tr>
        </table>

        <div class="tip"><strong>เกณฑ์ผ่าน:</strong> เวลาเรียนไม่น้อยกว่าร้อยละ 80 และผลการประเมินทั้งภาคทฤษฎีและภาคปฏิบัติ
        ไม่น้อยกว่าร้อยละ 60 จึงได้รับวุฒิบัตรพัฒนาฝีมือแรงงาน</div>

        <h2>เริ่มที่นี่</h2>
{quiz_card("pre-test.html", "ก่อน", "แบบทดสอบความรู้ก่อนเรียน ใช้เทียบคะแนนกับหลังเรียน")}

{section_blocks()}'''

if __name__ == "__main__":
    write("index.html", page_html("หน้าแรก", BODY, active_top="index"))
