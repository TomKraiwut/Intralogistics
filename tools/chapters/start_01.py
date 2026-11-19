# -*- coding: utf-8 -*-
"""start 1: ติดตั้ง Plant Simulation 2504.
Source: 2504_PtS_Intralogistics\\00_Installation\\Installation_Guide.pdf pages 1-3 (page 4 = sales license types, not used).
Images assets/images/start/01-0N.jpg are cropped from pages 2-3 (Host ID blurred in 01-02)."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ตรวจได้ว่าเครื่องของตัวเองพร้อมสำหรับ Plant Simulation 2504",
    "ติดตั้งโปรแกรมได้เองจากไฟล์ <code>PlantSimulation2504_Setup.msi</code>",
    "ตั้งค่า Student License ได้ทั้งตอนเปิดโปรแกรมครั้งแรก และเปลี่ยนภายหลัง",
]

# kept for reference; the page shows BODY
TOPICS = [
    "ความต้องการของเครื่อง",
    "ติดตั้ง Plant Simulation 2504",
    "ตั้งค่า Student License",
]

# Google Drive share link of PlantSimulation2504_Setup.msi ("anyone with the link"); empty = "รับจากผู้สอน"
MSI_URL = "https://drive.google.com/file/d/1igXHnUvl60YaBdmGCDzmSc93ZQ0s5QYz/view?usp=sharing"

if MSI_URL:
    _GET_MSI = (f'<div class="download">\n  <a class="download-btn" href="{MSI_URL}" target="_blank" rel="noopener">'
                f'⬇ ดาวน์โหลดไฟล์ติดตั้ง (Google Drive)</a>\n'
                f'  <p><code>PlantSimulation2504_Setup.msi</code> ประมาณ 300 MB — Google Drive จะเตือนว่าสแกนไวรัสไฟล์ใหญ่ไม่ได้ '
                f'ให้คลิก <strong>Download anyway</strong></p>\n</div>')
else:
    _GET_MSI = '<p>ไฟล์ติดตั้ง <code>PlantSimulation2504_Setup.msi</code> (ประมาณ 300 MB) รับลิงก์จากผู้สอน</p>'

BODY = f'''
<div class="tip"><strong>ทำก่อนวันอบรม:</strong> ติดตั้งโปรแกรมและตั้ง License ให้เสร็จก่อนมาเรียน
ใช้เวลาประมาณ 15–20 นาที — ดาวน์โหลดไฟล์ติดตั้งเก็บลงไดรฟ์ในเครื่องก่อน แล้วค่อยเปิดติดตั้ง</div>

{_GET_MSI}

<div class="note"><strong>ติดตั้งบนเครื่องไหน:</strong> คอมพิวเตอร์ส่วนตัวติดตั้งได้เลย ·
ถ้าเป็นคอมพิวเตอร์ของบริษัท <strong>ต้องแจ้งฝ่าย IT ก่อนติดตั้ง</strong></div>

<h2>1. ความต้องการของเครื่อง</h2>
<table>
<tr><th>รายการ</th><th>ที่แนะนำ</th></tr>
<tr><td>ระบบปฏิบัติการ</td><td>Windows 10 หรือ Windows 11 แบบ 64-bit (<strong>ไม่รองรับ</strong> Windows 7 และ macOS)</td></tr>
<tr><td>CPU</td><td>Intel Core i5, i7, i9 หรือเทียบเท่า</td></tr>
<tr><td>หน่วยความจำ (RAM)</td><td>16 GB</td></tr>
<tr><td>พื้นที่ดิสก์</td><td>ว่างอย่างน้อย 2 GB บน SSD</td></tr>
<tr><td>หน้าจอ</td><td>1920 × 1080 หรือละเอียดกว่า</td></tr>
</table>

<p><strong>ถ้าจะใช้ 3D</strong> (ใช้ในบท 2.8 Advanced 3D Animation)</p>
<ul>
<li>การ์ดจอต้องรองรับ OpenGL (1.1, 1.5, 3.3 หรือ 4.5) — ใช้ได้ทั้ง NVIDIA, AMD และ Intel</li>
<li>การ์ดจอ Intel ต้องเป็นรุ่น HD 4600 ขึ้นไป</li>
<li>ใช้ 3D ได้ครบทุกอย่างเมื่อการ์ดจอรองรับ OpenGL 4.5 ขึ้นไป</li>
</ul>

<div class="note"><strong>ระวัง:</strong> 3D ใช้ไม่ได้บนเครื่องเสมือน (Virtual Machine) หรือ VDI —
ถ้าจะเรียนบท 3D ให้ติดตั้งบนเครื่องจริง</div>

<h2>2. ติดตั้ง Plant Simulation 2504</h2>
{screenshot("assets/images/start/01-01.jpg", "ขั้นตอนติดตั้ง Plant Simulation 2504 ทั้ง 5 ขั้น")}
{step_list([
    "ดับเบิลคลิกไฟล์ <code>PlantSimulation2504_Setup.msi</code>",
    "หน้า Welcome คลิก <strong>Next</strong>",
    "หน้า Destination Folder ใช้โฟลเดอร์ที่ตั้งไว้ <code>C:\\Program Files\\Siemens\\Tecnomatix Plant Simulation 2504\\</code> แล้วคลิก <strong>Next</strong>",
    "หน้า Ready to install คลิก <strong>Install</strong> — ถ้า Windows ถามสิทธิ์ผู้ดูแลเครื่อง (รูปโล่บนปุ่ม) ให้คลิก <strong>Yes</strong>",
    "รอจนขึ้นหน้า Completed แล้วคลิก <strong>Finish</strong> — บนหน้าจอ Desktop จะมีไอคอน <strong>Plant Simulation 2504</strong>",
])}

<div class="note"><strong>ติดตั้งไม่ผ่าน:</strong> การติดตั้งต้องใช้สิทธิ์ผู้ดูแลเครื่อง (Administrator)
— ถ้าเป็นเครื่องของบริษัทแล้วคลิก Install ไม่ได้ ให้ฝ่าย IT ติดตั้งให้</div>

<h2>3. ตั้งค่า Student License</h2>
<p>Student License ใช้ได้ฟรีสำหรับการเรียนรู้ส่วนตัว ตั้งได้ 2 ทาง:
ตอนเปิดโปรแกรมครั้งแรก (3.1) หรือเปลี่ยนภายหลังจากเมนู (3.2)</p>

<div class="note"><strong>ข้อจำกัดของ Student License:</strong>
แบบจำลองหนึ่งตัวมี Object ได้ <strong>ไม่เกิน 80 ตัว</strong> ·
ใช้เพื่อการเรียนเท่านั้น ห้ามใช้กับงานโครงการของบริษัท งานรับจ้าง หรืองานเชิงพาณิชย์ และโอนสิทธิ์ให้ผู้อื่นไม่ได้</div>

<div class="tip"><strong>ใช้กับหลักสูตรนี้ได้ครบ:</strong> แบบจำลองทุกไฟล์ของหลักสูตรมี Object ไม่เกิน 80 ตัว
จึงเปิดและรันด้วย Student License ได้ทุกบท</div>

<h3>3.1 เปิดโปรแกรมครั้งแรก</h3>
{side_by_side(
    screenshot("assets/images/start/01-02.jpg", "หน้าต่าง License Setup ตอนเปิดโปรแกรมครั้งแรก"),
    step_list([
        "ดับเบิลคลิกไอคอน <strong>Plant Simulation 2504</strong> บน Desktop",
        "หน้าต่าง <strong>License Setup</strong> ขึ้นมา เพราะยังไม่มี License — คลิกปุ่มล่างสุด "
        "<strong>I am a student and want to use a free student license where I can use the software with some limitations.</strong>",
    ])
)}

<h3>3.2 เปลี่ยน License ภายหลัง</h3>
<p>ใช้เมื่อปิดหน้าต่าง License Setup ไปแล้ว หรือเคยเลือก License แบบอื่นไว้</p>
{screenshot("assets/images/start/01-03.jpg", "ตั้ง License Type เป็น Student ในหน้าต่าง Preferences")}
{step_list([
    "เปิด Plant Simulation 2504",
    "คลิกเมนู <strong>File</strong>",
    "คลิก <strong>Preferences</strong>",
    "คลิกแท็บ <strong>License</strong>",
    "ช่อง <strong>License Type</strong> เลือก <strong>Student</strong>",
    "คลิก <strong>OK</strong>",
])}

<h2>ตรวจว่าพร้อมเรียน</h2>
<ul>
<li>เปิด Plant Simulation 2504 ได้ และไม่มีหน้าต่าง License Setup ขึ้นมาอีก</li>
<li>ไปต่อที่ <a href="start-02.html">0.2 โหลดไฟล์ตัวอย่างของหลักสูตร</a> แล้วเปิดโมเดลแรกทดสอบ</li>
</ul>
'''
