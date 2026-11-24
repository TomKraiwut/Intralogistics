# -*- coding: utf-8 -*-
"""evaluation 2: สอบภาคปฏิบัติ -- user 2026-11-24. Task = build a small inbound warehouse model from scratch (no sample file),
Method LeadTimeMin, ExperimentManager 1-5 forklifts. Answer key (measured on PtS 2504, deterministic) + rubric live in
_No_Upload/exam/ANSWER_KEY_TH.md; the answer sheet is a Google Form (EXAM_FORMS["practical"])."""
from gen_site import screenshot, step_list, side_by_side, EXAM_FORMS, form_embed

TOPICS = []

OBJECTIVES = [
    "สร้างแบบจำลองคลังรับสินค้าจากโจทย์ได้ด้วยตัวเอง",
    "เขียน Method วัดผล และใช้ ExperimentManager หาจำนวน Forklift ที่พอดีได้",
    "อธิบายผลด้วยกำลังการทำงานต่อชั่วโมงได้ และสอบผ่านไม่น้อยกว่าร้อยละ 60",
]

BODY = f'''
<p class="lead" style="max-width:46em;">สร้างแบบจำลอง<strong>ท่ารับสินค้า</strong>ใหม่เองตั้งแต่เฟรมเปล่า แล้วหาว่าต้องใช้ Forklift กี่คัน
— ใช้ทักษะจากบท <a href="logistics-03.html">1.3</a>, <a href="logistics-04.html">1.4</a> และ <a href="ai-02.html">3.2</a>
· <strong>คะแนนเต็ม 100 ผ่าน 60 คะแนนขึ้นไป</strong></p>

<div class="tip"><strong>สิ่งที่ต้องมี:</strong> Plant Simulation (โมเดลใหม่ ไม่ต้องใช้ไฟล์ตัวอย่าง) · ดูบทเรียนบนเว็บได้ ·
<strong>อย่าปิดโปรแกรมหลังส่งคำตอบ</strong> ผู้สอนจะตรวจแบบจำลองบนหน้าจอของคุณ</div>

<h2>โจทย์</h2>
<p>ท่ารับสินค้ามีรถส่งพาเลทเข้ามา<strong>สม่ำเสมอทุก 2 นาที</strong> พาเลทพักที่ท่ารับได้<strong>ไม่เกิน 100 พาเลท</strong>
Forklift แต่ละคัน<strong>ยกพาเลทขึ้นชั้นคันละ 5 นาทีต่อพาเลท</strong> ทำงาน 1 กะ <strong>8 ชั่วโมง</strong></p>

<h3>ส่วนที่ 1: สร้างแบบจำลอง</h3>
<table>
<tr><th>Object</th><th>ชื่อ</th><th>ตั้งค่า</th></tr>
<tr><td>Source</td><td><code>Inbound</code></td><td>Interval 2:00</td></tr>
<tr><td>Buffer</td><td><code>Dock</code></td><td>Capacity 100 · Processing time 0</td></tr>
<tr><td>ParallelStation</td><td><code>Putaway</code></td><td>Processing time 5:00 · X-Dimension = จำนวน Forklift · Y-Dimension 1 · ☐ Start Processing When Full</td></tr>
<tr><td>Drain</td><td><code>Rack</code></td><td>—</td></tr>
<tr><td>EventController</td><td></td><td>End 8:00:00</td></tr>
</table>
<p>ต่อ Connector: Inbound → Dock → Putaway → Rack</p>

<h3>ส่วนที่ 2: Method วัดผล</h3>
<p>สร้าง Method <code>LeadTimeMin</code> คืนค่าเวลาเฉลี่ยตั้งแต่พาเลทมาถึงจนขึ้นชั้น <strong>เป็นนาที</strong>
(จาก <code>Rack.StatAvgLifeSpan</code>) — ถ้ายังไม่มีพาเลทเข้า Rack ให้คืน 0 (ดูตัวอย่างในบท <a href="ai-02.html">3.2</a> ขั้นที่ 5)</p>

<h3>ส่วนที่ 3: ทดลองและตอบคำถาม</h3>
{step_list([
    "ตั้ง Forklift 2 คัน รัน 8 ชั่วโมง → <strong>ข้อ 1</strong> พาเลทที่ขึ้นชั้น (Rack) · <strong>ข้อ 2</strong> พาเลทที่ค้างที่ Dock ตอนจบ",
    "สร้าง ExperimentManager: Input <code>root.Putaway.XDim</code> = 1, 2, 3, 4, 5 · Output <code>root.Rack.StatNumIn</code>, <code>root.Dock.NumMU</code>, <code>root.LeadTimeMin</code> → Reset › Start",
    "<strong>ข้อ 3</strong> จำนวน Forklift น้อยที่สุดที่ไม่มีพาเลทค้างที่ Dock",
    "<strong>ข้อ 4</strong> เวลาเฉลี่ย (นาที) ของจำนวน Forklift ในข้อ 3",
    "<strong>ข้อ 5</strong> อธิบายว่าทำไมจำนวนในข้อ 3 พอ แต่น้อยกว่านั้นไม่พอ — คิดเป็นพาเลทต่อชั่วโมง",
])}
<div class="note"><strong>ตรวจก่อนส่ง:</strong> ถ้าลืมเอาเครื่องหมายออกจาก Start Processing When Full
Forklift จะรอจนทุกช่องมีพาเลทก่อนเริ่มงาน และตัวเลขทุกข้อจะผิด</div>

<h2>เกณฑ์ให้คะแนน (100 คะแนน · ผ่าน 60)</h2>
<table>
<tr><th>ส่วน</th><th>คะแนน</th><th>ผู้สอนตรวจอะไร</th></tr>
<tr><td>สร้างแบบจำลอง</td><td>25</td><td>Object ชื่อและการเชื่อมต่อครบ ค่าที่ตั้งตรงโจทย์</td></tr>
<tr><td>Method LeadTimeMin</td><td>10</td><td>คืนค่าเป็นนาที และไม่ error ตอนเวลา 0</td></tr>
<tr><td>ExperimentManager</td><td>15</td><td>Input / Output ตามโจทย์ รันครบ 5 ชุด</td></tr>
<tr><td>ข้อ 1–4</td><td>40</td><td>ข้อละ 10 คะแนน ตัวเลขตรงกับแบบจำลองที่ถูกต้อง</td></tr>
<tr><td>ข้อ 5</td><td>10</td><td>เหตุผลจากกำลังต่อชั่วโมงถูกต้อง</td></tr>
</table>

<h2>ส่งคำตอบ</h2>
{form_embed(EXAM_FORMS["practical"], "ฟอร์มส่งคำตอบ")}
'''
