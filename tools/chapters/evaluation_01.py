# -*- coding: utf-8 -*-
"""evaluation 1: สอบภาคทฤษฎี -- user 2026-11-24. The exam itself is a Google Form built by _No_Upload/exam/ExamCode.gs
(createExams); its link goes into gen_site.EXAM_FORMS["theory"]. Questions/answers never appear on this page."""
from gen_site import screenshot, step_list, side_by_side, EXAM_FORMS, form_embed

TOPICS = []

OBJECTIVES = [
    "ทบทวนเนื้อหาภาคทฤษฎีของหัวข้อ 1–4 ก่อนสอบ",
    "สอบภาคทฤษฎีผ่านเกณฑ์ไม่น้อยกว่าร้อยละ 60",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ข้อสอบปรนัย <strong>20 ข้อ ข้อละ 1 คะแนน</strong> ทำใน Google Forms
<strong>ผ่านเมื่อได้ 12 คะแนนขึ้นไป (ร้อยละ 60)</strong> — ผู้สอนแจ้งผลหลังทุกคนส่งครบ</p>

<h2>ขอบเขต: บทภาคทฤษฎี 5 บท</h2>
<table>
<tr><th>บท</th><th>ทบทวนเรื่อง</th><th>จำนวนข้อ</th></tr>
<tr><td><a href="logistics-01.html">1.1</a></td><td>โลจิสติกส์ · Intralogistics · ชั้นวาง (FIFO / LIFO) · WMS / WCS · คะแนนความเสี่ยง</td><td>4</td></tr>
<tr><td><a href="simulation-01.html">2.1</a></td><td>ABC · EOQ · Safety Stock · จุดสั่งซื้อ (ROP) · Discrete-Event Simulation</td><td>4</td></tr>
<tr><td><a href="simulation-05.html">2.5</a></td><td>Forklift · AGV · AMR · การป้อนข้อมูลเข้าแบบจำลอง · Verification / Validation</td><td>4</td></tr>
<tr><td><a href="ai-01.html">3.1</a></td><td>Digital Shadow / Twin · ช่วงความเชื่อมั่น · Genetic Algorithm · Neural Network</td><td>4</td></tr>
<tr><td><a href="strategy-01.html">4.1</a></td><td>ระยะคืนทุน · NPV · เทียบกับทางเลือกที่ไม่ลงทุน · ตัดสินใจภายใต้ความไม่แน่นอน</td><td>4</td></tr>
</table>

<h2>ก่อนสอบ</h2>
{step_list([
    "เตรียมเครื่องคิดเลข — มีข้อคำนวณ EOQ, ROP, ช่วงความเชื่อมั่น และ NPV (ใช้สูตรและตัวคูณตามบทเรียน)",
    "ใช้อีเมลของตัวเองตอนเข้าฟอร์ม และกรอกชื่อ-นามสกุลให้ตรงกับรายชื่อผู้เรียน",
    "เปิดเว็บบทเรียนดูได้ระหว่างสอบหรือไม่ — ทำตามที่ผู้สอนแจ้งในห้อง",
    "ส่งได้ครั้งเดียว ตรวจคำตอบก่อนกด Submit",
])}

<h2>แบบทดสอบ</h2>
{form_embed(EXAM_FORMS["theory"], "ข้อสอบภาคทฤษฎี")}

<div class="tip"><strong>ไม่ผ่าน:</strong> ทบทวนบทในตารางด้านบน แล้วนัดผู้สอนเพื่อสอบซ่อม</div>
'''
