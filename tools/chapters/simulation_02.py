# -*- coding: utf-8 -*-
"""simulation 2 (practice): สร้างคลังสินค้าแรก.
User 2026-11-19: from 2504_HBW\\StepByStep\\H01_ClassLibrary.pptx (HBW_Lesson.spp frame H01_ClassLibrary) + a section on drawing
a Conveyor. HBW images 02-01..09, 02-17 = crops of the H01 slides (callouts as on the slides, no title/footer).
Conveyor images 02-10..16 = PlantSimulation site lesson 03 images (2606, from 03_Conveyor_Buffer_Failures_OEE.pptx).
Numbers re-run on 2504 2026-11-19 (copy of HBW_Lesson.spp, frame H01, 8 h): Source out 1,461 · Drain 1,425 · places 32 used / 68 free ·
Conveyor 4 m, 1 m/s · Source interval 10 s. RSU statistics (26.26 / 28.58 / 44.97 / 0.19 %) are from the deck.
User 2026-11-19: + H02-H04 (decks H02_userSetTarget / H03_RacksAndRSU / H04_WarehouseFull), images 02-18..31 cropped from their slides.
Re-run on 2504: H02 Drain 2,880 / 0 places · H03 in 1,530 out 1,425 100/100 · H04 stops 22:46.56, Source 105, Drain 0.
Trial rows (RSU 0.5 m/s, 20 columns, removal 10 s, Method) and RSU % are from the decks."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เพิ่ม Library HBW และหา Object ของคลังอัตโนมัติ (RackLane, WMS, userSetTarget) ใน Toolbox ได้",
    "วาด Conveyor ทั้งช่วงตรงและโค้ง แก้รูปทรง และตั้งความเร็วได้",
    "วางและต่อ Source → Conveyor → RackLane → Drain แล้วตั้งค่า RackLane และ WMS ได้",
    "รัน 8 ชั่วโมง อ่านสถิติของ RSU และบอกได้ว่าอะไรเป็นคอขวดของคลัง",
    "แก้ปัญหาที่พบบ่อยของคลังอัตโนมัติ: ชิ้นงานไม่ถูกเก็บ (userSetTarget) ชั้นเต็มเมื่อเร่ง RSU และโมเดลหยุดเมื่อไม่มีการนำออก",
]

TOPICS = []

BODY = f'''
<p class="lead" style="max-width:46em;">สร้างคลังสินค้าอัตโนมัติแห่งแรกด้วย <strong>Library HBW</strong> (High Bay Warehouse) ที่มากับ Plant Simulation:
ชิ้นงานวิ่งบนสายพานเข้าชั้นวาง รถยก <strong>RSU</strong> (Rack Serving Unit) เก็บเข้าช่อง แล้ว <strong>WMS</strong> สั่งนำของออก
— ต่อจากการวาง Object และต่อ Connector ในบท <a href="logistics-03.html">1.3</a></p>

<div class="tip"><strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 · Library HBW (ฟรี) · ไฟล์ <code>HBW_Lesson.spp</code> Frame <code>H01_ClassLibrary</code>
(หรือสร้างใหม่ทั้งหมดตามขั้นตอน) &nbsp;·&nbsp; ผลรัน 8 ชั่วโมง: ชิ้นงานเข้าคลัง <strong>1,461 ชิ้น</strong></div>

<h2>ภาพรวม: สร้างคลังอัตโนมัติใน 7 ขั้น</h2>
<table>
<tr><th>ขั้น</th><th>ทำอะไร</th></tr>
<tr><td>1</td><td>เพิ่ม Library HBW</td></tr>
<tr><td>2</td><td>หา Object ของ HBW ใน Toolbox</td></tr>
<tr><td>3</td><td>วาด Conveyor</td></tr>
<tr><td>4</td><td>วาง Object และต่อ Connector</td></tr>
<tr><td>5</td><td>ตั้งค่า RackLane</td></tr>
<tr><td>6</td><td>ตั้งค่า WMS</td></tr>
<tr><td>7</td><td>รัน 8 ชั่วโมง แล้วอ่านผล</td></tr>
<tr><td>H02</td><td>แบบฝึก: ชิ้นงานไม่ถูกเก็บ — สร้าง sensor เรียก userSetTarget</td></tr>
<tr><td>H03</td><td>แบบฝึก: เร่ง RSU เป็น 2 m/s — คอขวดย้ายไปที่การนำออก</td></tr>
<tr><td>H04</td><td>แบบฝึก: ปิดการนำออก — คลังเต็มแล้วโมเดลหยุด</td></tr>
</table>
<p>โมเดลของบทนี้: Source ปล่อยชิ้นงานทุก 10 วินาที → Conveyor → RackLane → Drain · WMS เก็บแบบ One by one และนำของออกทุก 20 วินาที</p>

<h2>ขั้นที่ 1: เพิ่ม Library HBW</h2>
{side_by_side(
    screenshot("assets/images/simulation/02-02.jpg", "ปุ่ม Manage Class Library ในแท็บ Home"),
    screenshot("assets/images/simulation/02-01.jpg", "หน้าต่าง Manage Class Library แท็บ Libraries")
)}
{step_list([
    "แท็บ <strong>Home</strong> คลิก <strong>Manage Class Library</strong>",
    "คลิกแท็บ <strong>Libraries</strong>",
    "ใต้ <strong>Free of Charge Example Libraries</strong> คลิกช่องหน้า <strong>HBW</strong> ให้ขึ้นเครื่องหมายถูก ☑",
    "คลิก <strong>OK</strong> — แท็บ <strong>HBW</strong> จะขึ้นใน Toolbox",
])}
<div class="note"><strong>ตัวแดง:</strong> ชื่อ Library สีแดงแปลว่าเวอร์ชันในไฟล์ (2404) เก่ากว่าที่ติดตั้ง ใช้งานได้ตามเดิม
— ถ้าเปิดไฟล์แล้วมีแถบ <em>The model contains outdated libraries</em> ไม่ต้องกด Update สำหรับบทนี้ (ถ้าจะ Update ให้สำรองไฟล์ก่อน)</div>

<h2>ขั้นที่ 2: Object ของ HBW ใน Toolbox</h2>
{screenshot("assets/images/simulation/02-03.jpg", "Toolbox แท็บ HBW")}
{step_list([
    "Toolbox แท็บ <strong>HBW</strong>",
    "<strong>WMS</strong> — ตัวจัดการคลัง: เลือกช่องเก็บ และนำของออก",
    "<strong>RackLane</strong> — ชั้นวาง 2 ด้าน + รถยก RSU + สายพานเข้า–ออก ในตัว",
    "<strong>userSetTarget</strong> — Method ที่ sensor บน Conveyor เรียก เพื่อจองช่องในคลัง",
])}
<div class="tip"><strong>ใน Class Library:</strong> อยู่ที่ <code>ApplicationObjects › HBW3D</code> · คู่มืออยู่ที่ <code>HBW_Documentation</code>
· ลากไอคอนจาก Toolbox ลงใน Frame และชี้เมาส์ค้างไว้จะขึ้นชื่อ Object</div>

<h2>ขั้นที่ 3: วาด Conveyor</h2>
<p>สายพานในคลังของบทนี้เป็นช่วงตรงยาว 4 m — หัวข้อนี้สอนวิธีวาดทั้งช่วงตรงและโค้ง แก้รูปทรง และตั้งค่า
(ภาพในหัวข้อนี้มาจาก Plant Simulation 2606 ขั้นตอนเหมือนกันใน 2504)</p>

<h3>3.1 เลือก Conveyor แล้วคลิกจุดเริ่ม</h3>
<p><code>Toolbox › Material Flow › Conveyor</code></p>
{screenshot("assets/images/simulation/02-10.jpg", "เลือก Conveyor ใน Toolbox แล้วคลิกจุดเริ่มข้าง Source")}
{step_list([
    "<strong>Conveyor</strong> — คลิกไอคอนใน Toolbox แท็บ Material Flow",
    "<strong>คลิกจุดเริ่ม</strong> — ข้าง Source ตรงที่สายพานจะรับงาน",
    "<strong>Line/Arc Parameters</strong> — หน้าต่างนี้ขึ้นมาเอง บอกความยาวระหว่างวาด",
])}
<div class="tip"><strong>ยกเลิก:</strong> คลิกขวาในพื้นที่ Frame หรือคลิกปุ่ม <code>Abort</code> ถ้าวาดผิด</div>

<h3>3.2 คลิกจุดถัดไป ดูความยาวในช่อง Line Length</h3>
<p>เลื่อนเมาส์ไปตามทิศที่ต้องการ ดูตัวเลขเมตร แล้วคลิก — ไม่ต้องพิมพ์ตัวเลข</p>
{screenshot("assets/images/simulation/02-11.jpg", "ช่อง Line Length บอกความยาวระหว่างเลื่อนเมาส์")}
{step_list([
    "<strong>Line Length = 4.000 m</strong> — ตัวเลขเปลี่ยนตามเมาส์ทันที",
    "<strong>คลิกจุดที่จะวาง</strong> — เมื่อตัวเลขได้ความยาวที่ต้องการ (สายพานของคลังในบทนี้ = 4 m แล้วคลิก Finish ได้เลย)",
])}
<div class="tip"><strong>ความยาวพอดี:</strong> จุดบนพื้นห่างกันจุดละ 1 m ช่วยให้คลิกได้ค่าลงตัว</div>

<h3>3.3 กด Ctrl ค้างแล้วคลิก ได้ทางโค้ง แล้วคลิก Finish</h3>
<p>Ctrl + คลิก = โค้ง 90° · คลิก = ตรง · Finish = จบ</p>
{screenshot("assets/images/simulation/02-12.jpg", "วาดทางโค้งด้วย Ctrl + คลิก แล้วต่อช่วงตรงและคลิก Finish")}
{step_list([
    "<strong>กด Ctrl ค้าง แล้วคลิก</strong> — ได้ทางโค้ง 90° รัศมี 2 m",
    "<strong>Curve Angle 90, Radius 2</strong> — ช่องหน้า fixed มีเครื่องหมายถูก ☑ = ใช้ค่านี้ทุกโค้ง",
    "<strong>ปล่อย Ctrl แล้วคลิก</strong> — สายพานตรงต่ออีก 1 m",
    "<strong>Finish</strong> — จบการวาด ได้ Conveyor ยาว 4 + 3.14 + 1 = 8.14 m",
])}

<h3>3.4 แก้รูปทรงสายพานหลังวาด</h3>
<p>คลิกขวาที่ Conveyor › <code>Show Manipulators</code> (M) แล้วลากจุด Anchor</p>
{screenshot("assets/images/simulation/02-13.jpg", "เมนู Show Manipulators และจุด Anchor Point บนสายพานในมุมมอง 3D")}
{step_list([
    "<strong>คลิกขวาที่ Conveyor › Show Manipulators</strong> — หรือคลิกเลือกแล้วกด <code>M</code>",
    "<strong>Anchor Point</strong> — จุดหักของสายพาน (สีเหลือง) คลิกค้างแล้วลากไปวางที่ใหม่ ช่วงตรงและโค้งยืด / หดตาม",
])}

<h3>3.5 เมนู Segments — แก้เป็นตัวเลข ต่อ กลับทิศ แยก</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-14.jpg", "คลิกขวาที่ Conveyor › Segments และเมนูย่อย"),
    step_list([
        "<strong>Segments</strong> — ชี้ที่เมนูนี้ เมนูย่อยจะเปิดทางขวา",
        "<strong>Edit... (F7)</strong> — ตาราง Segments ของทุกช่วง แก้ Length (m), มุมโค้ง และรัศมีเป็นตัวเลข แล้วคลิก OK",
        "<strong>Append...</strong> — ต่อสายพานจากปลายเดิม คลิกจุดถัดไปเหมือนตอนวาด",
        "<strong>Reverse</strong> — กลับทิศทางการไหล จุดสุดท้ายกลายเป็นจุดแรก",
        "<strong>Split Up</strong> — แยกสายพานเป็นคนละชิ้น ตรงจุดที่คลิกเลือก",
    ])
)}
<div class="tip"><strong>ตัวอย่าง:</strong> ช่วงตรงยาว 4 m อยากได้ 5 m: <code>Edit...</code> › แถวช่วงนั้น › Length = 5 › OK ช่วงที่ตามมาเลื่อนไปเอง</div>

<h3>3.6 ตั้งค่า Conveyor</h3>
<p>ดับเบิลคลิก Conveyor (ภาพซ้าย · ภาพขวาเป็นหน้าต่างของ Buffer ใช้ในบทอื่น)</p>
{screenshot("assets/images/simulation/02-15.jpg", "หน้าต่างตั้งค่า Conveyor (ซ้าย) และ Buffer (ขวา)")}
{step_list([
    "<strong>Length</strong> — มาจากที่วาด แก้ในช่องนี้ไม่ได้ (แก้ด้วย Segments)",
    "<strong>Width 1 m</strong> — ความกว้างสายพาน",
    "<strong>Speed 1 m/s</strong> — ความเร็ว (สายพานของคลังในบทนี้ 1 m/s)",
    "<strong>Capacity -1</strong> — รับได้เต็มความยาวสายพาน",
    "(ภาพขวา) Buffer Capacity — ไม่ใช้ในบทนี้",
])}
<div class="tip"><strong>เวลาบนสายพาน:</strong> ความยาว ÷ ความเร็ว — สายพาน 4 m ที่ 1 m/s ชิ้นงานใช้เวลา 4 วินาทีจาก Source ถึงหน้าคลัง</div>

<h3>3.7 เปลี่ยนรูปสายพานใน 3D เป็นแบบ Roller (ถ้าต้องการ)</h3>
<p>คลิกขวาที่ Conveyor › <code>Edit 3D Properties...</code> › แท็บ Appearance</p>
{screenshot("assets/images/simulation/02-16.jpg", "Edit 3D Properties ของ Conveyor แท็บ Appearance เลือก Roller conveyor")}
{step_list([
    "<strong>Edit 3D Properties...</strong> — หรือคลิกเลือกแล้วกด <code>Space</code>",
    "<strong>แท็บ Appearance</strong>",
    "<strong>Type = Roller conveyor</strong> — เลือกรูปแบบสายพานจากรายการ",
    "<strong>Legs</strong> — ขาตั้ง: รูปแบบ สี และขนาด",
    "<strong>Rollers · Support Frame</strong> — สีและขนาดลูกกลิ้ง และโครงข้าง",
    "<strong>Apply</strong> แล้ว <strong>OK</strong>",
])}
<div class="note"><strong>มีผลแค่หน้าตา:</strong> เปลี่ยนเฉพาะภาพ 3D ความเร็ว ความยาว และผลการรันเท่าเดิม</div>

<h2>ขั้นที่ 4: วาง Object และต่อ Connector</h2>
{side_by_side(
    screenshot("assets/images/simulation/02-04.jpg", "Frame H01 ใน 3D ก่อนรัน"),
    step_list([
        "<strong>Source</strong> — สร้างชิ้นงาน (Part) ทุก 10 วินาที",
        "<strong>Conveyor</strong> — สายพาน 4 m พาชิ้นงานเข้าคลัง (วาดตามขั้นที่ 3)",
        "<strong>RackLane</strong> — 10 คอลัมน์ × 5 ชั้น × 2 ด้าน = 100 ช่อง",
        "<strong>Drain</strong> — รับชิ้นงานที่นำออกจากคลัง",
        "<strong>WMS</strong> — วางใน Frame ไม่ต้องต่อ Connector",
        "<strong>userSetTarget</strong> — sensor บน Conveyor เรียกใช้เพื่อจองช่อง",
    ])
)}
<div class="tip"><strong>Connector:</strong> Source → Conveyor → RackLane → Drain · ภาพนี้คือ Frame ก่อนรัน ชั้นวางยังว่าง
เสาสีดำกลางชั้นคือรถยก RSU ที่วิ่งในช่องกลาง</div>
<div class="note"><strong>ต่างจาก Store:</strong> RackLane ต่อ Connector ไป Drain ได้ เพราะ WMS เป็นตัวสั่งนำของออกจากชั้นวาง
(ส่วน Store ธรรมดาต่อ Drain ไม่ได้ ต้องเขียน Method สั่ง)</div>

<h2>ขั้นที่ 5: ตั้งค่า RackLane</h2>
<p>ดับเบิลคลิก RackLane</p>
{side_by_side(
    screenshot("assets/images/simulation/02-05.jpg", "RackLane แท็บ Racks"),
    screenshot("assets/images/simulation/02-06.jpg", "RackLane แท็บ Rack Serving Unit")
)}
{step_list([
    "<strong>Number of columns 10, Number of rows 5</strong> — ต่อด้าน (2 ด้าน = 100 ช่อง)",
    "<strong>Dimension of a storage place</strong> — ขนาดช่อง 0.9 × 1.2 × 1.3 m",
    "<strong>Warehouse management system = WMS</strong> — ชื่อ WMS ที่คุมชั้นนี้",
    "แท็บ <strong>Rack Serving Unit</strong>: <strong>Speed of RSU 1 m/s</strong>",
    "<strong>Availability / MTTR</strong> — การเสียของ RSU (100 % = ไม่เสีย)",
])}
<div class="tip"><strong>แท็บ Conveyor:</strong> ตั้งสายพานเข้า–ออกในตัว RackLane (1 m/s) · บทนี้ใช้ค่าตามภาพ</div>

<h2>ขั้นที่ 6: ตั้งค่า WMS</h2>
<p>ดับเบิลคลิก WMS</p>
{side_by_side(
    screenshot("assets/images/simulation/02-07.jpg", "WMS แท็บ Strategy"),
    screenshot("assets/images/simulation/02-08.jpg", "WMS แท็บ Stock Removal")
)}
{step_list([
    "<strong>Storing strategy = One by one</strong> — เก็บเรียงช่อง (กลยุทธ์อื่นอยู่ในบท 2.7)",
    "แท็บ <strong>Stock Removal</strong>: คลิกช่อง <strong>Automatic stock removal</strong> ให้ขึ้นเครื่องหมายถูก ☑",
    "<strong>Removing starts after = 5:00</strong> — เริ่มนำออกหลัง 5 นาที",
    "<strong>Interval between removing = 20</strong> — นำออกทุก 20 วินาที",
    "<strong>Maximum Stock Removed = 1</strong> — ครั้งละ 1 ชิ้น",
])}
<div class="note"><strong>ชิ้นงานที่นำออก</strong> ออกทาง RackLane ไปที่ Drain ตาม Connector</div>

<h2>ขั้นที่ 7: รัน 8 ชั่วโมง แล้วอ่านสถิติ RSU</h2>
<p>EventController: Reset แล้ว Start (End = 8:00:00) · จบแล้วดับเบิลคลิก RackLane › แท็บ <strong>Statistics</strong></p>
{side_by_side(
    screenshot("assets/images/simulation/02-09.jpg", "Frame H01 หลังรัน 8 ชั่วโมง"),
    screenshot("assets/images/simulation/02-17.jpg", "RackLane แท็บ Statistics หลังรัน 8 ชั่วโมง")
)}
{step_list([
    "ตอนจบมีของ <strong>32 ช่อง</strong> จาก 100",
    "ชิ้นงานต่อคิวบนสายพาน รอเข้าคลัง",
    "<strong>Unloading 44.97 %</strong> — RSU ใช้เวลาเก็บของเข้าช่องมากที่สุด",
    "<strong>Waiting 0.19 %</strong> — RSU แทบไม่เคยว่าง = <strong>คอขวด</strong>",
])}

<h3>ผลลัพธ์: RSU เป็นคอขวดของคลัง</h3>
<table>
<tr><th>ค่าที่อ่าน</th><th>ผล (8 ชม.)</th><th>ความหมาย</th></tr>
<tr><td>ชิ้นงานเข้าคลัง</td><td><strong>1,461</strong> ชิ้น</td><td>Source ปล่อยได้ 2,880 ชิ้นถ้าไม่ติด (8 ชม. ÷ 10 วินาที)</td></tr>
<tr><td>ชิ้นงานออก Drain</td><td><strong>1,425</strong> ชิ้น</td><td>นำออกทุก 20 วินาที หลังนาทีที่ 5</td></tr>
<tr><td>ช่องที่มีของตอนจบ</td><td><strong>32 / 100</strong> ช่อง</td><td>Rack Space Utilization 32 % (WMS)</td></tr>
<tr><td>RSU รอ (Waiting)</td><td><strong>0.19 %</strong> ของเวลา</td><td>แทบไม่ว่าง = คอขวด</td></tr>
</table>
<div class="note"><strong>ชวนคิด:</strong> ของเข้าคลังได้ครึ่งเดียวของที่ Source ปล่อย เพราะ RSU เก็บไม่ทัน ส่วนของออกถูกกำหนดด้วยรอบการนำออก
— 3 แบบฝึกต่อไปนี้ใช้คลังเดียวกัน แก้ทีละเรื่องแล้วดูว่าผลเปลี่ยนอย่างไร</div>

<h2>แบบฝึก H02: ชิ้นงานไม่ถูกเก็บเข้าคลัง (userSetTarget)</h2>
<p>Frame <code>H02_userSetTarget</code> = คลังของ H01 ที่ลบ sensor บน Conveyor ออก บันทึกไว้ในสถานะที่มีปัญหา ให้หาสาเหตุและแก้เอง</p>

<h3>1. รัน 8 ชั่วโมง ชั้นวางยังว่าง</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-18.jpg", "Frame H02 หลังรัน 8 ชั่วโมง ชั้นวางว่าง"),
    step_list([
        "ชั้นวางไม่มีของเลย (0 ช่อง)",
        "ชิ้นงานวิ่งผ่าน RackLane ตรงไป",
        "Drain ได้ <strong>2,880 ชิ้น</strong> เท่ากับที่ Source ปล่อยทั้งหมด",
    ])
)}
<div class="note"><strong>สังเกต:</strong> ไม่มีข้อความ error โมเดลรันจนจบ 8:00:00 — H01 เก็บได้ 1,461 ชิ้น แต่ H02 ไม่เก็บเลย
ทั้งที่ RackLane และ WMS ตั้งค่าเหมือนกัน ต้องสังเกตเองว่าชั้นว่าง</div>

<h3>2. เทียบ Sensors ของ Conveyor</h3>
<p>ดับเบิลคลิก Conveyor › แท็บ <strong>Controls</strong> (ซ้าย = Frame H01 · ขวา = Frame H02)</p>
{side_by_side(
    screenshot("assets/images/simulation/02-19.jpg", "Conveyor ของ H01: Sensors (1)"),
    screenshot("assets/images/simulation/02-20.jpg", "Conveyor ของ H02: Sensors (0)")
)}
{step_list([
    "ดับเบิลคลิก Conveyor แท็บ <strong>Controls</strong>",
    "H01: <strong>Sensors (1)</strong>",
    "H02: <strong>Sensors (0)</strong> ไม่มี sensor",
])}
<div class="tip"><strong>สาเหตุ:</strong> ไม่มี sensor = ไม่มีใครเรียก <code>userSetTarget</code> ชิ้นงานจึงไม่ได้จองช่องในคลัง</div>

<h3>3. userSetTarget ทำอะไร</h3>
{screenshot("assets/images/simulation/02-21.jpg", "โค้ดของ Method userSetTarget")}
{step_list([
    "<code>WMS.placeIntoStock(@)</code> — ขอให้ WMS หาช่องว่างและจองให้ชิ้นงาน",
    "ได้ช่อง → <code>@.stopped := false</code> ชิ้นงานวิ่งต่อเข้าคลัง",
    "คลังเต็ม → <code>@.stopped := true</code> หยุดชิ้นงานบนสายพาน",
    "<code>waituntil</code> — รอจนมีช่องว่างเพิ่ม แล้วถามใหม่",
])}
<div class="note"><strong>ไม่ต้องเขียนเอง:</strong> Method นี้มากับ Library HBW (Toolbox แท็บ HBW) แค่ให้ sensor เรียกใช้</div>

<h3>4. สร้าง sensor ที่ 2 m เรียก userSetTarget</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-22.jpg", "Sensor List ของ Conveyor"),
    screenshot("assets/images/simulation/02-23.jpg", "หน้าต่างตั้งค่า Sensor")
)}
{step_list([
    "คลิก <strong>Sensors (0)</strong> แล้วคลิก <strong>New...</strong>",
    "Position: <strong>Length 2 m</strong>",
    "คลิกช่อง <strong>Front</strong> ให้ขึ้นเครื่องหมายถูก ☑",
    "Control: คลิกปุ่ม <strong>...</strong> แล้วเลือก <strong>userSetTarget</strong>",
    "คลิก <strong>OK</strong> — รายการใน Sensor List จะเป็นแบบภาพซ้าย",
])}
<div class="tip"><strong>ทางลัด:</strong> คลิกขวาบน Conveyor ในหน้าต่าง 3D › <code>Create Sensor</code></div>

<h3>5. รันใหม่ แล้วเทียบผล (8 ชม.)</h3>
<table>
<tr><th>ค่า</th><th>ไม่มี sensor</th><th>มี sensor</th></tr>
<tr><td>ชิ้นงานเข้าคลัง</td><td>0</td><td><strong>1,461</strong></td></tr>
<tr><td>ชิ้นงานออก Drain</td><td>2,880 (ทั้งหมด)</td><td><strong>1,425</strong> (WMS นำออก)</td></tr>
<tr><td>ช่องที่มีของตอนจบ</td><td>0 / 100</td><td><strong>32 / 100</strong></td></tr>
</table>
<p>มี sensor แล้วผลเท่ากับ H01</p>

<h2>แบบฝึก H03: เร่ง RSU เป็น 2 m/s</h2>
<p>Frame <code>H03_RacksAndRSU</code> = H01 ที่ตั้ง Speed of RSU = 2 m/s ค่าอื่นเหมือนเดิม (นำออกทุก 20 วินาที)
— <strong>คำถามนำ:</strong> ถ้า RSU เป็นคอขวด เร่ง RSU แล้วของออกจากคลังจะเพิ่มไหม?</p>

<h3>1. ตั้ง Speed of RSU = 2 m/s</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-24.jpg", "RackLane แท็บ Rack Serving Unit: Speed of RSU 2 m/s"),
    step_list([
        "ดับเบิลคลิก RackLane แท็บ <strong>Rack Serving Unit</strong>",
        "<strong>Speed of RSU</strong> 1 → <strong>2 m/s</strong> แล้วคลิก OK",
    ])
)}
<div class="tip"><strong>SimTalk:</strong> ช่องนี้คือตัวแปร <code>RackLane.RSU_speed</code> · Speed of load handler คือความเร็วงายก บทนี้แก้เฉพาะ Speed of RSU</div>

<h3>2. รัน 8 ชั่วโมง ชั้นเต็ม 100 ช่อง</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-25.jpg", "Frame H03 หลังรัน 8 ชั่วโมง ชั้นเต็ม"),
    screenshot("assets/images/simulation/02-26.jpg", "WMS แท็บ Statistics: Rack Space Utilization 100 %")
)}
{step_list([
    "ทุกช่องมีของ (<strong>100 / 100</strong>)",
    "ชิ้นงานต่อคิวบนสายพาน รอช่องว่าง",
    "WMS แท็บ Statistics: <strong>Rack Space Utilization 100 %</strong>",
])}
<p>RSU เก็บของได้เร็วขึ้น แต่ WMS ยังนำออกทุก 20 วินาทีเท่าเดิม ของจึงสะสมจนเต็ม</p>

<h3>3. เทียบสถิติ RSU กับ H01</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-27.jpg", "สถิติ RSU ของ H01 (1 m/s)"),
    screenshot("assets/images/simulation/02-28.jpg", "สถิติ RSU ของ H03 (2 m/s)")
)}
{step_list([
    "H01 (1 m/s): <strong>Waiting 0.19 %</strong> — RSU ไม่เคยว่าง",
    "H03 (2 m/s): <strong>Waiting 17.36 %</strong> — RSU มีเวลาว่าง",
])}
<div class="note"><strong>สรุป:</strong> RSU ไม่ใช่คอขวดแล้ว คอขวดย้ายไปที่การนำออก (ทุก 20 วินาที)</div>

<h3>4. เทียบความเร็ว RSU และจำนวนคอลัมน์ (8 ชม.)</h3>
<table>
<tr><th>ค่าที่ลอง</th><th>เข้าคลัง</th><th>ออก Drain</th><th>ช่องที่มีของ</th></tr>
<tr><td>RSU 0.5 m/s</td><td>1,437</td><td>1,419</td><td>14 / 100</td></tr>
<tr><td>RSU 1 m/s (H01)</td><td>1,461</td><td>1,425</td><td>32 / 100</td></tr>
<tr><td>RSU 2 m/s (H03)</td><td>1,530</td><td>1,425</td><td>100 / 100 (เต็ม)</td></tr>
<tr><td>RSU 1 m/s, 20 คอลัมน์</td><td>1,461</td><td>1,425</td><td>32 / 200</td></tr>
</table>
<p>ของออกเท่าเดิมทุกแบบ เพราะ WMS นำออกทุก 20 วินาที · เพิ่มคอลัมน์ไม่ช่วย เพราะ RSU คันเดียวยังวิ่งเท่าเดิม
(20 คอลัมน์ตั้งที่แท็บ Racks › Number of columns)</p>

<h2>แบบฝึก H04: ปิดการนำออก คลังเต็มแล้วโมเดลหยุด</h2>
<p>Frame <code>H04_WarehouseFull</code> = H01 ที่ไม่ได้เลือก Automatic stock removal ค่าอื่นเหมือนเดิม
— <strong>คำถามนำ:</strong> ถ้าไม่มีใครเอาของออก คลัง 100 ช่องจะเต็มเมื่อไร แล้วโมเดลจะทำอย่างไร?</p>

<h3>1. ปิด Automatic stock removal</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-29.jpg", "WMS แท็บ Stock Removal ไม่ได้เลือก Automatic stock removal"),
    step_list([
        "ดับเบิลคลิก WMS แท็บ <strong>Stock Removal</strong> แล้วคลิกช่อง <strong>Automatic stock removal</strong> ให้เครื่องหมายถูกหายไป ☐",
        "ช่องตั้งเวลาด้านล่างจะเป็นสีเทา ใช้ไม่ได้",
    ])
)}
<div class="tip"><strong>SimTalk:</strong> <code>WMS.activateAutoRemove := false</code> — WMS จะไม่เอาของออกเองเลย
ของออกได้ทางเดียวคือสั่งด้วย Method (บท <a href="simulation-03.html">2.3</a>)</div>

<h3>2. รัน แล้วโมเดลหยุดที่ 22:47</h3>
{side_by_side(
    screenshot("assets/images/simulation/02-30.jpg", "Frame H04 เมื่อโมเดลหยุด ชั้นเต็ม"),
    screenshot("assets/images/simulation/02-31.jpg", "เวลาจำลองหยุดที่ 22:46.56")
)}
{step_list([
    "ชั้นเต็ม <strong>100 / 100</strong> ช่อง",
    "สายพานเต็ม Source ปล่อยชิ้นงานต่อไม่ได้",
    "เวลาหยุดที่ <strong>22:46.56</strong> ไม่ถึง 8 ชั่วโมง",
])}
<div class="note"><strong>ไม่มีข้อความ error:</strong> เวลาหยุดเดินเอง สังเกตที่มุมขวาล่างของหน้าต่าง</div>

<h3>3. ทำไมโมเดลหยุด</h3>
<table>
<tr><th>ค่าที่อ่าน</th><th>ผล</th><th>ความหมาย</th></tr>
<tr><td>Source ปล่อยชิ้นงาน</td><td>105 ชิ้น</td><td>100 ในชั้น + 5 บนสายพาน</td></tr>
<tr><td>ช่องว่างใน WMS</td><td>0 ช่อง</td><td>ไม่มีที่เก็บ <code>userSetTarget</code> หยุดชิ้นงาน</td></tr>
<tr><td>ชิ้นงานออก Drain</td><td>0 ชิ้น</td><td>ไม่มีการนำออก</td></tr>
<tr><td>RSU Unloading</td><td>0 %</td><td>RSU ไม่เคยนำของออก</td></tr>
</table>
<p>ทุก Object รอกันหมด ไม่มีเหตุการณ์ (Event) เหลือ Plant Simulation จึงจบการรันก่อนเวลา End</p>

<h3>4. วิธีแก้ (รัน 8 ชม.)</h3>
<table>
<tr><th>วิธีแก้</th><th>ผล</th></tr>
<tr><td>เลือก Automatic stock removal (ทุก 20 วินาที)</td><td>รันครบ 8 ชม. เข้า 1,461 ออก 1,425 (= H01)</td></tr>
<tr><td>นำออกถี่ขึ้น ทุก 10 วินาที</td><td>เข้า 2,263 ออก 2,249</td></tr>
<tr><td>นำออกตามคำสั่งซื้อด้วย Method</td><td>เข้า 796 ออก 693 (บท <a href="simulation-03.html">2.3</a>)</td></tr>
</table>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>ไม่มีแท็บ HBW ใน Toolbox</td><td>Manage Class Library › Libraries › คลิกช่อง HBW ให้ขึ้น ☑ (ขั้นที่ 1)</td></tr>
<tr><td>ชิ้นงานวิ่งผ่านคลังไป Drain ไม่ถูกเก็บ</td><td>Conveyor แท็บ Controls ต้องเป็น Sensors (1) และ Control ของ sensor = <code>userSetTarget</code> (แบบฝึก H02)</td></tr>
<tr><td>ไม่มี userSetTarget ใน Frame</td><td>ลากจาก Toolbox แท็บ HBW ลงใน Frame</td></tr>
<tr><td>ชั้นเต็ม สายพานต่อคิวยาว</td><td>คอขวดอยู่ที่การนำออก: ลดค่า Interval between removing ใน WMS (แบบฝึก H03)</td></tr>
<tr><td>เวลาหยุดก่อน End ไม่มี error</td><td>WMS แท็บ Statistics: Rack Space Utilization 100 % = คลังเต็ม · ตรวจ Automatic stock removal (แบบฝึก H04)</td></tr>
<tr><td>ตั้ง NumberOfColumns ด้วย SimTalk แล้วชั้นไม่ขยาย</td><td>เรียก <code>RackLane.InitRackLane</code> หลังตั้งค่า</td></tr>
<tr><td>วาด Conveyor ผิด</td><td>ระหว่างวาด: คลิกขวาหรือ Abort · วาดแล้ว: Show Manipulators หรือ Segments › Edit</td></tr>
<tr><td>แถบ The model contains outdated libraries</td><td>ใช้ได้ตามเดิม ถ้าจะ Update ให้สำรองไฟล์ก่อน</td></tr>
</table>
'''
