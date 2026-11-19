# -*- coding: utf-8 -*-
"""start 2: โหลดไฟล์ตัวอย่างของหลักสูตร.
Files live in the user's shared Google Drive folder "01_Training_Model" (anyone with the link, viewer);
the user adds files over time. FILES lists them for the table -- empty = "ไฟล์จะทยอยเพิ่ม" note."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ดาวน์โหลดไฟล์ตัวอย่างของหลักสูตรจาก Google Drive",
    "เก็บไฟล์ไว้ในโฟลเดอร์ที่โปรแกรมเปิดได้โดยไม่มีปัญหา",
    "เปิดไฟล์โมเดลใน Plant Simulation 2504 เพื่อทดสอบว่าพร้อมเรียน",
]

# kept for reference; the page shows BODY
TOPICS = [
    "ดาวน์โหลดชุดไฟล์ของหลักสูตร",
    "เก็บไฟล์ในโฟลเดอร์ที่ถูกต้อง",
    "เปิดโมเดลทดสอบ",
    "ตารางไฟล์",
]

# Google Drive folder "01_Training_Model" (shared: anyone with the link can view)
FOLDER_URL = "https://drive.google.com/drive/folders/1k1a3frNfgsbFyR7Rul0bFnxQqvMtbt9f?usp=sharing"

# (file or folder name, used in chapter, what it is) -- fill in as files are added to the Drive folder
FILES = []

if FILES:
    _rows = "\n".join(f"<tr><td><code>{n}</code></td><td>{c}</td><td>{d}</td></tr>" for n, c, d in FILES)
    _FILE_TABLE = f'''<table>
<tr><th>ไฟล์ / โฟลเดอร์</th><th>ใช้ในบท</th><th>คืออะไร</th></tr>
{_rows}
</table>'''
else:
    _FILE_TABLE = '''<div class="note"><strong>ไฟล์จะทยอยเพิ่ม:</strong> ไฟล์ของแต่ละบทจะเพิ่มเข้าโฟลเดอร์เดิมก่อนวันอบรม
ใช้ลิงก์เดิมได้ตลอด — ก่อนวันอบรมให้ดาวน์โหลดอีกครั้งเพื่อให้ได้ไฟล์ครบ</div>'''

BODY = f'''
<div class="download">
  <a class="download-btn" href="{FOLDER_URL}" target="_blank" rel="noopener">⬇ เปิดโฟลเดอร์ไฟล์ตัวอย่าง (Google Drive)</a>
  <p>โฟลเดอร์ <code>01_Training_Model</code> — เปิดดูได้โดยไม่ต้องล็อกอิน</p>
</div>

<h2>1. ดาวน์โหลดไฟล์</h2>
{step_list([
    "คลิกปุ่ม <strong>เปิดโฟลเดอร์ไฟล์ตัวอย่าง</strong> ด้านบน",
    "ดาวน์โหลดทั้งโฟลเดอร์: คลิกชื่อโฟลเดอร์ <strong>01_Training_Model</strong> ด้านบนของหน้า แล้วเลือก <strong>Download</strong> "
    "— Google Drive จะรวมไฟล์เป็น <code>.zip</code> ให้ (ถ้าไฟล์ใหญ่อาจได้หลาย zip)",
    "ถ้าต้องการบางไฟล์: คลิกขวาที่ไฟล์นั้นแล้วเลือก <strong>Download</strong>",
])}

<h2>2. เก็บไฟล์ในโฟลเดอร์ที่ถูกต้อง</h2>
{step_list([
    "สร้างโฟลเดอร์ <code>C:\\PtS_Intralogistics</code>",
    "แตกไฟล์ <code>.zip</code> (คลิกขวา → <strong>Extract All…</strong>) ลงในโฟลเดอร์นี้",
    "ตรวจว่าไฟล์ <code>.spp</code> กับไฟล์ข้อมูล (เช่น Excel) ที่มาด้วยกันอยู่ในโฟลเดอร์เดียวกัน",
])}

<div class="note"><strong>ระวัง:</strong> อย่าเปิดไฟล์จากในไฟล์ <code>.zip</code> โดยตรง และอย่าเก็บไว้ในโฟลเดอร์ที่ชื่อมีภาษาไทย
— แบบจำลองที่อ่านไฟล์ข้อมูลจะหาไฟล์จากโฟลเดอร์ของตัวเอง ถ้าแยกไฟล์ไว้คนละที่จะอ่านข้อมูลไม่ได้</div>

<h2>3. เปิดโมเดลทดสอบ</h2>
{step_list([
    "เปิด Plant Simulation 2504",
    "คลิกเมนู <strong>File</strong> → <strong>Open</strong> แล้วเลือกไฟล์ <code>.spp</code> ในโฟลเดอร์ <code>C:\\PtS_Intralogistics</code>",
    "ดับเบิลคลิก Frame ใน Class Library › <strong>Models</strong> เพื่อดูแบบจำลอง",
])}

<div class="tip"><strong>ไฟล์ทุกไฟล์บันทึกด้วย Plant Simulation 2504:</strong> เปิดด้วยเวอร์ชัน 2504 หรือใหม่กว่าได้
แต่ถ้าบันทึกทับด้วยเวอร์ชันใหม่กว่า จะเปิดกลับใน 2504 ไม่ได้ — ระหว่างเรียนให้ใช้ 2504 เท่านั้น</div>

<h2>4. ไฟล์ในโฟลเดอร์</h2>
{_FILE_TABLE}
'''
