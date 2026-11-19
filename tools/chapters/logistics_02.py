# -*- coding: utf-8 -*-
"""logistics 2 (practice): Factory 51 -- ระบบสารสนเทศ อุปกรณ์เคลื่อนย้าย และการขนส่ง.
User 2026-11-18: this chapter uses the Siemens example model Factory 51 (2504: Examples\\3D\\Factory51.spp)
instead of the case company's finished warehouse model.
Screens: captured by Claude 2026-11-18 on Plant Simulation 2504 (full licence, copy of the example, never saved),
annotated into assets/images/logistics/02-01..18. Mouse controls tested on 2504: wheel = zoom, right-drag = pan,
wheel-drag or Ctrl+right-drag = rotate, V = View All. Values: run 20 min / 1 h from reset (EventController End = 0 in the file).
Not verified on 2504: the Student-licence prompt for > 80 objects (described as on the 2606 site)."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิดโมเดลตัวอย่าง Factory 51 ใน Plant Simulation 2504 และควบคุมมุมมอง 3D ได้",
    "ชี้ได้ว่าอุปกรณ์เคลื่อนย้ายแต่ละแบบในโรงงาน (รถบรรทุก เครน รถยก AGV สายพาน AS/RS) ทำหน้าที่อะไรในการรับ–เก็บ–ส่งของ",
    "อ่านข้อมูลแบบระบบสารสนเทศ (WMS ของคลัง HBW) และเชื่อมการขนส่งกับกิจกรรมคลังจากผลการรันได้",
]

TOPICS = []

BODY = f'''
<p class="lead" style="max-width:46em;">บทนี้ยังไม่ต้องสร้างอะไรเอง — เปิดโรงงานตัวอย่าง <strong>Factory 51</strong> ที่มากับโปรแกรม
แล้วเดินชมทั้งระบบตั้งแต่รถบรรทุกส่งของเข้า เก็บ ผลิต จนถึงคลังอัตโนมัติและรถส่งของออก เพื่อเห็นของจริงของเรื่องที่เรียนในบท
<a href="logistics-01.html">1.1</a>: อุปกรณ์เคลื่อนย้าย ระบบสารสนเทศ (WMS) และการขนส่งกับกิจกรรมคลัง</p>

<div class="tip"><strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 (ติดตั้งตามบท <a href="start-01.html">0.1</a>)
— ไฟล์ <code>Factory51.spp</code> มากับโปรแกรมอยู่แล้วในโฟลเดอร์ <code>Examples\\3D</code> ของโฟลเดอร์ติดตั้ง ไม่ต้องดาวน์โหลดเพิ่ม</div>

<div class="note"><strong>Student License:</strong> Factory 51 มี Object มากกว่า 80 ตัว จึงเปิดได้แบบ <strong>Viewer</strong>
คือดูและรันได้ แต่บันทึกการแก้ไขไม่ได้ — พอสำหรับบทนี้ ถ้าโปรแกรมถามตอนเปิดไฟล์ ให้ตอบ <strong>Yes</strong></div>

<h2>ภาพรวม</h2>
<table>
<tr><th>ขั้น</th><th>ทำอะไร</th><th>เชื่อมกับเนื้อหา</th></tr>
<tr><td>1</td><td>เปิด Factory 51 จาก Example Models</td><td>—</td></tr>
<tr><td>2</td><td>ซูม เลื่อน หมุนมุมมอง 3D</td><td>—</td></tr>
<tr><td>3</td><td>เดินชม 5 โซน</td><td>อุปกรณ์เคลื่อนย้าย · การขนส่งกับกิจกรรมคลัง</td></tr>
<tr><td>4</td><td>เปิด Frame ด้านใน: โรงผลิต P1 และคลัง HBW</td><td>AS/RS</td></tr>
<tr><td>5</td><td>อ่านข้อมูลของ WMS</td><td>ระบบสารสนเทศคลังสินค้า</td></tr>
<tr><td>6</td><td>รัน 1 ชั่วโมง แล้วกรอกตารางผล</td><td>การขนส่ง · KPI</td></tr>
</table>

<h2>ขั้นที่ 1: เปิด Factory 51</h2>
{side_by_side(
    screenshot("assets/images/logistics/02-01.jpg", "Start Page ของ Plant Simulation 2504 และปุ่ม Example Models"),
    step_list([
        "เปิด Plant Simulation 2504 — หน้าแรกคือ <strong>Start Page</strong>",
        "ในกลุ่ม <strong>Getting Started</strong> คลิก <strong>Example Models</strong>",
    ])
)}
{side_by_side(
    screenshot("assets/images/logistics/02-02.jpg", "หน้าต่าง Example Models ของ Plant Simulation 2504"),
    step_list([
        "หน้าต่าง <strong>Example Models</strong> แสดงโมเดลตัวอย่าง 7 รายการ — คลิก <strong>Factory 51</strong>",
        "ถ้าปิด Start Page ไปแล้ว เปิดไฟล์เองได้: <code>File → Open</code> แล้วเลือก <code>Examples\\3D\\Factory51.spp</code> ในโฟลเดอร์ติดตั้ง",
    ])
)}
{screenshot("assets/images/logistics/02-03.jpg", "Factory 51 ที่เปิดแล้วในหน้าต่าง 3D")}
{step_list([
    "Class Library → <strong>Models → Factory51</strong> คือโมเดลที่เปิดอยู่",
    "แท็บ <code>3D.Models.Factory51</code> — โมเดลเปิดในหน้าต่าง 3D ทันที",
    "ปุ่มในฉาก <strong>Start/Stop Simulation</strong> และ <strong>Reset Simulation</strong>",
    "นาฬิกา <strong>EventController</strong> — ใช้ในขั้นที่ 6",
    "ตัวนับ <strong>TrucksArrived</strong> / <strong>TrucksMissed</strong> — รถบรรทุกที่เข้ามาแล้ว / ที่พลาดคิว",
])}

<h2>ขั้นที่ 2: ควบคุมมุมมอง 3D</h2>
<table>
<tr><th>เมาส์ / ปุ่ม (ทดสอบบน 2504)</th><th>ผล</th></tr>
<tr><td>หมุนล้อเมาส์</td><td>ซูมเข้า–ออก</td></tr>
<tr><td>คลิกขวาค้างแล้วลาก</td><td>เลื่อนฉาก (Pan)</td></tr>
<tr><td>กดล้อเมาส์ค้างแล้วลาก หรือ <code>Ctrl</code> + คลิกขวาค้างแล้วลาก</td><td>หมุนฉาก</td></tr>
<tr><td>กด <code>V</code></td><td>View All — เห็นทั้งโรงงาน</td></tr>
</table>
{screenshot("assets/images/logistics/02-04.jpg", "กด V เพื่อดูทั้งโรงงาน", caption="กด V แล้วเห็นทั้งโรงงานในภาพเดียว")}
<div class="note"><strong>ต่างจาก 2606:</strong> ใน 2504 การกดล้อเมาส์ค้างแล้วลากคือ<strong>หมุน</strong> (ใน 2606 คือเลื่อน)
— ถ้าดูคู่มือหรือวิดีโอของเวอร์ชันอื่น ให้ลองกับโปรแกรมของตัวเองก่อน</div>

<h2>ขั้นที่ 3: เดินชม 5 โซน</h2>
<p>ซูมและเลื่อนไปดูทีละโซนตามลำดับการไหลของของ: รับของ → ผลิต → ขนส่งภายใน → คลังอัตโนมัติ → ส่งของ
(ภาพทั้งหมดถ่ายที่เวลาจำลอง 20 นาที)</p>

<h3>3.1 รับของ (Inbound)</h3>
{screenshot("assets/images/logistics/02-05.jpg", "โซนรับของของ Factory 51")}
{step_list([
    "<strong>รถบรรทุก</strong> วิ่งเข้าตามถนน (<code>SupplyRoad</code>) — การขนส่งขาเข้า",
    "<strong>เครนขนาดเล็ก</strong> (<code>SmallCrane</code>) จัดการกองพาเลทเปล่า",
    "<strong>สายพาน + หุ่นยนต์หยิบวาง</strong> ส่งพาเลทเข้าโรงผลิต",
    "<strong>เครนแบบพอร์ทัล</strong> (<code>MultiPortalCrane</code>) เก็บพาเลทในพื้นที่จัดเก็บ (<code>StorageArea</code>)",
    "<strong>รถยกพาเลท</strong> ขนของจากรถบรรทุกเข้าพื้นที่พัก (สร้างด้วย <code>AGVPool</code> และ Method <code>UnloadTruck</code>)",
])}

<h3>3.2 ผลิต (P1 / P2)</h3>
{screenshot("assets/images/logistics/02-06.jpg", "โรงผลิต P1 และ P2",
            caption="โรงผลิต P1 (หน้า) และ P2 (หลัง): สายพานพาชิ้นงานผ่านบูธพ่นสี อบ ตรวจคุณภาพ และแพ็ก โดยมีพนักงาน (WorkerPool) ทำงานที่จุดต่าง ๆ")}

<h3>3.3 ขนส่งภายในด้วย AGV</h3>
{screenshot("assets/images/logistics/02-07.jpg", "AGV วิ่งตามเส้นทางสีเหลือง")}
{step_list([
    "<strong>AGV</strong> ขนของระหว่างโรงผลิตกับคลัง",
    "<strong>เส้นทางสีเหลือง</strong> — AGV วิ่งตามเส้นทางที่กำหนด (ตรงกับลักษณะ AGV ในบท 1.1) และมีจุดชาร์จแบตเตอรี่ระหว่างทาง",
])}

<h3>3.4 คลังอัตโนมัติ (HBW / AS/RS)</h3>
{screenshot("assets/images/logistics/02-08.jpg", "คลังอัตโนมัติ HBW")}
{step_list([
    "<strong>ชั้นวางสูงพร้อมเครน</strong> — คลังอัตโนมัติสร้างด้วย Library HBW (ดูในขั้นที่ 4)",
    "<strong>สายพานขาออก</strong> พาพาเลทจากคลังไปท่าส่งของ",
    "ตัวนับ <strong>Palettes Shipped</strong> — จำนวนพาเลทที่ส่งออกแล้ว",
])}

<h3>3.5 ส่งของ (Outbound)</h3>
{screenshot("assets/images/logistics/02-09.jpg", "ท่าส่งของและรถบรรทุกขาออก")}
{step_list([
    "<strong>สายพานแยก 3 ท่า</strong> ส่งพาเลทถึงท้ายรถ",
    "<strong>รถบรรทุกขาออก</strong> รอรับของที่ท่า — การขนส่งขาออก",
    "ตัวนับ <strong>Palettes Shipped</strong>",
])}

<div class="tip"><strong>เทียบกับบท 1.1:</strong> ในโรงงานเดียวมีอุปกรณ์เคลื่อนย้ายครบเกือบทุกแบบในตาราง — รถบรรทุก เครน รถยก
สายพาน หุ่นยนต์หยิบวาง AGV และ AS/RS — ลองบอกว่าแต่ละแบบถูกเลือกใช้ตรงนั้นเพราะอะไร</div>

<h2>ขั้นที่ 4: เปิด Frame ด้านใน</h2>
<p>อาคารบางหลังเป็น <strong>Frame</strong> ซ้อนอยู่ข้างใน (โมเดลย่อย) — เปิดดูข้างในได้</p>
{screenshot("assets/images/logistics/02-16.jpg", "คลิกขวาที่อาคารเพื่อเปิดเมนู")}
{step_list([
    "<strong>คลิกขวา</strong>ที่อาคาร — ด้านบนเมนูมีแถบปุ่ม Quick tools (Start / Stop / Reset ฯลฯ)",
    "<strong>Open</strong> (<code>Enter</code>) — เปิด Frame ของอาคารนั้น",
    "<strong>Show Statistics Report</strong> (<code>F6</code>) — ดูสถิติของ Object ที่เลือก",
])}
{side_by_side(
    screenshot("assets/images/logistics/02-10.jpg", "Frame P1 ที่เปิดแล้ว"),
    screenshot("assets/images/logistics/02-11.jpg", "Frame Warehouse (คลัง HBW) ที่เปิดแล้ว")
)}
{step_list([
    "Frame ที่เปิดจะเป็นแท็บใหม่ด้านล่าง เช่น <code>3D.Models.Factory51.P1</code> — คลิกแท็บ <code>3D.Models.Factory51</code> เพื่อกลับ",
    "เปิด Frame <strong>Warehouse</strong> จะเห็นชั้นวาง (RackLane) 5 แถวของคลัง HBW",
])}

<h2>ขั้นที่ 5: อ่านข้อมูลของ WMS</h2>
<p>คลัง HBW มี Frame <strong>WMS</strong> (Warehouse Management System) อยู่ใน Warehouse — ทำหน้าที่แบบเดียวกับ WMS จริง:
รู้ว่ามีของอะไร อยู่ที่ไหน และเลือกช่องเก็บ</p>
{screenshot("assets/images/logistics/02-12.jpg", "Frame WMS ภายในคลัง HBW")}
{step_list([
    "<strong>Storage Strategy</strong> — วิธีเลือกช่องเก็บ: OneByOne · Random · Predefined · XYZ (โซนตามสินค้า)",
    "<strong>NumFreePlaces / NumOccupiedPlaces</strong> — ช่องว่าง / ช่องที่มีของ (ที่ 20 นาที: ว่าง 373 · มีของ 127 จาก 500 ช่อง)",
    "ตาราง <strong>Inventory</strong> — สินค้าในคลังแยกตามรหัส",
    "<strong>Dialog</strong> — หน้าต่างตั้งค่า WMS",
])}
{side_by_side(
    screenshot("assets/images/logistics/02-13.jpg", "ตาราง Inventory ของ WMS", caption="ตาราง Inventory: รหัสสินค้า (Product) และตารางพาเลทของแต่ละรหัส"),
    screenshot("assets/images/logistics/02-14.jpg", "หน้าต่าง WMS แท็บ Strategy", caption="ดับเบิลคลิก Dialog → Show Dialog: แท็บ Strategy เลือกกลยุทธ์จัดเก็บ (1)")
)}
{screenshot("assets/images/logistics/02-15.jpg", "หน้าต่าง WMS แท็บ Statistics หลังรัน 1 ชั่วโมง",
            caption="แท็บ Statistics หลังรัน 1 ชั่วโมง: เครนรอ (Waiting) 91 % (1) · ใช้พื้นที่ชั้นวาง 28 % (2)")}
<div class="note"><strong>ข้อคิด:</strong> เครนของคลังอัตโนมัติว่างเกือบตลอดเวลา และชั้นวางใช้ไปไม่ถึงหนึ่งในสาม — แบบเดียวกับกรณี
"เครนทำงานแค่ประมาณ 12 %" ในบท <a href="simulation-05.html">2.5</a>: ระบบอัตโนมัติที่ใหญ่เกินงาน ต้องดูตัวเลขก่อนตัดสินใจลงทุน</div>

<h2>ขั้นที่ 6: รัน 1 ชั่วโมง แล้วกรอกตารางผล</h2>
{side_by_side(
    screenshot("assets/images/logistics/02-17.jpg", "หน้าต่าง EventController"),
    step_list([
        "<strong>Time</strong> — เวลาจำลองตอนนี้",
        "<strong>Reset</strong> — เวลากลับไป 0",
        "<strong>Start</strong> — เริ่มรัน (ปุ่มถัดไปคือรันเร็วโดยไม่แสดงภาพ)",
        "แถบ <strong>Slower / Faster</strong> — ปรับความเร็วภาพเคลื่อนไหว",
        "<strong>Real-time ×</strong> — เร็วกว่าเวลาจริงกี่เท่า",
    ])
)}
{step_list([
    "ดับเบิลคลิกนาฬิกา EventController ในฉาก แล้วคลิก <strong>Reset</strong>",
    "แท็บ <strong>Settings</strong> ตั้งเวลาจบ (End) เป็น <code>1:00:00</code> — ในไฟล์ตัวอย่างไม่ได้ตั้งเวลาจบไว้ จะรันไปเรื่อย ๆ",
    "คลิก <strong>Start</strong> ดูรถ เครน และ AGV ทำงาน แล้วปรับ <strong>Faster</strong> ให้ถึง 1 ชั่วโมงเร็วขึ้น",
    "เมื่อหยุดที่ 1:00:00 อ่านค่าแล้วกรอกตาราง",
])}
<table>
<tr><th>ค่าที่อ่าน</th><th>อ่านจากไหน</th><th>ผลที่วัดบน 2504 (1 ชั่วโมง)</th></tr>
<tr><td>รถบรรทุกเข้ามา / พลาดคิว</td><td>ตัวนับ TrucksArrived / TrucksMissed</td><td>6 / 0 คัน</td></tr>
<tr><td>ช่องในคลังที่มีของ / ว่าง</td><td>WMS: NumOccupiedPlaces / NumFreePlaces</td><td>140 / 360 ช่อง</td></tr>
<tr><td>สัดส่วนเวลาที่เครนรอ</td><td>WMS → Dialog → Statistics: Waiting</td><td>91 %</td></tr>
</table>

<div class="tip"><strong>คำถามท้ายบท:</strong>
(1) รถบรรทุก 6 คันต่อชั่วโมงเข้ามาแล้วไม่มีคันไหนพลาดคิว — ถ้ารถมาถี่ขึ้นเป็นสองเท่า ควรดูค่าไหนก่อน?
(2) ถ้าเครนรอ 91 % ของเวลา ควรลงทุนเครนเพิ่มหรือไม่ เพราะอะไร?
(3) WMS ช่วยตอบคำถาม "อะไร อยู่ที่ไหน เท่าไร" ได้จากตารางไหน?</div>

<h2>แบบฝึก: หา Beer room ใน Factory 51</h2>
<p>ฝึกซูม เลื่อน และหมุนให้คล่อง — ในโรงผลิตมีห้องเล็ก ๆ ซ่อนอยู่ ลองหาเองก่อนแล้วค่อยดูเฉลย</p>
<details>
<summary>ดูเฉลย</summary>
{screenshot("assets/images/logistics/02-18.jpg", "ประตู Beer ข้างห้อง Bathroom ในโรงผลิต P1",
            caption="ซูมเข้าโรงผลิต P1 ใต้ชั้นลอย — ประตู Beer (1) อยู่ข้างห้อง Bathroom")}
</details>
'''
