# -*- coding: utf-8 -*-
"""ai 2 (practice): นำเข้าข้อมูล และจำลองสถานการณ์ -- user 2026-11-24: step by step on the example
01_Training_Model\\2504_AI\\3_2_Excel_Experiment.spp + Inbound.xlsx (built by build_ai.py, PtS 2504).
Screens captured on PtS 2504 (scratchpad ai\\cap_ai.py + crop_ai.py), numbers from check_ai.py / the captured run."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "อ่านตารางรถเข้าจาก Excel มาเป็น DataTable และให้ Source สร้างพาเลทตามตาราง (Delivery Table) ได้",
    "ใช้ ParallelStation แทน Forklift หลายคัน และวัดผลด้วย Method ได้",
    "ตั้ง ExperimentManager ทดลองหลายสถานการณ์ รันซ้ำ และอ่านตารางผลได้",
    "เลือกจำนวน Forklift ที่พอดีกับงานจากผลการทดลองได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ข้อมูลจริงของคลังมักอยู่ใน Excel — บทนี้อ่าน<strong>ตารางรถเข้า 8 ชั่วโมง</strong>จาก Excel
ให้ Source สร้างพาเลทตามเวลาจริง แล้วใช้ <strong>ExperimentManager</strong> ลองจำนวน Forklift 1–4 คันในครั้งเดียว
เพื่อตอบคำถามว่า <strong>"ต้องใช้ Forklift กี่คันจึงเก็บของเข้าชั้นได้ทันในกะเดียว"</strong></p>

<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 · ไฟล์ <code>3_2_Excel_Experiment.spp</code> และ <code>Inbound.xlsx</code>
ในโฟลเดอร์ <code>2504_AI</code> ของ<a href="start-02.html">ไฟล์ตัวอย่าง</a> · เครื่องต้องมี Microsoft Excel
(Plant Simulation อ่าน .xlsx ผ่าน Excel)
</div>

<h2>ภาพรวม: 6 ขั้น</h2>
<table>
<tr><th>ขั้นที่</th><th>เรื่อง</th><th>ได้อะไร</th></tr>
<tr><td>1</td><td>เปิดแบบจำลอง</td><td>รู้จัก Object ทั้งหมดในเฟรม</td></tr>
<tr><td>2</td><td>ข้อมูลใน Excel</td><td>ตารางรถเข้า 8 แถว 250 พาเลท</td></tr>
<tr><td>3</td><td>Source แบบ Delivery Table</td><td>Source สร้างพาเลทตามเวลาในตาราง</td></tr>
<tr><td>4</td><td>Method ReadExcel</td><td>อ่าน Excel เข้า Inbound_Table</td></tr>
<tr><td>5</td><td>Forklift และค่าที่วัด</td><td>Putaway = Forklift, LeadTimeMin = เวลาเฉลี่ย</td></tr>
<tr><td>6</td><td>ExperimentManager</td><td>Forklift 1–4 คัน × 3 รอบ → เลือกจำนวนที่พอดี</td></tr>
</table>

<h2>ขั้นที่ 1: เปิดแบบจำลอง</h2>
{screenshot("assets/images/ai/02-01.jpg", "เฟรม Inbound_Model: Inbound → Dock → Putaway → Rack, Inbound_Table, ExcelFile, ReadExcel, ExperimentManager, LeadTimeMin")}
{step_list([
    "เปิด <code>3_2_Excel_Experiment.spp</code> แล้วเปิดเฟรม <code>Models › Inbound_Model</code>",
    "แถวกลาง: <code>Inbound</code> (Source = รถเข้า) → <code>Dock</code> (Buffer = ท่ารับ จุได้ 500) → <code>Putaway</code> (ParallelStation = Forklift) → <code>Rack</code> (Drain = ขึ้นชั้นแล้ว)",
    "แถวบน: <code>Inbound_Table</code> (ตารางรถเข้า), <code>ExcelFile</code> (ที่อยู่ไฟล์ Excel), <code>ReadExcel</code> (Method อ่าน Excel)",
    "แถวล่าง: <code>ExperimentManager</code> และ <code>LeadTimeMin</code> (Method คิดเวลาเฉลี่ย) — กล่องข้อความสรุปวิธีใช้",
])}

<h2>ขั้นที่ 2: ข้อมูลใน Excel</h2>
<p>เปิด <code>Inbound.xlsx</code> ชีต <strong>Inbound</strong> — 1 แถว = รถ 1 รอบที่มาถึง (เริ่มกะ 0:00 · ช่วงพักเที่ยง 4:00 รถน้อย):</p>
<table>
<tr><th>Delivery Time</th><th>MU</th><th>Number</th><th>Name</th></tr>
<tr><td>0:00:00</td><td>.MUs.Part</td><td>20</td><td>Pallet</td></tr>
<tr><td>1:00:00</td><td>.MUs.Part</td><td>35</td><td>Pallet</td></tr>
<tr><td>2:00:00</td><td>.MUs.Part</td><td>50</td><td>Pallet</td></tr>
<tr><td>3:00:00</td><td>.MUs.Part</td><td>40</td><td>Pallet</td></tr>
<tr><td>4:00:00</td><td>.MUs.Part</td><td>10</td><td>Pallet</td></tr>
<tr><td>5:00:00</td><td>.MUs.Part</td><td>45</td><td>Pallet</td></tr>
<tr><td>6:00:00</td><td>.MUs.Part</td><td>30</td><td>Pallet</td></tr>
<tr><td>7:00:00</td><td>.MUs.Part</td><td>20</td><td>Pallet</td></tr>
</table>
<p>รวม <strong>250 พาเลท</strong> ใน 8 ชั่วโมง ≈ 31 พาเลท/ชม.</p>
<div class="note"><strong>เขียนชื่อ MU เต็ม:</strong> คอลัมน์ MU ต้องเป็น <code>.MUs.Part</code> (มีจุดนำหน้า) — ถ้าเขียนแค่ <code>Part</code>
Plant Simulation อ่านเป็นค่าว่าง และ Source จะไม่สร้างพาเลทเลย (ทดลองแล้วบน 2504)</div>

<h2>ขั้นที่ 3: Source แบบ Delivery Table</h2>
{side_by_side(
    screenshot("assets/images/ai/02-03.jpg", "หน้าต่าง Inbound: Time of Creation = Delivery Table, Table = Inbound_Table"),
    screenshot("assets/images/ai/02-02.jpg", "Inbound_Table ก่อนอ่าน Excel: คอลัมน์ time, object, integer, string"))}
{step_list([
    "ดับเบิลคลิก <code>Inbound</code> › แท็บ <code>Attributes</code>",
    "<code>Time of Creation</code> = <strong>Delivery Table</strong> (ไม่ใช่ Interval Adjustable)",
    "<code>Table</code> = <code>Inbound_Table</code> — Source จะสร้าง MU ตามแถวในตารางนี้",
    "ดับเบิลคลิก <code>Inbound_Table</code>: 4 คอลัมน์ตั้งชนิดข้อมูลไว้แล้ว — <code>time</code> (Delivery Time), <code>object</code> (MU), <code>integer</code> (Number), <code>string</code> (Name)",
])}
<div class="tip"><strong>ชนิดข้อมูลของคอลัมน์สำคัญ:</strong> ตั้งชนิดคอลัมน์ให้ถูกก่อนอ่าน Excel — Plant Simulation จะแปลงข้อความ
<code>1:00:00</code> เป็นเวลา และ <code>.MUs.Part</code> เป็น Object ให้เอง</div>

<h2>ขั้นที่ 4: Method ReadExcel — อ่าน Excel เข้าตาราง</h2>
{screenshot("assets/images/ai/02-04.jpg", "โค้ด Method ReadExcel: readExcelFile และ selectFileForOpen")}
{step_list([
    "ดับเบิลคลิก <code>ReadExcel</code> ดูโค้ด: <code>Inbound_Table.readExcelFile(ExcelFile, &quot;Inbound&quot;, true)</code> อ่านชีต Inbound เข้าตาราง",
    "ครั้งแรกตัวแปร <code>ExcelFile</code> ยังว่าง โค้ดจึงเปิดหน้าต่าง Open (<code>selectFileForOpen</code>) ให้เลือก <code>Inbound.xlsx</code>",
    "กด <code>Run</code> (F5) ในหน้าต่าง Method › เลือกไฟล์ › ขึ้นข้อความ <em>อ่าน Excel แล้ว 8 แถว</em>",
    "ไฟล์ที่เลือกถูกจำไว้ใน <code>ExcelFile</code> — ครั้งต่อไปกด Run ได้เลย",
])}
{side_by_side(
    screenshot("assets/images/ai/02-05.jpg", "Variable ExcelFile ชนิด string ยังว่างก่อนอ่านครั้งแรก"),
    screenshot("assets/images/ai/02-06.jpg", "Inbound_Table หลังอ่าน Excel: 8 แถว เวลา 0:00 ถึง 7:00"))}
<div class="note"><strong>แก้ข้อมูลใน Excel แล้วต้องอ่านใหม่:</strong> แบบจำลองใช้ข้อมูลใน <code>Inbound_Table</code> ไม่ได้เปิด Excel ทุกครั้งที่รัน
— เปลี่ยนตัวเลขใน Excel แล้วต้องรัน <code>ReadExcel</code> อีกรอบ</div>

<h2>ขั้นที่ 5: Forklift และค่าที่วัด</h2>
{side_by_side(
    screenshot("assets/images/ai/02-07.jpg", "Putaway: X-Dimension 2 = Forklift 2 คัน, Start Processing When Full ไม่เลือก"),
    screenshot("assets/images/ai/02-08.jpg", "Method LeadTimeMin คืนค่าเวลาเฉลี่ยเป็นนาที"))}
{step_list([
    "ดับเบิลคลิก <code>Putaway</code> (ParallelStation): <code>X-Dimension</code> = จำนวน Forklift (ในไฟล์ = 2), Y-Dimension = 1",
    "☐ <code>Start Processing When Full</code> — ไม่เลือก ไม่อย่างนั้นทุกช่องต้องมีพาเลทครบก่อน Forklift จึงเริ่มงาน",
    "แท็บ Times: ยกพาเลทละ 4 นาที (1 คันเก็บได้ 15 พาเลท/ชม.) · แท็บ Failures: Availability 95 %, MTTR 10 นาที (มีเสียแบบสุ่ม ผลแต่ละรอบจึงต่างกัน)",
    "<code>LeadTimeMin</code>: เวลาเฉลี่ยตั้งแต่พาเลทมาถึงจนขึ้นชั้น (<code>Rack.StatAvgLifeSpan / 60</code>) — ถ้ายังไม่มีพาเลทเข้า Rack คืน 0",
    "ลองรันครั้งเดียว: กด <code>Start</code> ที่ EventController (จบเองที่ 8 ชม.) แล้วดูจำนวนใน Rack และที่ค้างใน Dock",
])}
{screenshot("assets/images/ai/02-09.jpg", "หลังรัน 8 ชม. ด้วย Forklift 2 คัน")}
<div class="tip"><strong>ทำไมใช้ Method เป็นค่าผลตอบ:</strong> ExperimentManager อ่านค่าได้ทั้ง Attribute (เช่น <code>Rack.StatNumIn</code>)
และ Method ที่คืนตัวเลข — แต่มันเรียก Method ตอนเวลา 0 ด้วย ต้องกันการหารด้วยศูนย์ ไม่อย่างนั้นการทดลองหยุดเงียบ ๆ และตารางผลว่าง</div>

<h2>ขั้นที่ 6: ExperimentManager — Forklift 1–4 คัน</h2>
<p>ExperimentManager ตั้งไว้แล้วในไฟล์:</p>
<table>
<tr><th>ส่วน</th><th>ค่า</th></tr>
<tr><td>Define Input Values</td><td><code>root.Putaway.XDim</code></td></tr>
<tr><td>Define Experiments</td><td>4 ชุด: XDim = 1, 2, 3, 4</td></tr>
<tr><td>Define Output Values</td><td><code>root.Rack.StatNumIn</code> (ขึ้นชั้นแล้ว) · <code>root.Dock.NumMU</code> (ค้างที่ท่าตอนจบกะ) · <code>root.LeadTimeMin</code></td></tr>
<tr><td>Observations per experiment</td><td>3 รอบต่อชุด</td></tr>
</table>
{screenshot("assets/images/ai/02-10.jpg", "หน้าต่าง Experiments ก่อนและหลังรัน: Current experiment 4/4, Observation 3/3")}
{step_list([
    "ดับเบิลคลิก <code>ExperimentManager</code> — หน้าต่าง <strong>Experiments</strong> เปิดขึ้น",
    "ถ้าปุ่ม <code>Start</code> เป็นสีเทา กด <code>Reset</code> ก่อน",
    "กด <code>Start</code> — รัน 4 ชุด × 3 รอบ = 12 รอบ (เสร็จในไม่กี่วินาที) ขึ้น Current experiment 4/4, Observation 3/3",
    "ดูผล: แท็บ <code>Evaluation</code> หรือเปิดตาราง <code>ExperimentManager › Results</code> (ค่าเฉลี่ยของ 3 รอบ)",
])}
{screenshot("assets/images/ai/02-11.jpg", "ตาราง Results: Exp 1–4")}

<h2>อ่านผล: ใช้ Forklift กี่คัน</h2>
<table>
<tr><th>Forklift</th><th>ขึ้นชั้นใน 8 ชม.</th><th>ค้างที่ท่า</th><th>เวลาเฉลี่ย (นาที)</th></tr>
<tr><td>1 คัน</td><td>114</td><td>135</td><td>152</td></tr>
<tr><td>2 คัน</td><td>218</td><td>30</td><td>73</td></tr>
<tr><td><strong>3 คัน</strong></td><td><strong>250</strong></td><td><strong>0</strong></td><td><strong>32</strong></td></tr>
<tr><td>4 คัน</td><td>250</td><td>0</td><td>22</td></tr>
</table>
<p>ค่าเฉลี่ย 3 รอบ วัดบน Plant Simulation 2504 · รถเข้าเฉลี่ย 31 พาเลท/ชม. แต่ Forklift 2 คันยกได้แค่ 30 พาเลท/ชม. (และมีเสีย)
→ <strong>3 คันเก็บได้ครบในกะ</strong> · คันที่ 4 ลดเวลาเฉลี่ยจาก 32 เหลือ 22 นาทีแต่ไม่ได้เก็บเพิ่ม — คุ้มค่ารถอีก 1 คันหรือไม่
เป็นคำถามด้านการลงทุนในบท <a href="strategy-01.html">4.1</a></p>

<div class="tip"><strong>ลองเอง:</strong> (1) แก้ Excel ให้ชั่วโมง 2:00 มา 80 พาเลท แล้วรัน <code>ReadExcel</code> + ExperimentManager ใหม่ — 3 คันยังพอไหม
(2) เพิ่มชุด Forklift 5 คันใน <code>Define Experiments</code> (3) เปลี่ยน Observations เป็น 10 แล้วดูว่าค่าเฉลี่ยเปลี่ยนไปเท่าไร</div>
'''
