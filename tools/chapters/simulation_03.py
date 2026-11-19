# -*- coding: utf-8 -*-
"""simulation 3 (practice): ป้อนข้อมูลสินค้าเข้า – ออก, Method และการแสดงข้อมูลสินค้าคงคลัง.
User 2026-11-19: old chapters 2.3 + 2.4 merged; content = HBW H05-H12 (2504_HBW\\StepByStep\\H05..H12_*.pptx, HBW_Lesson.spp frames
H05..H12). Images 03-01..27 auto-cropped from the slides (picture + the callouts whose connector touches it; autocrop.py in scratchpad).
Re-run on 2504 2026-11-19 (copy of HBW_Lesson.spp, 8 h): H05 2,263 / 2,249 / 9 · H06 972 / 874 / 96 · H07 873 / 805 / 66 ·
H08 576 + 576 / 994 / 155 of 200 · H09 (One by one) 977 / 879 / 96 · H10 1,411 / 1,425 / 32, at 1 s 50 / 50 · H11 796 / 693 / 100 ·
H12 1,313 / 1,288 = the decks. Trial rows (other intervals, strategies in H09) and RSU % are from the decks."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ป้อนข้อมูลสินค้าออกด้วยรอบการนำออกของ WMS และข้อมูลสินค้าเข้าหลายชนิดด้วย Source ได้",
    "เลือกกลยุทธ์จัดเก็บ (One by one, Random, XYZ ranges, Predefined racks) และเทียบผลอย่างยุติธรรมได้",
    "ใช้ Method เติมสต็อกตั้งต้น (Init) นำของออกตามคำสั่งซื้อ (OrderControl) และเก็บสถิติเมื่อรันจบ (EndSim) ได้",
    "อ่านข้อมูลสินค้าคงคลังจาก WMS (ช่องว่าง / มีของ, Rack Space Utilization) และสถิติของ RSU ได้",
]

TOPICS = []

BODY = f'''
<p class="lead" style="max-width:46em;">ต่อจากคลังอัตโนมัติในบท <a href="simulation-02.html">2.2</a> — บทนี้ใช้คลังเดิม (Library HBW)
แล้วเพิ่มทีละเรื่อง: <strong>ข้อมูลสินค้าออก</strong> (รอบการนำออก) · <strong>ข้อมูลสินค้าเข้า</strong> (สินค้า 2 ชนิด) ·
<strong>กลยุทธ์จัดเก็บ</strong> · <strong>Method</strong> (สต็อกตั้งต้น และนำออกตามคำสั่งซื้อ) · <strong>สถิติ</strong></p>

<div class="tip"><strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 · Library HBW · ไฟล์ <code>HBW_Lesson.spp</code> Frame H05–H12
(1 Frame ต่อ 1 หัวข้อ) · ทุกตัวเลขในบทนี้มาจากการรัน 8 ชั่วโมง</div>

<h2>ภาพรวม: 8 แบบฝึก</h2>
<table>
<tr><th>ส่วน</th><th>Frame</th><th>เรื่อง</th><th>ผลหลัก (8 ชม.)</th></tr>
<tr><td rowspan="1">ข้อมูลสินค้าออก</td><td>H05</td><td>รอบการนำออก</td><td>นำออกทุก 10 วินาที เข้าคลัง 2,263 ชิ้น</td></tr>
<tr><td>ข้อมูลสินค้าเข้า</td><td>H06</td><td>สินค้า 2 ชนิด เก็บแบบ Random</td><td>เข้า 972 ใช้ 96 ช่อง</td></tr>
<tr><td rowspan="3">กลยุทธ์จัดเก็บ</td><td>H07</td><td>แบ่งโซนคอลัมน์ (XYZ ranges)</td><td>เข้า 873 ใช้ 66 ช่อง</td></tr>
<tr><td>H08</td><td>แยกชั้นตามสินค้า (Predefined racks)</td><td>เข้า 1,152 ใช้ 155 / 200 ช่อง</td></tr>
<tr><td>H09</td><td>เทียบกลยุทธ์ให้ยุติธรรม</td><td>XYZ เข้าน้อยกว่า One by one 11 %</td></tr>
<tr><td rowspan="2">Method</td><td>H10</td><td>เติมของก่อนรัน (Init)</td><td>มีของ 50 ช่องตั้งแต่เริ่ม</td></tr>
<tr><td>H11</td><td>นำออกตามคำสั่งซื้อ (OrderControl)</td><td>นำออก 693 ชิ้น</td></tr>
<tr><td>สถิติ</td><td>H12</td><td>RSU เสีย และเก็บสถิติลงตาราง (EndSim)</td><td>เข้าคลังน้อยลง 10 %</td></tr>
</table>

<h2>1. ข้อมูลสินค้าออก — H05 รอบการนำออก</h2>
<p>Frame <code>H05_StockRemoval</code> = H01 ที่นำออกทุก 10 วินาที (เดิม 20) ค่าอื่นเหมือนเดิม · Source ปล่อยชิ้นงานทุก 10 วินาที
— ถ้านำออกทุก 10 วินาทีเท่ากัน ของเข้าและออกจะเกือบเท่ากัน</p>

<h3>1.1 ตั้ง Interval between removing = 10</h3>
{side_by_side(
    screenshot("assets/images/simulation/03-01.jpg", "WMS แท็บ Stock Removal: Interval between removing 10"),
    step_list([
        "WMS แท็บ <strong>Stock Removal</strong>: <strong>Interval between removing</strong> 20 → <strong>10</strong> วินาที "
        "(Removing starts after 5:00 และ Maximum Stock Removed 1 เหมือนเดิม)",
    ])
)}
<div class="tip"><strong>SimTalk:</strong> <code>WMS.RemoveInterval := 10</code> · Interval คือเวลาระหว่างการนำออกแต่ละครั้ง หน่วยวินาที</div>

<h3>1.2 รัน 8 ชั่วโมง ของในคลังเหลือน้อย</h3>
{side_by_side(
    screenshot("assets/images/simulation/03-02.jpg", "Frame H05 หลังรัน 8 ชั่วโมง"),
    screenshot("assets/images/simulation/03-03.jpg", "สถิติ RSU ของ H05")
)}
{step_list([
    "ตอนจบมีของแค่ <strong>9 ช่อง</strong> (H01: 32)",
    "ยังมีชิ้นงานต่อคิวบนสายพาน",
    "RSU <strong>Waiting 0.19 %</strong> เท่า H01 แต่ย้ายของได้มากขึ้น",
])}
<div class="note"><strong>ข้อสังเกต:</strong> RSU ไม่ว่างเท่ากับ H01 แต่ย้ายของรวม 4,512 ครั้ง (H01: 2,886) — น่าจะเพราะของในคลังน้อย
ช่องที่ใช้อยู่ใกล้ RSU จึงวิ่งระยะสั้นลง (ยังไม่ได้พิสูจน์)</div>

<h3>1.3 เทียบรอบการนำออก (8 ชม.)</h3>
<table>
<tr><th>นำออกทุก</th><th>เข้าคลัง</th><th>ออก Drain</th><th>ช่องที่มีของ</th></tr>
<tr><td>10 วินาที (H05)</td><td>2,263</td><td>2,249</td><td>9 / 100</td></tr>
<tr><td>20 วินาที (H01)</td><td>1,461</td><td>1,425</td><td>32 / 100</td></tr>
<tr><td>30 วินาที</td><td>1,055</td><td>950</td><td>100 / 100 (เต็ม)</td></tr>
<tr><td>60 วินาที</td><td>580</td><td>475</td><td>100 / 100 (เต็ม)</td></tr>
</table>
<p>ของออก Drain ≈ (8 ชม. − 5 นาที) ÷ Interval เมื่อในคลังมีของพอ</p>
<table>
<tr><th>ถ้า</th><th>ผล</th></tr>
<tr><td>นำออกเร็วเท่ากับของเข้า (10 วินาที)</td><td>คลังเกือบว่าง ของไหลผ่าน</td></tr>
<tr><td>นำออกช้ากว่าของเข้า (30–60 วินาที)</td><td>คลังเต็ม ของเข้าลดลงตามของออก</td></tr>
<tr><td>ระหว่างกลาง (20 วินาที)</td><td>คลังมีของบางส่วน</td></tr>
</table>
<div class="note"><strong>ชวนคิด:</strong> รอบการนำออกใช้แทน<strong>ความต้องการของลูกค้า</strong> — คลังจริงควรมีของในคลังเท่าไร?</div>

<h2>2. ข้อมูลสินค้าเข้า — H06 สินค้า 2 ชนิด เก็บแบบ Random</h2>
<p>Frame <code>H06_Random</code>: สินค้า 2 ชนิด PartA และ PartB เข้าคลังสลับกัน WMS เลือกช่องเก็บแบบสุ่ม</p>
<div class="note"><strong>ตั้งค่าต่างจาก H01:</strong> Frame H06–H09 ใช้ Source ปล่อยชิ้นงานต่อเนื่อง (Interval 0) และ WMS เริ่มนำออกนาทีที่ 20
ทุก 5 นาที ครั้งละ 20 ชิ้น — ห้ามเทียบตัวเลขกับ H01 ตรง ๆ</div>

<h3>2.1 Source ปล่อย PartA และ PartB สลับกัน</h3>
{side_by_side(
    screenshot("assets/images/simulation/03-04.jpg", "Source แท็บ Attributes: Interval 0, MU Selection Sequence Cyclical"),
    step_list([
        "<strong>Interval 0</strong> — ปล่อยต่อเนื่อง เร็วเท่าที่สายพานรับ",
        "<strong>MU Selection = Sequence Cyclical</strong> — วนตามลำดับในตาราง",
        "<strong>Table = DataTable</strong> — PartA 1 ชิ้น, PartB 1 ชิ้น",
    ])
)}
<div class="tip"><strong>ที่อยู่:</strong> ดับเบิลคลิก Source แท็บ Attributes · ตาราง DataTable อยู่ใน Frame ข้าง Source ·
PartA และ PartB อยู่ใน Class Library › UserObjects</div>

<h3>2.2 WMS เก็บแบบ Random</h3>
{side_by_side(
    screenshot("assets/images/simulation/03-05.jpg", "WMS แท็บ Strategy: Random"),
    screenshot("assets/images/simulation/03-06.jpg", "WMS แท็บ Stock Removal ของ H06")
)}
{step_list([
    "<strong>Storing strategy = Random</strong> — สุ่มช่องว่าง",
    "เริ่มนำออกหลัง <strong>20 นาที</strong>",
    "นำออกทุก <strong>5 นาที</strong>",
    "ครั้งละไม่เกิน <strong>20 ชิ้น</strong>",
])}

<h3>2.3 รัน 8 ชั่วโมง สินค้าปนกันทั้งชั้น</h3>
{side_by_side(
    screenshot("assets/images/simulation/03-07.jpg", "Frame H06 หลังรัน สินค้า 2 สีปนกัน"),
    screenshot("assets/images/simulation/03-08.jpg", "WMS แท็บ Statistics: Rack Space Utilization 96 %")
)}
{step_list([
    "PartA และ PartB (2 สี) ปนกันทั่วชั้น",
    "ชิ้นงานต่อคิวบนสายพาน",
    "<strong>Rack Space Utilization 96 %</strong>",
])}
<table>
<tr><th>ค่าที่อ่าน</th><th>ผล</th><th>ความหมาย</th></tr>
<tr><td>ชิ้นงานเข้าคลัง</td><td>972</td><td>Source ปล่อยได้เท่าที่ RSU เก็บทัน</td></tr>
<tr><td>ชิ้นงานออก Drain</td><td>874</td><td>นำออกครั้งละ 20 ทุก 5 นาที</td></tr>
<tr><td>ช่องที่มีของตอนจบ</td><td>96 / 100</td><td>เกือบเต็ม</td></tr>
<tr><td>RSU Waiting</td><td>17 %</td><td>RSU มีเวลาว่าง</td></tr>
</table>

<h2>3. กลยุทธ์จัดเก็บ — H07 · H08 · H09</h2>

<h3>3.1 H07 แบ่งโซนคอลัมน์ (XYZ ranges)</h3>
<p>Frame <code>H07_XYZ</code> = H06 ที่เปลี่ยนกลยุทธ์เป็น XYZ ranges และกรอกตาราง Product Ranges</p>
{side_by_side(
    screenshot("assets/images/simulation/03-09.jpg", "WMS Storing strategy XYZ ranges และปุ่ม Product Ranges"),
    screenshot("assets/images/simulation/03-10.jpg", "ตาราง Product Ranges")
)}
{step_list([
    "<strong>Storing strategy = XYZ ranges</strong>",
    "คลิกปุ่ม <strong>Product Ranges</strong> (ใช้ได้เมื่อเลือก XYZ)",
    "PartA ใน Racklane คอลัมน์ <strong>1 ถึง 5</strong>",
    "PartB ใน Racklane คอลัมน์ <strong>6 ถึง 10</strong>",
])}
{side_by_side(
    screenshot("assets/images/simulation/03-11.jpg", "Frame H07 หลังรัน สินค้าแยกโซน"),
    """<ul>
