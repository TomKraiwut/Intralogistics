# -*- coding: utf-8 -*-
"""simulation 5 (theory): ระบบขนถ่ายในคลังสินค้าอัตโนมัติ.
Source: 02_Decks\\Theory\\07_S3_Automated_Handling.pptx (16 slides, text + notes, 2026-11-18).
Images: assets/images/simulation/05-01 (slide 12 AS/RS model), 05-02 (slide 14 3D models).
Numbers of the case company come from the first model set -- re-check when the new models are built."""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปรียบเทียบระบบขนถ่าย คน, Forklift, AGV, AMR และ AS/RS และบอกว่าแต่ละแบบสร้างด้วย Object อะไรได้",
    "อธิบายการป้อนข้อมูลสินค้าเข้า–ออก การใช้ Method และการแสดงข้อมูลสินค้าคงคลังในแบบจำลองได้",
    "ตรวจแบบจำลองด้วย Verification และ Validation ก่อนนำผลไปใช้ตัดสินใจได้",
]

TOPICS = []

BODY = f'''
<h2>เริ่มจากตัวเลข: Forklift 3 คัน → 1 คัน</h2>
<p>สยามพาร์ทใช้ Forklift 3 คันมานาน ไม่มีใครเคยวัดว่ารถทำงานจริงกี่เปอร์เซ็นต์ของเวลา พอจำลองพบว่าลดเหลือคันเดียวก็ยังส่งทันเป้า 20 นาที
<strong>ประหยัดได้ปีละ 650,000 บาท</strong> — ก่อนคิดซื้อ AGV หรือ AMR ต้องรู้ก่อนว่าระบบเดิมใช้งานได้เต็มที่หรือยัง</p>

<h2>1. คนและรถขน</h2>

<h3>บันไดสู่คลังอัตโนมัติ: เปลี่ยนทีละขั้น วัดทุกขั้น</h3>
{step_list([
    "<strong>คน</strong> — เดินขนด้วยรถลาก ยืดหยุ่น ลงทุนต่ำ",
    "<strong>Forklift</strong> — ยกพาเลท เร็วขึ้น แต่ต้องมีคนขับ",
    "<strong>AGV</strong> — อัตโนมัติ วิ่งตามเส้นทางที่กำหนด",
    "<strong>AMR</strong> — อัตโนมัติ หาเส้นทางเอง หลบคน",
    "<strong>AS/RS</strong> — เครนเก็บและหยิบในชั้นสูงเอง",
])}
<div class="tip"><strong>ทุกขั้นวัดด้วย KPI เดียวกัน:</strong> ส่งครบ · lead time · utilization · ต้นทุน · คาร์บอน
— ภาคปฏิบัติจะสร้างและเทียบทุกขั้นบนงานเดียวกัน</div>

<h3>ลำเลียงสินค้าด้วยคน: WorkerPool · Broker</h3>
<ul>
<li><strong>WorkerPool</strong> — ห้องพักของพนักงาน กำหนดจำนวนคนและความเร็วเดิน และผูกกับกะทำงาน (ShiftCalendar)</li>
<li><strong>Broker</strong> — คนกลางจับคู่งานกับคน เมื่อมีงาน ส่งคนที่ว่างไป คนเดียวทำได้หลายจุด</li>
<li><strong>ผลที่วัดได้</strong> — utilization ของคน เวลารอคน งานค้างตอนเลิกงาน และระยะเดินต่อวัน</li>
</ul>
<p>ในแบบจำลองรุ่นทดลอง คนไม่ตรงกับช่วงงานหนักทำให้พาเลทค้าง 11 พาเลทตอนเลิกงาน — ฝึกในบท <a href="simulation-04.html">2.4</a></p>

<h3>Forklift และ AGV: รถที่วิ่งบนเส้นทาง</h3>
<table>
<tr><th></th><th>Forklift</th><th>AGV</th></tr>
<tr><td>สร้างในโปรแกรม</td><td>Transporter บน Track (ทางวิ่ง)</td><td>Transporter บน Track แบบวงรอบทางเดียว</td></tr>
<tr><td>ลักษณะ</td><td>ตั้งความเร็ว เวลายก–วาง ต้องมีคนขับ พักเที่ยงรถหยุด (ผูกกับกะ)</td>
<td>วิ่งตามเส้นทางที่กำหนดเท่านั้น ช้ากว่าแต่ไม่ต้องมีคนขับ ทำงานได้ต่อเนื่อง</td></tr>
<tr><td>คาร์บอน</td><td>ดีเซล → นับลิตร เป็นคาร์บอน Scope 1</td><td>ไฟฟ้า → นับ kWh เป็นคาร์บอน Scope 2</td></tr>
</table>
<p>วาด Track และให้รถ Transporter วิ่งขนชิ้นงาน — ฝึกในบท <a href="simulation-06.html">2.6</a></p>

<h3>AMR: หุ่นยนต์ที่หาเส้นทางเอง</h3>
{side_by_side(
    """<p><strong>วิธีสร้างในโปรแกรม</strong></p>
<ul>
<li>รถวิ่งอิสระบนพื้นที่ ไม่ต้องวาดทาง</li>
<li>หาเส้นทางสั้นที่สุดเอง หลบสิ่งกีดขวาง</li>
<li>Method สั่ง: ไปรับที่ไหน ส่งที่ไหน</li>
<li>แบตเตอรี่: kWh = Ah × V ÷ 1,000</li>
</ul>""",
    """<p><strong>คำถามที่แบบจำลองตอบ</strong></p>
<ul>
<li>ต้องใช้กี่คันจึงทันเป้า</li>
<li>รถรอกันตรงไหน (จุดคอขวด)</li>
<li>ต้องชาร์จเมื่อไร แบตเตอรี่พอทั้งกะไหม</li>
<li>เวลายก–วางมีผลแค่ไหน</li>
</ul>"""
)}
<p>ในแบบจำลองสยามพาร์ท AMR คันเดียวไม่พอ สองคันพอ — ฝึกสร้าง AMR ในบท <a href="simulation-07.html">2.7</a></p>

<h3>Forklift · AGV · AMR บนงานเดียวกัน</h3>
<p>วัดจากแบบจำลองสยามพาร์ท งาน 120 เที่ยวต่อวัน</p>
<table>
<tr><th>รถ</th><th>ลักษณะ</th><th>ต้องใช้</th><th>lead time</th><th>ต้นทุน/วัน (บาท)</th><th>kgCO₂e/ออเดอร์</th></tr>
<tr><td>Forklift ดีเซล</td><td>2.5 ม./วินาที · ต้องมีคนขับ · พักเที่ยงรถหยุด</td><td>1 คัน</td><td>14.7 นาที</td><td>2,986</td><td>0.130</td></tr>
<tr><td>AGV</td><td>1.0 ม./วินาที · วิ่งตามวงรอบทางเดียว</td><td>2 คัน</td><td>14.8 นาที</td><td>3,618</td><td>0.030</td></tr>
<tr><td>AMR</td><td>1.2 ม./วินาที · หาทางสั้นสุดเอง</td><td>2 คัน</td><td>8.8 นาที</td><td>3,610</td><td>0.017</td></tr>
</table>
<div class="note"><strong>ไม่มีรถแบบไหนชนะทุกเกณฑ์:</strong> Forklift ต้นทุนต่ำสุดแต่ปล่อยคาร์บอนมากกว่า AMR เกือบ 8 เท่าและต้องมีคนขับ
AMR ให้ lead time ดีที่สุด → ต้องตัดสินด้วยหลายเกณฑ์ในบท <a href="strategy-01.html">4.1</a></div>

<h2>2. ข้อมูล Method และสต็อก</h2>

<h3>การป้อนข้อมูลสินค้าเข้า–ออก</h3>
<table>
<tr><th>ข้อมูล</th><th>หน้าตาตาราง</th><th>ใส่ที่ไหนในแบบจำลอง</th></tr>
<tr><td>สินค้าเข้า (รถผู้ขาย)</td><td>เวลา · ชื่อรถ · รหัสสินค้า · จำนวนพาเลท</td><td>Source → Delivery table (ตาราง <code>Deliveries</code>)</td></tr>
<tr><td>สินค้าออก (ออเดอร์)</td><td>เวลา · เลขออเดอร์ · รหัสสินค้า · จำนวน</td><td>ตาราง <code>Orders</code> → Method หยิบตามเวลา</td></tr>
<tr><td>ข้อมูลสินค้า</td><td>รหัส · กลุ่ม ABC · ยอดใช้ · EOQ · ROP · ช่องเก็บ</td><td>ตาราง <code>Products</code></td></tr>
<tr><td>สต็อกตั้งต้น</td><td>จำนวนพาเลทต่อรหัสตอนเริ่มวัน</td><td>Method <code>Init</code> เติมชั้นวางก่อนเริ่ม</td></tr>
<tr><td>ข้อมูลจากระบบจริง</td><td>ไฟล์ Excel / CSV จาก WMS หรือ ERP</td><td>นำเข้าตาราง (ฝึกในบท <a href="ai-02.html">3.2</a>)</td></tr>
</table>
<div class="tip"><strong>แยกข้อมูลไว้ในตาราง:</strong> เปลี่ยนสถานการณ์ได้โดยไม่ต้องแก้แบบจำลอง</div>

<h3>Method กับแบบจำลองคลัง: กฎการทำงานที่ทำให้โมเดลคิดได้</h3>
{side_by_side(
    """<p><strong>Method ในคลังของเราทำอะไร</strong></p>
<ul>
<li><code>Init</code> — เติมสต็อกตั้งต้นตอนเริ่ม</li>
<li>เก็บเข้าช่อง — เลือกช่องว่างตามกลยุทธ์</li>
<li>หยิบ — หาพาเลทของสินค้าที่สั่ง แล้วส่งออก</li>
<li>สั่งซื้อ — สต็อก ≤ ROP → สั่ง EOQ และบันทึก <code>StockLog</code></li>
</ul>""",
    """<p><strong>ผู้เรียนต้องรู้แค่ไหน</strong></p>
<ul>
<li>เขียน Method สั้น ๆ 5–10 บรรทัดตามบทเรียน ไม่ต้องเป็นโปรแกรมเมอร์</li>
<li>ภาษา SimTalk: <code>if</code> · <code>for</code> · <code>ตาราง[คอลัมน์, แถว]</code></li>
<li>Method ยาว ๆ ของรถอัตโนมัติมีให้ในไฟล์พร้อมใช้ เปิดอ่านได้</li>
<li>ผู้ช่วย AI ช่วยอธิบายหรือแก้ Method ได้</li>
</ul>"""
)}
<div class="note"><strong>หลักการ:</strong> Method = กฎการทำงาน เขียนสั้นเท่าที่จำเป็น และทดสอบทุกครั้งที่แก้</div>

<h3>แสดงข้อมูลสินค้าคงคลัง: ให้คนดูเข้าใจทันที</h3>
<table>
<tr><th>แบบ</th><th>แสดงอะไร</th><th>ใช้ทำอะไร</th></tr>
<tr><td>กราฟ (Chart)</td><td>ระดับสต็อกตามเวลา (ฟันเลื่อย) · utilization ของคน / รถ</td><td>ตรวจว่าแบบจำลองทำงานถูก</td></tr>
<tr><td>ตาราง (<code>StockLog</code>)</td><td>บันทึกทุกครั้งที่ของเข้า–ออก</td><td>นำออกไป Excel วิเคราะห์ต่อ หรือใช้สอน AI</td></tr>
<tr><td>ตัวเลขบนหน้าจอ</td><td>สต็อกปัจจุบันต่อรหัส · ของขาด · กระดาน KPI</td><td>เห็นระหว่างรัน</td></tr>
<tr><td>สีใน 3D</td><td>ชั้นวางเปลี่ยนสีตามสินค้า / ABC</td><td>เห็นช่องว่าง ช่องเต็ม ผู้บริหารเข้าใจเร็ว</td></tr>
</table>
<p>เลือกแบบที่เหมาะกับคนดู: ทีมงานดูตาราง ผู้บริหารดูกราฟและภาพ</p>

<h2>3. AS/RS · 3D · ตรวจแบบจำลอง</h2>

<h3>AS/RS ด้วย Library HBW</h3>
{side_by_side(
    screenshot("assets/images/simulation/05-01.jpg", "โมเดล 3 มิติของ AS/RS พร้อมเครนและสายพานเข้า–ออก",
               caption="โมเดล 3 มิติของ AS/RS ที่ทำไว้สำหรับหลักสูตร"),
    """<p><strong>ส่วนประกอบใน Library HBW</strong></p>
<ul>
<li><strong>RackLane</strong> — ชั้นวางสูงพร้อมเครน สยามพาร์ท 150 ช่อง (15 คอลัมน์ × 5 ชั้น × 2 ด้าน)</li>
<li><strong>เครน (RSU / Stacker Crane)</strong> — วิ่งเก็บและหยิบเอง ตั้งความเร็วแกน X / Z</li>
<li><strong>WMS ของ AS/RS</strong> — เลือกช่องเก็บแบบ One by one · Random · XYZ (โซนตามสินค้า)</li>
<li>สั่งนำออกตามออเดอร์ · I/O conveyor หน้าชั้นวาง</li>
</ul>"""
)}
<p>ในแบบจำลองสยามพาร์ท เครนทำงานแค่ประมาณ 12 % ของเวลา เพราะงานวันละ 120 รอบน้อยมากสำหรับเครน เปลี่ยนกลยุทธ์จัดเก็บจึงแทบไม่มีผล
ประโยชน์จริงที่นี่คือคนไม่ต้องหยิบ จึงลดพนักงานได้ 1 คน — ฝึก Library HBW ในบท <a href="simulation-02.html">2.2</a> และ <a href="simulation-03.html">2.3</a></p>
<div class="note"><strong>หาคอขวดก่อน:</strong> ปรับจุดที่ไม่ใช่คอขวดไม่ได้อะไร</div>

<h3>ชั้นวางแต่ละแบบ สร้างเป็น Object อะไรใน Plant Simulation</h3>
<table>
<tr><th>ชั้นวาง</th><th>Object</th><th>การหยิบ</th><th>เรื่องที่แบบจำลองแสดงได้</th></tr>
<tr><td>Selective</td><td>Store (X = bay, Y = ชั้น)</td><td>หยิบได้ทุกพาเลท</td><td>พื้นฐาน · ทางรถ 3.5 ม.</td></tr>
<tr><td>VNA</td><td>Store + รถ VNA</td><td>หยิบได้ทุกพาเลท</td><td>ทางแคบ ช่องมาก รถช้าลง</td></tr>
<tr><td>Mobile</td><td>Store + เวลาเปิดทางเดิน</td><td>ต้องรอเปิดทาง</td><td>จุมาก แต่หยิบได้ช้า</td></tr>
<tr><td>Drive-in / Push-Back</td><td>Buffer แบบ Stack</td><td>LIFO</td><td>1 ช่อง = 1 รหัส · ช่องว่างใช้ไม่ได้</td></tr>
<tr><td>Shuttle</td><td>Buffer Stack / Queue + รถ shuttle</td><td>LIFO หรือ FIFO</td><td>รถในช่องเป็นคอขวดไหม</td></tr>
<tr><td>Pallet Flow</td><td>Buffer แบบ Queue + เวลาไหล</td><td>FIFO</td><td>ของมีวันหมดอายุ</td></tr>
<tr><td>AS/RS</td><td>Library HBW: RackLane + WMS</td><td>หยิบได้ทุกพาเลท</td><td>เครน · กลยุทธ์จัดเก็บ</td></tr>
</table>

<h3>Advanced 3D Animation: จากโมเดล CAD สู่ภาพเคลื่อนไหว</h3>
{screenshot("assets/images/simulation/05-02.jpg", "โมเดล CAD ของชั้นวาง 4 แบบสำหรับทำ 3D Animation",
            caption="1 Selective Rack นำเข้าจาก CAD (STEP) เป็นกราฟิก 3D ของ Store · 2 AS/RS + I/O เครนและสายพานขยับตามแบบจำลอง · 3 รถในช่องทาง เห็นรถรอกันในทางแคบ · 4 ชิ้นส่วนที่ขยับได้ งา / shuttle มีแกนเคลื่อนที่")}
{step_list([
    "ส่งออกจาก CAD เป็นไฟล์ STEP เป็นชุดเล็ก ๆ เช่น ชั้นวาง 1 bay",
    "นำเข้าเป็นกราฟิก 3D ของ Object ใน Plant Simulation",
    "ชิ้นที่ต้องขยับ เช่น เครนหรืองา ตั้งเป็นชิ้นที่มีแกนเคลื่อนที่",
    "ตั้งมุมกล้อง ทางกล้อง แล้วบันทึกวิดีโอ",
])}
<div class="note"><strong>ระวัง:</strong> อย่านำเข้าทั้งฉากใหญ่ทีเดียว แบบจำลองจะช้ามาก — ฝึกกับ Selective และ AS/RS ในบท <a href="simulation-08.html">2.8</a></div>

<h3>ตรวจแบบจำลองก่อนเชื่อ: Verification และ Validation</h3>
<table>
<tr><th>Verification · สร้างถูกไหม</th><th>Validation · ถูกโมเดลไหม</th></tr>
<tr><td>
<ul>
<li>ดูพาเลทวิ่งถูกทางในภาพ 3D</li>
<li>ตรวจสมดุล: รับเข้า = ส่งออก + สต็อกที่เพิ่ม</li>
<li>ลองค่าสุดโต่ง เช่น รถ 0 คัน ต้องส่งไม่ได้</li>
<li>สยามพาร์ท: สต็อกเริ่ม 100 จบ 100 ✔</li>
</ul></td>
<td>
<ul>
<li>เทียบ KPI กับข้อมูลที่วัดจากหน้างาน</li>
<li>ต่างไม่เกิน ±10 % จึงใช้ตัดสินใจได้</li>
<li>ตัวอย่าง: lead time −7 % · คน −5 % · รถ −7 % ✔</li>
<li>ถ้าต่างมาก: กลับไปดูข้อมูลหรือกฎที่ขาด</li>
</ul></td></tr>
</table>
<div class="note"><strong>กรณีศึกษา (สมมติ) บริษัท ฎ.:</strong> ใช้แบบจำลองที่ไม่เคยเทียบกับข้อมูลจริง จึงซื้อเครื่องเกินจำเป็น
— แบบจำลองที่ไม่ได้ตรวจ อันตรายกว่าไม่มีแบบจำลอง</div>
'''
