# -*- coding: utf-8 -*-
"""evaluation 2: สอบภาคปฏิบัติ -- 2026-11-27: separate MCQ form (EXAM_FORMS["practical"], built from
_No_Upload/exam/52_practical_draft_TH.md by build_52.py): A 10 x 2 · C 10 x 2 · D 5 x 4 = 60 in the form; B (strategy) 20 is
assessed by the instructor. The build-it-yourself task stays as an ungraded review exercise (key in ANSWER_KEY_TH.md)."""
from gen_site import screenshot, step_list, side_by_side, EXAM_FORMS, form_embed

TOPICS = []

OBJECTIVES = [
    "ทบทวนการใช้ Plant Simulation ก่อนสอบ",
    "ทำแบบทดสอบภาคปฏิบัติ (80 คะแนน) ได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ข้อสอบภาคปฏิบัติ <strong>80 คะแนน</strong> — คำถามการใช้โปรแกรมแบบตัวเลือก 60 คะแนน
ตรวจอัตโนมัติ และหมวดกลยุทธ์ 20 คะแนน ผู้สอนประเมิน · รวมกับภาคทฤษฎี (บท <a href="evaluation-01.html">5.1</a>) เป็น 100 คะแนน
<strong>ผ่านเมื่อได้ 60 คะแนนขึ้นไป</strong></p>

<h2>ขอบเขต</h2>
<table>
<tr><th>หมวดวิชา</th><th>ทบทวนบท</th><th>รูปแบบ</th><th>คะแนน</th></tr>
<tr><td>หลักการจัดการโลจิสติกส์</td><td><a href="logistics-02.html">1.2</a>–<a href="logistics-04.html">1.4</a></td><td>ตัวเลือก 10 ข้อ × 2</td><td>20</td></tr>
<tr><td>การจัดการสินค้าคงคลังและสร้างแบบจำลอง</td><td><a href="simulation-02.html">2.2</a>–<a href="simulation-08.html">2.8</a></td><td>ตัวเลือก 10 ข้อ × 2</td><td>20</td></tr>
<tr><td>การใช้แบบจำลองเสมือนจริงวิเคราะห์</td><td><a href="ai-02.html">3.2</a>–<a href="ai-03.html">3.3</a></td><td>ตัวเลือก 5 ข้อ × 4</td><td>20</td></tr>
<tr><td>การจัดการเชิงกลยุทธ์และการตัดสินใจ</td><td><a href="strategy-02.html">4.2</a></td><td>ผู้สอนประเมิน</td><td>20</td></tr>
<tr><td><strong>รวม</strong></td><td></td><td></td><td><strong>80</strong></td></tr>
</table>

<h2>แบบทดสอบ</h2>
{form_embed(EXAM_FORMS["practical"], "ข้อสอบภาคปฏิบัติ")}

<h2>แบบฝึกทบทวน (ไม่คิดคะแนน): สร้างท่ารับสินค้าเอง</h2>
<p>ท่ารับสินค้ามีรถส่งพาเลทเข้ามา<strong>ทุก 2 นาที</strong> พักที่ท่าได้ไม่เกิน <strong>100 พาเลท</strong>
Forklift ยก<strong>คันละ 5 นาทีต่อพาเลท</strong> ทำงาน <strong>8 ชั่วโมง</strong></p>
<table>
<tr><th>Object</th><th>ชื่อ</th><th>ตั้งค่า</th></tr>
<tr><td>Source</td><td><code>Inbound</code></td><td>Interval 2:00</td></tr>
<tr><td>Buffer</td><td><code>Dock</code></td><td>Capacity 100 · Processing time 0</td></tr>
<tr><td>ParallelStation</td><td><code>Putaway</code></td><td>Processing time 5:00 · X-Dimension = จำนวน Forklift · ☐ Start Processing When Full</td></tr>
<tr><td>Drain</td><td><code>Rack</code></td><td>—</td></tr>
<tr><td>EventController</td><td></td><td>End 8:00:00</td></tr>
</table>
{step_list([
    "Forklift 2 คัน รัน 8 ชั่วโมง — พาเลทขึ้นชั้นกี่พาเลท และค้างที่ Dock กี่พาเลท",
    "สร้าง Method <code>LeadTimeMin</code> (ดูบท <a href=\"ai-02.html\">3.2</a> ขั้นที่ 5) และ ExperimentManager ลอง Forklift 1–5 คัน",
    "จำนวน Forklift น้อยที่สุดที่ไม่มีพาเลทค้าง และเวลาเฉลี่ยของจำนวนนั้น",
    "อธิบายด้วยพาเลทต่อชั่วโมง: รถเข้ากี่พาเลท/ชม. Forklift 1 คันยกได้กี่พาเลท/ชม.",
])}
<div class="note">เฉลยอยู่กับผู้สอน — ทำเสร็จแล้วให้ผู้สอนตรวจบนหน้าจอ</div>
'''
