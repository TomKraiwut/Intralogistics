# -*- coding: utf-8 -*-
"""evaluation 1: สอบภาคทฤษฎี -- 2026-11-27: the separate 5.1 Google Form (EXAM_FORMS["theory"]), edited by the user himself
to 10 questions × 2 points. Page text follows the user's own edit of evaluation/01.html (scope table removed, step 1 shortened).
No questions or answers on this page."""
from gen_site import screenshot, step_list, side_by_side, EXAM_FORMS, form_embed

TOPICS = []

OBJECTIVES = [
    "ทบทวนเนื้อหาภาคทฤษฎีของ 4 หมวดวิชาก่อนสอบ",
    "ทำแบบทดสอบภาคทฤษฎี (20 คะแนน) ได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ข้อสอบภาคทฤษฎี — ปรนัย <strong>10 ข้อ ข้อละ 2 คะแนน = 20 คะแนน</strong>
ครอบคลุม 4 หมวดวิชา ตรวจอัตโนมัติ · รวมกับภาคปฏิบัติ (บท <a href="evaluation-02.html">5.2</a>) เป็น 100 คะแนน
<strong>ผ่านเมื่อได้ 60 คะแนนขึ้นไป</strong></p>

<h2>ก่อนสอบ</h2>
{step_list([
    "ทบทวนเนื้อหาภาคทฤษฎี",
    "ใช้อีเมลเดียวกับตอนทำแบบทดสอบก่อนเรียน และกรอกชื่อ-นามสกุลให้ตรงกับรายชื่อผู้เรียน",
    "ส่งได้ครั้งเดียว ตรวจคำตอบก่อนกด Submit",
])}

<h2>แบบทดสอบ</h2>
{form_embed(EXAM_FORMS["theory"], "ข้อสอบภาคทฤษฎี")}
'''
