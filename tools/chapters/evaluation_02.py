# -*- coding: utf-8 -*-
"""evaluation 2: สอบภาคปฏิบัติ -- 2026-11-27: the exam is the PRACTICE part (40 software MCQ × 2) of the post-test form.
The earlier build-it-yourself task stays as an ungraded review exercise (answer key in _No_Upload/exam/ANSWER_KEY_TH.md)."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "ทบทวนการใช้ Plant Simulation ของ 4 หมวดวิชาก่อนสอบ",
    "ทำแบบทดสอบหลังเรียนส่วนภาคปฏิบัติ (80 คะแนน) ได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ภาคปฏิบัติอยู่ใน<a href="post-test.html"><strong>แบบทดสอบหลังเรียน</strong></a>
(ส่วนที่สองของฟอร์ม ต่อจากภาคทฤษฎี) — <strong>คำถามการใช้โปรแกรม 40 ข้อ ข้อละ 2 คะแนน</strong> หมวดละ 10 ข้อ
ตรวจอัตโนมัติ · รวมกับภาคทฤษฎี (บท <a href="evaluation-01.html">5.1</a>) เป็น 100 คะแนน <strong>ผ่านเมื่อได้ 60 คะแนนขึ้นไป</strong></p>

<h2>ขอบเขต</h2>
<table>
<tr><th>หมวดวิชา</th><th>ทบทวนบท</th><th>ข้อ / คะแนน</th></tr>
<tr><td>หลักการจัดการโลจิสติกส์</td><td><a href="logistics-02.html">1.2</a>–<a href="logistics-04.html">1.4</a> — Factory 51 · Source / Station / Drain · Display · EventController · คอขวด</td><td>10 / 20</td></tr>
<tr><td>การจัดการเชิงกลยุทธ์และการตัดสินใจ</td><td><a href="strategy-02.html">4.2</a> (+ 4.1) — จำลองจำนวนรถหลายสถานการณ์ · PV เช่า / ซื้อ · ตัดสินใจ 3 วิธี</td><td>10 / 20</td></tr>
<tr><td>การจัดการสินค้าคงคลังและสร้างแบบจำลอง</td><td><a href="simulation-02.html">2.2</a>–<a href="simulation-08.html">2.8</a> — Library HBW · Sensor · WMS · Method Init · คนและกะ · 3D</td><td>10 / 20</td></tr>
<tr><td>การใช้แบบจำลองเสมือนจริงวิเคราะห์</td><td><a href="ai-02.html">3.2</a>–<a href="ai-03.html">3.3</a> — Excel · ExperimentManager · GAWizard · NeuralNet</td><td>10 / 20</td></tr>
</table>
<div class="tip"><strong>เปิดโปรแกรมระหว่างทำได้:</strong> คำถามถามเรื่องเมนู หน้าต่าง และผลจากแบบจำลองในบทเรียน
ถ้าไม่แน่ใจ ลองเปิดไฟล์ตัวอย่างหรือหน้าบทเรียนดูได้ตามที่ผู้สอนอนุญาต</div>

<div class="download"><a class="download-btn" href="post-test.html">ไปที่แบบทดสอบหลังเรียน</a></div>

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