<li>คอลัมน์ 1–5 (ฝั่งสายพาน): PartA อย่างเดียว (1)</li>
<li>คอลัมน์ 6–10: PartB อย่างเดียว (2)</li>
</ul>
<p><strong>เทียบกับ Random (H06):</strong> เข้าคลัง 972 → 873 (−10 %) · ออก 874 → 805 · ช่องที่มีของ 96 → 66</p>"""
)}
<div class="note"><strong>ข้อควรจำ:</strong> สินค้าแต่ละชนิดมีที่ได้แค่ 50 ช่อง โซนเต็มแล้วต้องรอ — แบ่งโซนแล้วหาของง่าย
แต่ใช้ที่ได้น้อยลง เพราะโซนของชนิดหนึ่งเต็มขณะที่อีกโซนยังว่าง</div>

<h3>3.2 H08 แยกชั้นตามสินค้า (Predefined racks)</h3>
<p>Frame <code>H08_PredefinedRacks</code>: RackLane 2 ชุดรวม 200 ช่อง กำหนดให้ PartA ไป RackLane และ PartB ไป RackLane2</p>
{side_by_side(
    screenshot("assets/images/simulation/03-12.jpg", "Frame H08 ก่อนรัน มี RackLane 2 ชุด"),
    step_list([
        "<strong>Source</strong>",
        "<strong>Source2</strong> — ปล่อย PartA / PartB เข้าสายพานเดียวกัน",
        "<strong>RackLane</strong> 100 ช่อง",
        "<strong>RackLane2</strong> 100 ช่อง",
        "<strong>Drain</strong>",
        "<strong>WMS</strong> — ตัวเดียวคุมทั้งคู่",
    ])
)}
<div class="tip"><strong>ตั้งค่า:</strong> RackLane ทั้ง 2 ชุด แท็บ Racks ใส่ชื่อ WMS</div>
{side_by_side(
    screenshot("assets/images/simulation/03-13.jpg", "WMS Storing strategy Predefined racks"),
    screenshot("assets/images/simulation/03-14.jpg", "ตาราง Predefined Racks")
)}
{step_list([
    "<strong>Storing strategy = Predefined racks</strong>",
    "คลิกปุ่ม <strong>Predefined Racks</strong>",
    "PartA → <strong>Racklane</strong>",
    "PartB → <strong>Racklane2</strong>",
])}
{side_by_side(
    screenshot("assets/images/simulation/03-15.jpg", "Frame H08 หลังรัน 8 ชั่วโมง"),
    """<ul>
