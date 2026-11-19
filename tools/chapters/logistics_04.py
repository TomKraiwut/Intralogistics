# -*- coding: utf-8 -*-
"""logistics 4 (practice): Bottleneck -- user 2026-11-19: from 2606_Step_By_Step\\02_Bottleneck_ParallelStation\\02_Bottleneck_ParallelStation.pptx
WITHOUT ParallelStation (steps 7-11 and try-it 2 removed). Ported from the PlantSimulation site lessons_02.py (same deck, 2606 screens).
Numbers re-measured on 2504 2026-11-19 with a new model (Source -> Station1..5 10 s -> Drain, 1 h): 355 / Model2 177 (Blocked 50 %,
Waiting 51 %) / Model3 + Station32 354 (Station2 exit strategy Cyclic) / try-it 177, 177, 237, 355, 236 = same as 2606."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "สร้าง / สลับ Frame แสดงชื่อ object และย้าย ลบ แทรก object ใน Frame ได้",
    "วาง Display และ Chart (Resource Statistics) ด้วยการลาก object มาวาง แล้วอ่านผลได้",
    "หาคอขวดจากสีใน Chart (Working / Blocked / Waiting) ได้",
    "แก้คอขวดด้วยการเพิ่มเครื่องขนาน และย้าย ลบ แทรก Object ในไลน์ได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ต่อจากบท <a href="logistics-03.html">1.3</a> — ใช้ไลน์ผลิต 5 สถานี อ่านผลจาก Display และ Chart
หาเครื่องที่ช้าที่สุด (<strong>คอขวด / Bottleneck</strong>) แล้วแก้ด้วยการเพิ่มเครื่องขนาน ทั้งหมด 6 ขั้น ไม่ต้องเขียนโค้ด
— ภาพหน้าจอในบทนี้มาจาก Plant Simulation 2606 ขั้นตอนเหมือนกันใน 2504 และตัวเลขทุกตัววัดซ้ำบน 2504 แล้วได้เท่ากัน</p>

<h2>ภาพรวม: 6 ขั้น จากไลน์ปกติ ถึงแก้คอขวด</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th><th>ขั้น</th></tr>
<tr><td>1</td><td>เปิด Frame Model</td><td>ไลน์ 5 สถานี เวลาเท่ากัน 0:10</td><td>1</td></tr>
<tr><td>2</td><td>วาง Display + Chart</td><td>จาก Toolbox แล้วลาก object มาวาง</td><td>2–3</td></tr>
<tr><td>3</td><td>รัน Model อ่านผล</td><td>FG 355 ทุกแท่งสีเขียว</td><td>4</td></tr>
<tr><td>4</td><td>Model2 มีคอขวด</td><td>Station3 ช้าเป็น 0:20 ได้ 177</td><td>5</td></tr>
<tr><td>5</td><td>Model3 เพิ่มเครื่อง</td><td>Station32 วางขนาน ได้ 354</td><td>6</td></tr>
</table>

<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 — สร้างไลน์ Source → Station1–5 → Drain เองแบบบท 1.3 (ทุกเครื่อง 0:10)
แล้วทำ Frame ถัดไปด้วยคลิกขวา › <code>Duplicate</code> &nbsp;·&nbsp; ผลผลิตก่อน–หลังแก้คอขวด <strong>177 → 354 ชิ้น/ชม.</strong>
(ทุกตัวเลขในบทนี้วัดจริงทั้งใน Plant Simulation 2504 และ 2606 จำลอง 1 ชั่วโมง)
</div>
<div class="note">
<strong>ต่อจากบท 1.3:</strong> การวาง object ต่อเส้น ตั้งค่า และกด Run ทำเหมือนบท <a href="logistics-03.html">1.3</a>
บทนี้เน้นอ่านผล หาเครื่องที่ช้าที่สุด แล้วแก้ด้วยการเพิ่มเครื่องขนาน
</div>

<h2>3 Frame เล่าเรื่องเดียวกัน</h2>
<table>
<tr><th>ลำดับ</th><th>Frame</th><th>เรื่อง</th><th>ขั้น</th></tr>
<tr><td>1</td><td><code>Model</code></td><td>ไลน์สมดุล ทุกเครื่อง 0:10 ได้ 355 ชิ้น/ชม.</td><td>1–4</td></tr>
<tr><td>2</td><td><code>Model2</code></td><td>Station3 ช้าเป็น 0:20 ทั้งไลน์เหลือ 177 ชิ้น/ชม.</td><td>5</td></tr>
<tr><td>3</td><td><code>Model3</code></td><td>เพิ่ม Station32 ขนานกับ Station3 ได้ 354 ชิ้น/ชม.</td><td>6</td></tr>
</table>
<p>บทนี้ในตัวเลข: <strong>3</strong> Frame · <strong>5</strong> Station ต่อไลน์ · <strong>60</strong> นาทีจำลองต่อการรัน
— เรื่องของบทนี้: ไลน์ปกติ → มีเครื่องหนึ่งช้า → แก้ด้วยการเพิ่มเครื่องขนาน</p>

<h2>ขั้นที่ 1: Frame Model ไลน์ 5 สถานี</h2>
<p>ดับเบิลคลิก <code>Models › Model</code> (ภาพนี้เป็น Planning View ก่อนรัน)</p>
{screenshot("assets/images/logistics/04-01.jpg", "Frame Model ไลน์ 5 สถานี ก่อนรัน (Planning View)")}
{step_list([
    "<strong>Source</strong> — ปล่อยงานทันทีที่ว่าง (Interval 0)",
    "<strong>Station1–5</strong> — ทุกเครื่อง 0:10 ต่อชิ้น",
    "<strong>Drain</strong> — ชิ้นงานที่เสร็จ",
    "<strong>Display</strong> — Production Time = เวลาจำลอง",
    "<strong>Display</strong> — FG = จำนวนชิ้นที่เสร็จ",
    "<strong>Chart</strong> — Resource Statistics สถานะเครื่อง",
    "<strong>EventController</strong> — End 1:00:00",
])}
<div class="note"><strong>เปิด Frame:</strong> Class Library › Models ดับเบิลคลิกชื่อ Frame เพื่อเปิด ถ้าหน้าต่างเล็ก กดปุ่ม □ มุมขวาบนของ Frame เพื่อขยาย</div>

<h2>ขั้นที่ 1: สร้าง Frame ใหม่ และสลับ Frame</h2>
<p>Class Library › คลิกขวา <code>Models</code> › <code>New</code> › <code>Model Frame</code></p>
{screenshot("assets/images/logistics/04-02.jpg", "เมนูคลิกขวา Models › New › Model Frame และ Frame ใหม่ Model6")}
{step_list([
    "<strong>คลิกขวาที่ Models</strong> ใน Class Library",
    "<code>New</code>",
    "<code>Model Frame</code>",
    "<strong>Model6</strong> — ขึ้นท้ายรายการ พิมพ์ชื่อใหม่ได้ทันที",
    "<strong>EventController</strong> — Frame ใหม่มีมาให้ 1 ตัว (Frame ใหม่เปิดเป็นมุมมอง 3D)",
    "<strong>แท็บด้านล่าง</strong> — คลิกเพื่อสลับ Frame",
    "<strong>×</strong> — ปิด Frame · เปิดใหม่ = ดับเบิลคลิกชื่อใน Class Library",
])}
<div class="tip"><strong>มีไลน์อยู่แล้ว:</strong> คลิกขวาที่ Frame เดิม (เช่น Model) › <code>Duplicate</code> ได้ Frame ใหม่พร้อม Object ทุกตัว
แล้วแก้เฉพาะจุดที่ต่าง เช่น Model2</div>

<h2>ขั้นที่ 1: แสดงชื่อ Object ใน Frame</h2>
<p>คลิกขวาที่ Object › <code>Edit 3D Properties</code> › แท็บ <code>Captions</code></p>
{side_by_side(
    screenshot("assets/images/logistics/04-03.jpg", "เมนูคลิกขวาที่ Station1"),
    screenshot("assets/images/logistics/04-04.jpg", "หน้าต่าง Edit 3D Properties แท็บ Captions"),
)}
{step_list([
    "คลิกขวาที่ <strong>Station1</strong>",
    "<code>Edit 3D Properties...</code> — หรือคลิกเลือกแล้วกด <code>Space</code>",
    "แท็บ <code>Captions</code>",
    "<code>Name / Label Activated</code> — คลิกช่องสี่เหลี่ยมด้านหน้าให้ขึ้นเครื่องหมายถูก ☑ = เปิดการแสดงชื่อ",
    "<code>OK</code> — ชื่อขึ้นใต้ Object",
])}

<h2>ขั้นที่ 1: ทำซ้ำทุก Object แล้วอ่านชื่อได้ทั้งไลน์</h2>
{side_by_side(
    screenshot("assets/images/logistics/04-05.jpg", "ก่อน (บน) และหลังตั้งชื่อครบทุก Object (ล่าง)"),
    step_list([
        "<strong>EventController</strong> — ชื่อขึ้นใต้นาฬิกา",
        "<strong>Source</strong> — ทำทีละ Object เหมือนขั้นก่อนหน้า",
        "<strong>Station1–5</strong> — ชื่อตรงกับใน Class Library และใน Chart",
        "<strong>Drain</strong> — ชื่อถูกป้าย FG บังอยู่ (วางที่เดียวกัน)",
    ])
)}
<div class="note"><strong>ชื่อไม่ขึ้น:</strong> ดูแท็บ View (ริบบอน 3D) › ปุ่ม <code>Names</code> ต้องเปิดอยู่ ปุ่มนี้เปิด / ปิดชื่อของทุก Object ใน Frame พร้อมกัน
— ตั้งที่ Object ใน Frame มีผลกับ Object นั้นตัวเดียว ถ้าตั้งที่ Class ใน Class Library ทุก Object ที่สืบทอดมาจะแสดงชื่อด้วย</div>

<h2>ขั้นที่ 2: วาง Display จาก Toolbox</h2>
<p>Toolbox › <code>User Interface</code> › <code>Display</code></p>
{screenshot("assets/images/logistics/04-06.jpg", "Toolbox แท็บ User Interface และ Display ที่วางใหม่ใกล้ Drain")}
{step_list([
    "แท็บ <strong>User Interface</strong> ใน Toolbox",
    "<strong>Display</strong> — คลิกไอคอน 9.86",
    "<strong>คลิกใน Frame</strong> — วาง Display ใกล้ Drain",
])}
<div class="tip"><strong>ภาพนี้:</strong> ลบป้าย FG เดิมใน Frame Model ออกก่อน แล้ววางใหม่ให้ดูทีละขั้น (ไม่ได้บันทึกไฟล์) ถ้าทำตาม ให้ลบป้ายเดิมก่อนเหมือนกัน
— Display ใหม่ยังไม่รู้ว่าจะแสดงค่าอะไร บนจอจึงเป็นกรอบเปล่าชื่อ Display</div>

<h2>ขั้นที่ 2: ลาก Drain ไปวางบน Display</h2>
{screenshot("assets/images/logistics/04-07.jpg", "ลาก Drain ไปปล่อยบน Display (ซ้าย) และ Display แสดง 0 (ขวา)")}
{step_list([
    "<strong>คลิกค้างที่ Drain</strong> แล้วลากไป",
    "<strong>ปล่อยบน Display</strong> — ห้ามปล่อยบนพื้นว่าง ไม่งั้น Drain จะย้ายที่แทน",
    "<strong>Display แสดง 0</strong> — Path = <code>Drain.statNumIn</code> ตั้งให้เอง = จำนวนชิ้นที่เข้า Drain",
])}

<h2>ขั้นที่ 2: คลิกขวา Start แล้วอ่านค่า</h2>
{screenshot("assets/images/logistics/04-08.jpg", "แถบเครื่องมือเมื่อคลิกขวาที่พื้น Frame (ซ้าย) และค่าหลังรัน 1 ชั่วโมง (ขวา)")}
{step_list([
    "<strong>Start/Stop Simulation</strong> — ปุ่มเขียวในแถบเครื่องมือที่ขึ้นตอนคลิกขวา",
    "<strong>Reset Simulation</strong> — ปุ่มแดง กลับไปเริ่มต้น ค่าบน Display กลับเป็น 0",
    "<strong>355</strong> — ชิ้นที่เสร็จใน 1 ชั่วโมง อีก 5 ชิ้นยังอยู่ในเครื่อง (Work in Process)",
])}
<p>ปุ่ม Start และ Reset เดียวกันนี้อยู่ที่ริบบอน <code>Home › Event Controller</code> ด้วย</p>

<h2>ขั้นที่ 2: ข้อความนำหน้า และรูปแบบตัวอักษร</h2>
<p>ดับเบิลคลิก Display · แท็บ <code>Data</code> (ซ้าย) · แท็บ <code>Display</code> (ขวา)</p>
{screenshot("assets/images/logistics/04-09.jpg", "หน้าต่าง Display แท็บ Data (ซ้าย) และแท็บ Display (ขวา)")}
{step_list([
    "<strong>Path</strong> — ป้ายเวลา = <code>EventController.SimTime</code>",
    '<strong>Comment</strong> — ข้อความหน้าตัวเลข เช่น "Production Time =" และ "FG ="',
    "แท็บ <strong>Display</strong> — รูปแบบของป้าย",
    "<strong>Font Size</strong> — ขนาดตัวอักษร",
    "<strong>Color</strong> — สีตัวอักษร แล้วกด <code>Apply</code>",
])}
<div class="note"><strong>ป้าย FG:</strong> ใช้ Path = <code>Drain.statNumIn</code> (ได้มาจากการลาก Drain) และ Comment "FG =" บน Frame จึงขึ้นเป็น FG = 355
(ภาพซ้ายเป็นป้าย Production Time หลังรัน ค่า Value จึงเป็น 3600 วินาที)</div>

<h2>ขั้นที่ 3: วาง Chart แล้วลาก Station1 มาวาง</h2>
<p>Toolbox › <code>User Interface</code> › <code>Chart</code></p>
{side_by_side(
    screenshot("assets/images/logistics/04-10.jpg", "วาง Chart ใต้ไลน์ แล้วลาก Station1 มาวาง"),
    screenshot("assets/images/logistics/04-11.jpg", "หน้าต่าง Statistics Type"),
)}
{step_list([
    "แท็บ <strong>User Interface</strong>",
    "<strong>Chart</strong> — คลิกไอคอนกราฟแท่ง",
    "<strong>คลิกใน Frame</strong> — วาง Chart ใต้ไลน์",
    "<strong>ลาก Station1</strong> ไปปล่อยบน Chart",
    "<strong>Resource Statistics</strong> ใน Statistics Type (= สถานะของเครื่อง)",
    "<code>OK</code>",
])}

<h2>ขั้นที่ 3: ลาก Station2–5 แล้วเปิด / ปิดหน้าต่าง Chart</h2>
{screenshot("assets/images/logistics/04-12.jpg", "หน้าต่าง Chart หลังรัน (ซ้าย) และเมนูคลิกขวาที่ Chart (ขวา)")}
{step_list([
    "<strong>Station1–5</strong> — ลากทีละเครื่องมาปล่อยบน Chart ได้ 5 แท่ง (ครั้งต่อไปไม่ถาม Statistics Type)",
    "ปุ่ม <strong>×</strong> — ปิดหน้าต่าง Chart",
    "คลิกขวาที่ Chart › <code>Show</code> — เปิดหน้าต่างอีกครั้ง",
])}
<p>หลังวาง Station แรก หน้าต่าง Chart เปิดขึ้นเอง ภาพซ้ายถ่ายหลังรัน 1 ชั่วโมง ทุกเครื่อง Working เกือบ 100%</p>

<h2>ขั้นที่ 3: ค่าของ Chart ที่ตั้งให้</h2>
<p>ดับเบิลคลิก Chart › แท็บ <code>Data</code></p>
{side_by_side(
    screenshot("assets/images/logistics/04-13.jpg", "หน้าต่าง Chart แท็บ Data"),
    step_list([
        "<strong>Collect Data</strong> — ช่องหน้าชื่อมีเครื่องหมายถูก ☑ = เก็บข้อมูลระหว่างรัน",
        "<strong>Data Source = Input Channels</strong> — แสดงข้อมูลของ object ที่เลือก",
        "ปุ่ม <strong>Input Channels</strong> — รายการ Station1–5 ที่ลากมาวาง",
        "<strong>Mode = Sample, Interval 1:00</strong> — เก็บค่าทุก 1 นาที",
    ])
)}
<div class="tip"><strong>ไม่ต้องพิมพ์เอง:</strong> ลาก object มาวางบน Chart = เพิ่มเข้า Input Channels ให้เอง ใช้ปุ่มนี้เมื่ออยากลบหรือเรียงลำดับแท่ง</div>

<h2>ขั้นที่ 3: Chart แบบแบนบน Frame หรือแบบ 3D</h2>
<p>แท็บ <code>Display</code>: Model (ซ้าย) · Model2 (ขวา)</p>
{screenshot("assets/images/logistics/04-14.jpg", "แท็บ Display ของ Chart: Model (ซ้าย) และ Model2 (ขวา)")}
{step_list([
    "<strong>Category</strong> — <code>Chart</code> = กราฟแบนบน Frame (Model) · <code>3D Chart</code> = ป้ายกราฟตั้งในฉาก 3D (Model2–Model3)",
    "<strong>Chart Type = 100% Stacked Columns</strong> — แท่งละ 100% แบ่งสีตามสถานะ",
    "<strong>Display in Frame</strong> — ช่องหน้าชื่อมีเครื่องหมายถูก ☑ = แสดงกราฟบน Frame แทนไอคอน",
])}
<div class="note"><strong>ระวัง:</strong> 3D Chart วาดใหม่ระหว่างรันแบบมีภาพเคลื่อนไหว ถ้ารันแบบไม่มีภาพเคลื่อนไหว กราฟจะว่าง (ทดสอบใน Plant Simulation 2606)
— Chart แบบแบนมองเห็นใน Planning View ส่วน 3D Chart ต้องดูในมุมมอง 3D</div>

<h2>ขั้นที่ 3: ตั้ง 3D Chart ให้ยืนอยู่หลังไลน์</h2>
<p>Model2 › Chart: แท็บ <code>Display</code> (ซ้าย) · ปุ่ม <code>3D</code> › <code>Transformation</code> (ขวา)</p>
{screenshot("assets/images/logistics/04-15.jpg", "Model2 › Chart: แท็บ Display (ซ้าย) และหน้าต่าง 3D แท็บ Transformation (ขวา)")}
{step_list([
    "<strong>Category = 3D Chart</strong> — ช่อง Display in Frame ขึ้นเครื่องหมายถูก ☑ ให้เอง",
    "ปุ่ม <strong>3D</strong> มุมซ้ายล่าง — เปิดหน้าต่าง 3D แท็บ Transformation",
    "<strong>Rotation: Angle = 90, Axis X = 1</strong> — หมุน 90 องศารอบแกน X แผ่นกราฟจึงตั้งขึ้นจากพื้น",
    "<strong>Position Z = 4 m</strong> — ยกกราฟขึ้นจากพื้น (X, Y = ตำแหน่งบนพื้น)",
    "<code>Apply</code> แล้ว <code>OK</code> — ดูผลในมุมมอง 3D (ขั้นที่ 5)",
])}
<div class="tip"><strong>ค่าจริงใน Model2:</strong> X = 11 m, Z = 4 m, หมุน 90 องศารอบแกน X — ค่า Y เป็นเลขเล็กมาก (เกือบ 0) เพราะเศษจากการคำนวณ</div>

<h2>ขั้นที่ 4: รัน Model 1 ชั่วโมง แล้วอ่านผล</h2>
{side_by_side(
    screenshot("assets/images/logistics/04-16.jpg", "Frame Model หลังรัน 1 ชั่วโมง"),
    step_list([
        "<strong>Production Time = 1:00:00</strong> — ครบเวลาแล้วหยุดเอง",
        "<strong>FG = 355</strong> — ชิ้นงานที่เสร็จใน 1 ชั่วโมง",
        "<strong>Chart เขียวเต็มทุกแท่ง</strong> — ทุกเครื่อง Working ~99–100%",
    ])
)}
<div class="note"><strong>ทำไมไม่ใช่ 360:</strong> Source ปล่อย 360 ชิ้น ตอนหมดเวลายังค้างอยู่ใน Station เครื่องละ 1 ชิ้น รวม 5 ชิ้น — ไลน์นี้สมดุล</div>

<h2>ขั้นที่ 5: Model2 — Station3 ช้ากว่าเพื่อน 2 เท่า</h2>
{side_by_side(
    screenshot("assets/images/logistics/04-17.jpg", "หน้าต่าง Station3 ใน Model2 แท็บ Times"),
    screenshot("assets/images/logistics/04-18.jpg", "Frame Model2 หลังรัน 1 ชั่วโมง"),
)}
{step_list([
    "<strong>Station3 Processing Time = 0:20</strong> — เครื่องอื่นยัง 0:10",
    "<strong>FG = 177</strong> — ทั้งไลน์ได้แค่ครึ่งเดียว",
])}
<div class="note"><strong>คอขวด (Bottleneck):</strong> ทั้งไลน์เดินได้เร็วเท่าเครื่องที่ช้าที่สุด 3600 ÷ 20 = 180 ชิ้น ใกล้กับ 177 ที่วัดได้</div>

<h2>ขั้นที่ 5: 3D Chart บอกว่าเครื่องไหนเป็นคอขวด</h2>
<p>Frame Model2 · มุมมอง 3D หลังรัน 1 ชั่วโมง (หมุนกล้องให้มองตรงกราฟ)</p>
{side_by_side(
    screenshot("assets/images/logistics/04-19.jpg", "3D Chart ของ Model2 หลังรัน 1 ชั่วโมง"),
    step_list([
        "<strong>Station1–2 สีเหลือง</strong> — Blocked ~50% ทำเสร็จแต่ส่งต่อไม่ได้",
        "<strong>Station3 เขียวเต็ม</strong> — Working ~99% = คอขวด",
        "<strong>Station4–5 สีเทา</strong> — Waiting ~51% รองานจากเครื่องก่อนหน้า",
        "<strong>ชื่อสถานะ</strong> — ดูสีจาก legend ด้านขวา",
    ])
)}
<div class="tip"><strong>วิธีจำ:</strong> ก่อนคอขวด = <strong>เหลือง</strong> (Blocked) · หลังคอขวด = <strong>เทา</strong> (Waiting) · คอขวด = <strong>เขียวเต็มแท่ง</strong></div>

<h2>ขั้นที่ 6: ย้าย Object ด้วยเมาส์ และปุ่มลูกศร</h2>
<p>Frame Model3 · คลิกเลือก Object แล้วลาก หรือกดปุ่มลูกศร</p>
{side_by_side(
    screenshot("assets/images/logistics/04-20.jpg", "ลาก Station32 (บน) และหลังปล่อยเมาส์ Connector ตามไปต่อเอง (ล่าง)"),
    step_list([
        "<strong>คลิกค้างที่ Station32 แล้วลาก</strong> — Connector หลุดชั่วคราวระหว่างลาก",
        "<strong>ปล่อยเมาส์</strong> — Connector ตามไปต่อที่ตำแหน่งใหม่เอง",
        "<strong>ขยับทีละนิด</strong> — คลิกเลือก Object แล้วกดปุ่มตามตารางด้านล่าง",
    ])
)}
<table>
<tr><th>ปุ่ม</th><th>ผล</th></tr>
<tr><td><code>→ ← ↑ ↓</code></td><td>ย้ายในแนว X / Y ครั้งละ 0.1 m</td></tr>
<tr><td><code>Shift</code> + ลูกศร</td><td>ย้ายในแนว X / Y ครั้งละ 1 m</td></tr>
<tr><td><code>Ctrl + ↑ ↓</code></td><td>ยกขึ้น / ลง (แกน Z) ครั้งละ 0.1 m · เพิ่ม Shift = 1 m</td></tr>
<tr><td><code>Ctrl + → ←</code></td><td>หมุนรอบแกน Z ครั้งละ 1° · เพิ่ม Shift = 45°</td></tr>
</table>
<div class="tip"><strong>ตรวจแล้ว:</strong> ทุกปุ่มลองกด Station32 ใน Plant Simulation 2606 แล้วอ่านตำแหน่งจริง ได้ค่าตามตารางนี้</div>

<h2>ขั้นที่ 6: ลบ และแทรก Object</h2>
<p>คลิกขวา › × · ลาก Object ไปปล่อยบน Connector</p>
{screenshot("assets/images/logistics/04-21.jpg", "ลบ Object ด้วยเมนูคลิกขวา และลาก Station ใหม่ไปปล่อยบน Connector")}
{step_list([
    "<strong>คลิกขวาที่ Object › ×</strong> — ลบ Object พร้อม Connector ที่ต่ออยู่",
    "<strong>วาง Station ใหม่</strong> — จาก Toolbox ในที่ว่าง ยังไม่ต่อเส้น",
    "<strong>ลาก Station ไปปล่อยบน Connector</strong> — Station5 → Drain",
    "<strong>Connector แยกเป็น 2 เส้นเอง</strong> — Station5 → Station → Drain",
])}
<div class="note"><strong>ระวัง:</strong> คลิกไอคอนใน Toolbox แล้วคลิกบน Connector ตรง ๆ จะไม่แทรก: Station ไปวางข้างเส้น และเส้นเดิมยังอยู่
ต้องวางในที่ว่างก่อน แล้วค่อยลากไปปล่อยบนเส้น</div>

<h2>ขั้นที่ 6: Model3 — เพิ่ม Station32 ขนานกับ Station3</h2>
{screenshot("assets/images/logistics/04-22.jpg", "Frame Model3 ที่มี Station32 วางขนานกับ Station3")}
{step_list([
    "<strong>Station3</strong> — 0:20 เหมือนเดิม",
    "<strong>Station32</strong> — เครื่องใหม่ 0:20 วางขนานกัน",
    "<strong>Connector 8 เส้น</strong> — Station2 ส่งไป 2 ทาง (Exit Strategy = Cyclic) แล้วรวมเข้า Station4",
    "<strong>FG = 354</strong> — กลับมาเกือบเท่าไลน์สมดุล",
])}
<div class="note"><strong>ทำไมได้ผล:</strong> 2 เครื่อง × 20 วินาที = เฉลี่ย 10 วินาทีต่อชิ้น เท่ากับเครื่องอื่นในไลน์</div>

<h2>ขั้นที่ 6: Chart หลังแก้ ทุกเครื่องทำงานเต็มที่</h2>
<p>Frame Model3 · มุมมอง 3D หลังรัน 1 ชั่วโมง</p>
{screenshot("assets/images/logistics/04-23.jpg", "3D Chart ของ Model3 หลังแก้ (ซ้าย) และตำแหน่ง Station32 ในฉาก 3D (ขวา)")}
{step_list([
    "<strong>ทุกแท่งสีเขียว</strong> — ไม่มีเครื่องถูกบล็อก หรือรองาน",
    "<strong>แท่ง Station32</strong> — เครื่องใหม่อยู่ใน Input Channels ของ Chart แล้ว",
    "<strong>Station32</strong> — วางหน้า Station3 ในฉาก 3D",
])}
<div class="tip"><strong>สรุป:</strong> แก้คอขวดได้ 177 → 354 ชิ้น/ชม. ด้วยการเพิ่มเครื่องที่จุดคอขวด — ต้องหาให้เจอก่อนว่าเครื่องไหนเป็นคอขวด (ขั้นที่ 5)</div>

<h2>สรุป 3 Frame (จำลอง 1 ชั่วโมง)</h2>
<table>
<tr><th>Frame</th><th>สิ่งที่ต่าง</th><th>Connector</th><th>FG (ชิ้น/ชม.)</th><th>เครื่องจุด Station3 ทำงาน</th></tr>
<tr><td><code>Model</code></td><td>ทุกเครื่อง 0:10</td><td>6</td><td><strong>355</strong></td><td>~99% ไลน์สมดุล</td></tr>
<tr><td><code>Model2</code></td><td>Station3 = 0:20</td><td>6</td><td><strong>177</strong></td><td>99% = คอขวด</td></tr>
<tr><td><code>Model3</code></td><td>เพิ่ม Station32 (0:20) ขนานกับ Station3</td><td>8</td><td><strong>354</strong></td><td>~99% ทั้ง 2 เครื่อง</td></tr>
</table>
<p>ทุกตัวเลขวัดจริงทั้งใน Plant Simulation 2504 และ 2606 ได้เท่ากัน</p>

<h2>ลองเอง: เปลี่ยนเวลาแล้วดู FG (Model–Model3)</h2>
<p>เดาก่อนว่า FG จะเป็นเท่าไร แล้วรันดู</p>
<table>
<tr><th>Frame</th><th>ลองเปลี่ยน</th><th>FG หลังรัน</th><th>ทำไม</th></tr>
<tr><td><code>Model</code></td><td>Station1 = 0:20</td><td><strong>177</strong></td><td>คอขวดอยู่ต้นไลน์ ผลเท่ากัน</td></tr>
<tr><td><code>Model</code></td><td>Station5 = 0:20</td><td><strong>177</strong></td><td>คอขวดอยู่ท้ายไลน์ ผลก็เท่ากัน</td></tr>
<tr><td><code>Model2</code></td><td>Station3 = 0:15</td><td><strong>237</strong></td><td>3600 ÷ 15 = 240</td></tr>
<tr><td><code>Model2</code></td><td>Station3 = 0:10</td><td><strong>355</strong></td><td>กลับเป็นไลน์สมดุลเหมือน Model</td></tr>
<tr><td><code>Model3</code></td><td>Station3 และ Station32 = 0:30</td><td><strong>236</strong></td><td>2 เครื่อง ÷ 30 วินาที = 15 วินาทีต่อชิ้น</td></tr>
</table>
<p>วัดจริงใน Plant Simulation 2504 (และ 2606 ได้เท่ากัน) แก้ทีละค่าจากค่าเดิม · กด Reset ก่อน Start ทุกครั้ง</p>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>3D Chart ว่างหลังรัน</td><td>รันด้วยปุ่ม Start แบบมีภาพเคลื่อนไหว 3D Chart จะวาดใหม่ระหว่างรัน</td></tr>
<tr><td>Planning View มองไม่เห็น 3D Chart</td><td>3D Chart ตั้งขึ้นในฉาก 3D: ปิด Planning View แล้วหมุนมุมกล้อง</td></tr>
<tr><td>Chart ไม่มีแท่งของเครื่องใหม่</td><td>ใส่เครื่องใหม่ (Station32) ใน Input Channels ของ Chart (ลากเครื่องไปปล่อยบน Chart)</td></tr>
<tr><td>เพิ่มเครื่องแล้ว FG ไม่เพิ่ม</td><td>ตรวจ Connector เข้า–ออกเครื่องใหม่ให้ครบ</td></tr>
<tr><td>เพิ่มเครื่องแล้ว FG ยังไม่เพิ่มตามคาด</td><td>คอขวดย้ายไปเครื่องอื่นแล้ว ดูสีใน Chart</td></tr>
<tr><td>กด Start แล้วผลไม่เริ่มจากศูนย์</td><td>กด Reset (ปุ่มแดง) ก่อน Start ทุกครั้ง</td></tr>
</table>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ใน Model2 ถ้าเปลี่ยนเวลาของ Station1 จาก 0:10 เป็น 0:15 (Station3 ยัง 0:20) FG จะเปลี่ยนไหม เพราะอะไร?
</div>
<div class="tip"><strong>เฉลย:</strong> ไม่เปลี่ยนมาก เพราะคอขวดยังเป็น Station3 (0:20) ซึ่งช้าที่สุดในไลน์ — ไลน์เดินได้เร็วเท่าเครื่องที่ช้าที่สุด
การทำให้เครื่องที่ไม่ใช่คอขวดช้าลงหรือเร็วขึ้นแทบไม่มีผล ต้องแก้ที่คอขวดก่อน (ขั้นที่ 6) — หลักเดียวกันใช้กับเครนของคลังอัตโนมัติในบท
<a href="simulation-02.html">2.2</a></div>
'''
