# -*- coding: utf-8 -*-
"""evaluation 1: สอบภาคทฤษฎี -- 2026-11-27: the exam is the THEORY part of the post-test form (post-test.html,
built from _No_Upload/exam/post_test_draft_TH.md → PostTestCode.gs). No questions or answers on this page."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "ทบทวนเนื้อหาภาคทฤษฎีของ 4 หมวดวิชาก่อนสอบ",
    "ทำแบบทดสอบหลังเรียนส่วนภาคทฤษฎี (20 คะแนน) ได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ภาคทฤษฎีอยู่ใน<a href="post-test.html"><strong>แบบทดสอบหลังเรียน</strong></a>
(ส่วนแรกของฟอร์ม) — ปรนัย <strong>10 ข้อ ข้อละ 2 คะแนน = 20 คะแนน</strong> ครอบคลุม 4 หมวดวิชา ตรวจอัตโนมัติ
· รวมกับภาคปฏิบัติ (บท <a href="evaluation-02.html">5.2</a>) เป็น 100 คะแนน <strong>ผ่านเมื่อได้ 60 คะแนนขึ้นไป</strong></p>

<h2>ขอบเขต</h2>
<table>
<tr><th>หมวดวิชา</th><th>ทบทวนบท</th></tr>
<tr><td>หลักการจัดการโลจิสติกส์</td><td><a href="logistics-01.html">1.1</a> — Intralogistics · ชั้นวาง (FIFO / LIFO) · WMS · ความเสี่ยง · งานในคลัง</td></tr>
<tr><td>การจัดการเชิงกลยุทธ์และการตัดสินใจ</td><td><a href="strategy-01.html">4.1</a> — NPV · ระยะคืนทุน · ทางเลือกที่ไม่ลงทุน · Maximin · 3PL</td></tr>
<tr><td>การจัดการสินค้าคงคลังและสร้างแบบจำลอง</td><td><a href="simulation-01.html">2.1</a>, <a href="simulation-05.html">2.5</a> — ABC · EOQ · ROP · กราฟสต็อก · Verification</td></tr>
<tr><td>การใช้แบบจำลองเสมือนจริงวิเคราะห์</td><td><a href="ai-01.html">3.1</a> — Digital Twin · ช่วงความเชื่อมั่น · GA · Neural Network · DOE</td></tr>
<tr><td><strong>รวม</strong></td><td><strong>10 ข้อ × 2 คะแนน = 20 คะแนน</strong></td></tr>
</table>

<h2>ก่อนสอบ</h2>
{step_list([
    "เตรียมเครื่องคิดเลข — มีข้อคำนวณ EOQ, ROP, ช่วงความเชื่อมั่น และ NPV (ใช้สูตรและตัวคูณตามบทเรียน)",
    "ใช้อีเมลเดียวกับตอนทำแบบทดสอบก่อนเรียน และกรอกชื่อ-นามสกุลให้ตรงกับรายชื่อผู้เรียน",
    "ทำต่อเนื่องจนจบภาคปฏิบัติในฟอร์มเดียวกัน แล้วกด Submit ครั้งเดียว",
])}

<div class="download"><a class="download-btn" href="post-test.html">ไปที่แบบทดสอบหลังเรียน</a></div>
'''