<li>RackLane: PartA อย่างเดียว (1)</li>
<li>RackLane2: PartB อย่างเดียว (2)</li>
<li>เข้า <strong>1,152</strong> (576 + 576) ออก 994 ใช้ 155 / 200 ช่อง</li>
</ul>
<p>RSU 2 คันทำงานพร้อมกัน ของเข้ามากกว่า H06 (972)</p>"""
)}

<h3>3.3 H09 เทียบกลยุทธ์ให้ยุติธรรม</h3>
<p>Frame <code>H09_CompareStrategies</code> = H06 ที่กรอก Product Ranges ไว้แล้ว บันทึกไว้ที่ One by one — ใช้ชิ้นงานและการนำออกชุดเดียวกัน
เปลี่ยนแค่ช่อง Storing strategy</p>
{side_by_side(
    screenshot("assets/images/simulation/03-16.jpg", "WMS เลือก Storing strategy"),
    step_list([
        "WMS แท็บ Strategy เปิดช่อง <strong>Storing strategy</strong>",
        "เลือก <strong>One by one / Random / XYZ ranges</strong> ทีละแบบ แล้วคลิก OK รัน 8 ชม. จดผล",
    ])
)}
<table>
<tr><th>กลยุทธ์</th><th>เข้าคลัง</th><th>ออก Drain</th><th>ช่องที่มีของ</th><th>RSU ว่าง (Waiting)</th></tr>
<tr><td>One by one — เก็บเรียงช่อง</td><td>977</td><td>879</td><td>96</td><td>18 %</td></tr>
<tr><td>Random — สุ่มช่องว่าง</td><td>972</td><td>874</td><td>96</td><td>17 %</td></tr>
<tr><td>XYZ ranges — PartA 1–5, PartB 6–10</td><td>873 (−11 %)</td><td>805</td><td>66</td><td>31 %</td></tr>
</table>
<table>
<tr><th>ข้อสังเกต</th><th>เหตุผล</th></tr>
<tr><td>One by one กับ Random ได้ผลใกล้กัน</td><td>ใช้ทุกช่องได้ทั้ง 2 ชนิด</td></tr>
<tr><td>XYZ ranges เข้าคลังน้อยที่สุด</td><td>โซนของชนิดหนึ่งเต็มก่อน อีกชนิดต้องรอ</td></tr>
<tr><td>XYZ ranges RSU ว่างมากที่สุด (31 %)</td><td>RSU รอชิ้นงานที่เข้าโซนได้</td></tr>
</table>
<div class="note"><strong>เลือกกลยุทธ์ตามงานจริง:</strong> แบ่งโซนช่วยหยิบของง่าย แต่ต้องเผื่อพื้นที่ · Predefined racks ต้องมี RackLane หลายชุด (H08)
จึงไม่อยู่ในการเทียบนี้ — <strong>ชวนคิด:</strong> ถ้า PartA ขายดีกว่า PartB ควรแบ่งคอลัมน์อย่างไร?</div>
<div class="tip"><strong>SimTalk:</strong> <code>WMS.StrategyIndex</code> 1 = One by one · 2 = Random · 3 = Predefined · 4 = XYZ</div>

<h2>4. Method — H10 สต็อกตั้งต้น · H11 นำออกตามคำสั่งซื้อ</h2>

<h3>4.1 H10 เติมของในคลังก่อนเริ่มรัน (Method Init)</h3>
<p>Frame <code>H10_InitialStock</code> = H01 + Method <code>Init</code> — คลังจริงไม่ได้เริ่มจากว่าง Method ที่ชื่อ <code>Init</code>
ถูกเรียกเองตอนเริ่มรัน (Method อยู่ใน Toolbox แท็บ Information Flow)</p>
{screenshot("assets/images/simulation/03-17.jpg", "โค้ด Method Init ที่เติมของ 50 ช่อง")}
{step_list([
    "คอลัมน์ 1 ถึง 5",
    "ชั้น 1 ถึง 5",
    "<code>RackLane.createPart(.MUs.Part, true, col, row)</code> — ชั้นด้านซ้าย",
    "<code>false</code> = ชั้นด้านขวา — รวม 5 × 5 × 2 = 50 ชิ้น",
])}
<div class="tip"><strong>createPart(Class, ด้าน, คอลัมน์, ชั้น):</strong> จองช่องและลงทะเบียนใน WMS ให้เอง (ตาราง Content และ Inventory)
· คลิกที่ภาพเพื่อดูโค้ดขนาดเต็ม</div>
{side_by_side(
    screenshot("assets/images/simulation/03-18.jpg", "Frame H10 ที่เวลา 1 วินาที ชั้นมีของแล้ว"),
    screenshot("assets/images/simulation/03-19.jpg", "เวลาจำลอง 1 วินาที")
)}
{step_list([
    "ของ <strong>50 ช่อง</strong> คอลัมน์ 1–5 (ฝั่งสายพาน)",
    "เวลา 1 วินาที: WMS ช่องว่าง 50 / มีของ 50 (<code>WMS.NumFreePlaces</code> / <code>NumOccupiedPlaces</code>)",
])}
<table>
<tr><th>ค่า (8 ชม.)</th><th>H01 เริ่มว่าง</th><th>H10 เริ่ม 50 ชิ้น</th></tr>
<tr><td>ชิ้นงานเข้าคลังจาก Source</td><td>1,461</td><td>1,411 (−50)</td></tr>
<tr><td>ชิ้นงานออก Drain</td><td>1,425</td><td>1,425</td></tr>
<tr><td>ช่องที่มีของตอนจบ</td><td>32</td><td>32</td></tr>
</table>
<p>ของออกเท่าเดิม แต่ Source ส่งเข้าน้อยลง 50 ชิ้น เท่ากับของที่เติมไว้ — ใช้สต็อกตั้งต้นเมื่ออยากให้ช่วงแรกของการรันเหมือนคลังจริง</p>

<h3>4.2 H11 นำของออกตามคำสั่งซื้อ (ตาราง Orders + Method OrderControl)</h3>
<p>Frame <code>H11_OrderRemoval</code> = H06 (PartA / PartB) ที่ปิดการนำออกอัตโนมัติ + ตาราง <code>Orders</code> + Method <code>Init</code>
และ <code>OrderControl</code> — รวมเรื่องปิดการนำออก (H04), สินค้า 2 ชนิด (H06) และ Method Init (H10)</p>
{side_by_side(
    screenshot("assets/images/simulation/03-20.jpg", "WMS แท็บ Stock Removal ปิดการนำออกอัตโนมัติ"),
    screenshot("assets/images/simulation/03-21.jpg", "ตาราง Orders")
)}
{step_list([
    "WMS แท็บ Stock Removal: คลิกช่อง <strong>Automatic stock removal</strong> ให้เครื่องหมายถูกหายไป ☐",
    "ตาราง <strong>Orders</strong> คอลัมน์ 1: ชื่อสินค้า (string)",
    "คอลัมน์ 2: จำนวน (integer) — 4 แถว: PartA 3, PartB 5, PartA 2, PartB 4 แล้ววนซ้ำ",
])}
{screenshot("assets/images/simulation/03-22.jpg", "โค้ด Method OrderControl")}
{step_list([
    "<code>wait 120</code> — ทุก 2 นาที",
    "อ่านแถวถัดไปของ <code>Orders</code>",
    "หาแถวสินค้าใน <code>WMS.Content</code>",
    "เช็กว่าสต็อกพอ",
    "<code>WMS.removeProducts</code> นำออก",
    "วนกลับแถวแรก",
])}
<div class="tip"><strong>เริ่ม OrderControl:</strong> Method <code>Init</code> ใน Frame นี้มีบรรทัดเดียว <code>&amp;OrderControl.methCall(0)</code>
เริ่ม OrderControl เป็นงานแยก · คลิกที่ภาพเพื่อดูโค้ดขนาดเต็ม</div>
<table>
<tr><th>ค่าที่อ่าน (8 ชม.)</th><th>ผล</th><th>ความหมาย</th></tr>
<tr><td>ชิ้นงานเข้าคลัง</td><td>796</td><td></td></tr>
<tr><td>นำออกตามคำสั่งซื้อ</td><td>693</td><td>เฉลี่ย 3.5 ชิ้น ทุก 2 นาที</td></tr>
<tr><td>ช่องที่มีของตอนจบ</td><td>100 / 100</td><td>คลังเต็ม ของเข้ามากกว่าคำสั่งซื้อ</td></tr>
</table>
<p>ถ้าทุกคำสั่งนำออกได้ จะได้ 840 ชิ้น (240 คำสั่ง × 3.5) ที่เหลือคือรอบที่สต็อกไม่พอ โค้ดจึงข้ามไป</p>
<table>
<tr><th>ข้อควรระวังกับ WMS.removeProducts</th><th>สิ่งที่พบ</th></tr>
<tr><td>OrderNo</td><td>ต้องเป็น string (คู่มือเขียน integer ซึ่งผิด) ใช้ <code>to_str(row)</code></td></tr>
<tr><td>สต็อกไม่พอ</td><td>Library เปิด Debugger ค้าง ต้องเช็ก <code>WMS.Content</code> ก่อนเรียกเสมอ</td></tr>
<tr><td>WMS.Content</td><td><code>[0, row]</code> = ชื่อสินค้า, <code>[1, row]</code> = จำนวน</td></tr>
</table>

<h2>5. สถิติ — H12 RSU เสีย และเก็บสถิติลงตาราง</h2>
<p>Frame <code>H12_FailuresStats</code> = H01 + RSU เสีย + ตาราง <code>RSUStats</code> + Method <code>EndSim</code>
— การเสียเป็นแบบสุ่มแต่ใช้ seed เดิมทุกครั้ง รันซ้ำจึงได้ตัวเลขเดิม</p>
{side_by_side(
    screenshot("assets/images/simulation/03-23.jpg", "RackLane แท็บ Rack Serving Unit: Availability 80, MTTR 300"),
    step_list([
        "RackLane แท็บ Rack Serving Unit: <strong>Availability 80</strong> — สัดส่วนเวลาที่ RSU พร้อมทำงาน",
        "<strong>MTTR 300</strong> วินาที (5 นาที) — เวลาซ่อมเฉลี่ย",
    ])
)}
<div class="tip"><strong>SimTalk:</strong> <code>RackLane.RSU_Availability := 80</code> · <code>RackLane.RSU_MTTR := 300</code></div>
{side_by_side(
    screenshot("assets/images/simulation/03-24.jpg", "โค้ด Method EndSim"),
    screenshot("assets/images/simulation/03-25.jpg", "ตาราง RSUStats หลังรัน")
)}
{step_list([
    "<code>RackLane.statistic(RSUStats)</code> — คัดลอกสถิติ RSU ลงตาราง",
    "หลังรัน: <strong>Failed 20.1 %</strong>",
    "แถวแรกมีป้าย State = Drive home (ชื่อสถานะใน Library ไม่ตรง)",
])}
<div class="note"><strong>EndSim:</strong> Method ที่ชื่อ <code>EndSim</code> ถูกเรียกเองเมื่อรันถึงเวลา End ของ EventController</div>
{side_by_side(
    screenshot("assets/images/simulation/03-26.jpg", "สถิติ RSU ของ H01: Failed 0 %"),
    screenshot("assets/images/simulation/03-27.jpg", "สถิติ RSU ของ H12: Failed 20.14 %")
)}
{step_list([
    "H01: <strong>Failed 0 %</strong>",
    "H12: <strong>Failed 20.14 %</strong> ตรงกับ Availability 80 % — Waiting ยังเป็น 0.19 % เท่า H01 RSU ยังเป็นคอขวด",
])}
<table>
<tr><th>ค่า (8 ชม.)</th><th>H01 ไม่มีเสีย</th><th>H12 มีเสีย</th></tr>
<tr><td>ชิ้นงานเข้าคลัง</td><td>1,461</td><td>1,313 (−10 %)</td></tr>
<tr><td>ชิ้นงานออก Drain</td><td>1,425</td><td>1,288</td></tr>
<tr><td>RSU Failed</td><td>0 %</td><td>20.1 %</td></tr>
</table>
<p>RSU เป็นคอขวดอยู่แล้ว เวลาที่เสียจึงลดของเข้าคลังโดยตรง</p>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>ช่อง Interval เป็นสีเทา แก้ไม่ได้</td><td>คลิกช่อง Automatic stock removal ให้ขึ้น ☑ ก่อน (H05)</td></tr>
<tr><td>ของไม่ออกในช่วงแรก</td><td>ดูค่า Removing starts after (H05 = 5:00, H06–H09 = 20:00)</td></tr>
<tr><td>ได้ชิ้นงานชนิดเดียว</td><td>Source: MU Selection = Sequence Cyclical และตารางมี 2 แถว (H06)</td></tr>
<tr><td>ปุ่ม Product Ranges / Predefined Racks เป็นสีเทา</td><td>เลือก Storing strategy = XYZ ranges / Predefined racks ก่อน (H07, H08)</td></tr>
<tr><td>RackLane2 ไม่มีของเข้า</td><td>RackLane2 แท็บ Racks: ใส่ชื่อ WMS (H08)</td></tr>
<tr><td>ชั้นว่างตอนเริ่มรัน</td><td>Method ต้องชื่อ <code>Init</code> และอยู่ใน Frame เดียวกัน แล้วกด Reset (H10)</td></tr>
<tr><td>รันแล้วเปิด Debugger ค้าง</td><td>เช็กสต็อกด้วย <code>WMS.Content</code> ก่อนเรียก <code>removeProducts</code> (H11)</td></tr>
<tr><td>ไม่มีของออก Drain เลย</td><td>ตรวจว่า <code>Init</code> เรียก <code>OrderControl</code> (H11)</td></tr>
<tr><td>ตาราง RSUStats ว่าง</td><td>รันให้ถึง End ของ EventController (8 ชม.) (H12)</td></tr>
<tr><td>รันซ้ำได้ตัวเลขเดิม</td><td>seed สุ่มเดิม — ใช้ ExperimentManager รันหลาย replication (บท <a href="ai-02.html">3.2</a>)</td></tr>
</table>
'''
