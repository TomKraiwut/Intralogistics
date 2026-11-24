# -*- coding: utf-8 -*-
"""ai 3 (practice): หาค่าที่เหมาะสม และ AI คาดการณ์ -- user 2026-11-24: step by step on the example
01_Training_Model\\2504_AI\\3_3_GA_NeuralNet.spp (frames GA_Slotting, NN_Predict; built by build_ai.py, PtS 2504).
Screens captured on PtS 2504 (scratchpad ai\\cap_ai.py + crop_ai.py). GA numbers from check_ai.py and the captured run
(17,892 m = the true optimum); NN predictions from check_ai.py (two runs gave identical values on 2504)."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "ตั้งโจทย์จัดวางสินค้า (Slotting) ให้ GAWizard สลับลำดับสินค้าเพื่อลดระยะเดินได้",
    "อ่านผล GA: ค่าที่ดีที่สุด ลำดับสินค้า และเทียบกับลำดับเดิมได้",
    "สอน NeuralNet จากผล ExperimentManager และใช้ทำนายชุดที่ไม่ได้รันได้",
    "บอกได้ว่าเมื่อไรควรเชื่อผลทำนายของ AI และเมื่อไรต้องรันแบบจำลองยืนยัน",
]

PREDICT = '''<pre><code>var x : table[real]
x.create
x[1,1] := 3        -- Forklift 3 คัน
x[1,2] := 195      -- ยกพาเลทละ 195 วินาที
var y := NeuralNet.getOutput(x)
print y[1,1]       -- ทำนาย Rack.StatNumIn
print y[1,2]       -- ทำนาย LeadTimeMin</code></pre>'''

BODY = f'''
<p class="lead" style="max-width:46em;">บทนี้มี 2 โจทย์ในไฟล์เดียว: <strong>(ก) GAWizard</strong> หาลำดับวางสินค้า 10 ตัวในช่อง 10 ช่อง
ให้คนหยิบเดินน้อยที่สุด และ <strong>(ข) NeuralNet</strong> เรียนจากผลการทดลอง 25 ชุด แล้วทำนายผลของชุดที่ไม่ได้รัน
— สองเครื่องมือนี้คือ "หาค่าที่ดีที่สุด" และ "AI คาดการณ์" ที่เล่าไว้ในบท <a href="ai-01.html">3.1</a></p>

<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 · ไฟล์ <code>3_3_GA_NeuralNet.spp</code> ในโฟลเดอร์ <code>2504_AI</code>
ของ<a href="start-02.html">ไฟล์ตัวอย่าง</a> (2 เฟรม: <code>GA_Slotting</code> และ <code>NN_Predict</code>) · พื้นฐาน ExperimentManager จากบท
<a href="ai-02.html">3.2</a>
</div>

<h2>ภาพรวม</h2>
<table>
<tr><th>ขั้นที่</th><th>เรื่อง</th><th>ได้อะไร</th></tr>
<tr><td>1</td><td>(ก) โจทย์จัดวางสินค้า</td><td>Products, Slots, CalcWalk — ลำดับเดิมเดิน 26,292 ม./วัน</td></tr>
<tr><td>2</td><td>(ก) ตั้งค่า GAWizard</td><td>สลับลำดับแถว Products, ยิ่งเดินน้อยยิ่งดี</td></tr>
<tr><td>3</td><td>(ก) รัน GA และอ่านผล</td><td>17,892 ม./วัน (ลด 32 %)</td></tr>
<tr><td>4</td><td>(ข) ข้อมูลสอน AI</td><td>ExperimentManager 25 ชุด</td></tr>
<tr><td>5</td><td>(ข) สอน NeuralNet</td><td>Training 3,000 รอบ</td></tr>
<tr><td>6</td><td>(ข) ทำนายและตรวจ</td><td>เทียบผลทำนายกับการรันจริง</td></tr>
</table>

<h2>ขั้นที่ 1 (ก): โจทย์จัดวางสินค้า</h2>
{screenshot("assets/images/ai/03-01.jpg", "เฟรม GA_Slotting: Products, Slots, Walk, GAWizard, CalcWalk")}
{side_by_side(
    screenshot("assets/images/ai/03-02.jpg", "Products: สินค้า P01–P10 และจำนวนหยิบต่อวัน"),
    screenshot("assets/images/ai/03-03.jpg", "Slots: ช่อง S01–S10 ระยะจากท่า 5–32 ม."))}
{step_list([
    "เปิดเฟรม <code>Models › GA_Slotting</code> — ไม่มีการไหลของงาน มีแต่ตารางกับ Method คิดระยะทาง",
    "<code>Products</code>: สินค้า 10 ตัว + <code>Picks</code> = จำนวนครั้งที่หยิบต่อวัน (P04 หยิบบ่อยสุด 200 ครั้ง, P05 น้อยสุด 8 ครั้ง)",
    "<code>Slots</code>: ช่องเก็บ 10 ช่อง + <code>Distance</code> = ระยะจากท่า (S01 ใกล้สุด 5 ม. ไกลขึ้นช่องละ 3 ม.)",
    "กติกา: <strong>สินค้าแถวที่ i อยู่ช่องที่ i</strong> — สลับลำดับแถว Products = ย้ายสินค้าไปช่องอื่น",
    "คอลัมน์ <code>Orig</code> และ <code>Chrom</code> ใน Products GAWizard เพิ่มให้เอง (ใช้จำลำดับเดิมและลำดับที่กำลังลอง) ไม่ต้องแก้",
])}
{screenshot("assets/images/ai/03-04.jpg", "Method CalcWalk: ระยะเดินต่อวัน = Picks × 2 × Distance รวมทุกแถว")}
<p><code>CalcWalk</code> คิดระยะเดินต่อวัน: คนหยิบเดิน ท่า → ช่อง → ท่า = 2 × ระยะ ทุกครั้งที่หยิบ รวมทุกสินค้า แล้วเก็บใน Variable <code>Walk</code>
· ลำดับเดิม (P01 ที่ S01, P02 ที่ S02, …) = <strong>26,292 ม./วัน</strong></p>
<div class="note"><strong>SimTalk ไม่สนตัวพิมพ์เล็ก-ใหญ่:</strong> ตัวแปรในโค้ดชื่อ <code>walk</code> กับ Variable <code>Walk</code> คือชื่อเดียวกัน —
ถ้าตั้งชื่อซ้ำ ค่าจะไม่ไปถึง Variable (ในไฟล์จึงใช้ชื่อ <code>dist</code>)</div>

<h2>ขั้นที่ 2 (ก): ตั้งค่า GAWizard</h2>
{screenshot("assets/images/ai/03-05.jpg", "GAWizard แท็บ Define และแท็บ Evaluate")}
{step_list([
    "ดับเบิลคลิก <code>GAWizard</code> — หน้าต่าง <strong>Genetic Algorithms</strong>",
    "แท็บ <code>Define</code>: Optimization direction = <strong>Minimum</strong> (ระยะเดินยิ่งน้อยยิ่งดี)",
    "Number of generations = 20 · Size of generation = 20 (ตั้งไว้แล้ว)",
    "<code>Optimization parameter › Open</code>: ตารางโจทย์ใส่ <code>root.Products</code> = ให้ GA สลับลำดับแถวของตารางนี้ (โจทย์แบบลำดับ / Sequence)",
    "<code>Fitness calculation › by table › Open</code>: ค่าที่ใช้ตัดสิน = <code>root.CalcWalk</code>",
])}
<div class="tip"><strong>ทำไมต้องใช้ GA:</strong> สินค้า 10 ตัวจัดได้ 10! = 3,628,800 แบบ ลองทุกแบบไม่ไหว — GA ลองเพียงหลักร้อยแบบ
โดยเก็บลำดับที่ดีไว้ผสมกันและสุ่มสลับ (Mutation) ทีละรุ่น จนได้คำตอบที่ดีมากในเวลาไม่ถึงวินาที</div>

<h2>ขั้นที่ 3 (ก): รัน GA และอ่านผล</h2>
{step_list([
    "แท็บ <code>Run</code> › <code>Reset</code> › <code>Start</code> — GA ลอง 780 แบบ ใช้เวลาไม่ถึง 1 วินาที",
    "แท็บ <code>Evaluate</code> › <code>Best individuals › Show</code> — ตารางคำตอบที่ดีที่สุด 5 อันดับ",
    "คอลัมน์ <code>Fitness</code> = ระยะเดินต่อวัน · <code>Chromosomes</code> = ลำดับสินค้าของคำตอบนั้น",
])}
{screenshot("assets/images/ai/03-06.jpg", "ตาราง Best individuals: อันดับ 1 Fitness 17,892")}
<table>
<tr><th></th><th>ลำดับในช่อง S01 → S10</th><th>ระยะเดิน (ม./วัน)</th></tr>
<tr><td>ลำดับเดิม</td><td>P01 P02 P03 P04 P05 P06 P07 P08 P09 P10</td><td>26,292</td></tr>
<tr><td><strong>GA อันดับ 1</strong></td><td><strong>P04 P08 P01 P06 P03 P10 P07 P09 P02 P05</strong></td><td><strong>17,892 (−32 %)</strong></td></tr>
</table>
<p>GA วางสินค้าที่หยิบบ่อยไว้ใกล้ท่า (P04 200 ครั้ง → S01, P08 150 ครั้ง → S02, …) — โจทย์นี้ตรวจคำตอบได้ด้วยมือ
(เรียงตามจำนวนหยิบจากมากไปน้อย) และ 17,892 ม. คือค่าที่ดีที่สุดจริง · หลักนี้เรียกว่า <strong>ABC / Velocity Slotting</strong></p>
<div class="tip"><strong>ลองเอง:</strong> (1) ลด Number of generations เหลือ 3 แล้วรันใหม่ — ยังได้ 17,892 ไหม
(2) แก้ Picks ของ P05 เป็น 300 แล้วรัน GA ใหม่ — P05 ย้ายไปช่องไหน</div>

<h2>ขั้นที่ 4 (ข): ข้อมูลสอน AI — ExperimentManager 25 ชุด</h2>
{screenshot("assets/images/ai/03-07.jpg", "เฟรม NN_Predict: Inbound → Dock → Putaway → Rack, ExperimentManager, NeuralNet, LeadTimeMin")}
{step_list([
    "เปิดเฟรม <code>Models › NN_Predict</code> — แบบเดียวกับบท 3.2 แต่รถเข้าสม่ำเสมอ 1 พาเลททุก 2 นาที (30 พาเลท/ชม.)",
    "ExperimentManager ตั้งไว้ 25 ชุด: Forklift (<code>Putaway.XDim</code>) 1–5 คัน × เวลายก (<code>Putaway.ProcTime</code>) 3:00, 3:30, 4:00, 4:30, 5:00 นาที · ชุดละ 1 รอบ",
    "ค่าผลตอบ: <code>Rack.StatNumIn</code> (ขึ้นชั้นใน 8 ชม.) และ <code>LeadTimeMin</code>",
    "ดับเบิลคลิก <code>ExperimentManager</code> › <code>Reset</code> › <code>Start</code> — ขึ้น Current experiment 25/25",
])}
{side_by_side(
    screenshot("assets/images/ai/03-08.jpg", "หน้าต่าง Experiments ก่อนและหลังรัน 25/25"),
    screenshot("assets/images/ai/03-09.jpg", "ตาราง Results 25 ชุด"))}
<p>ตัวอย่างจากตาราง: Forklift 1 คันได้ 86–144 พาเลท · 2 คัน 172–235 · 3 คันขึ้นไปได้ 231–239 พาเลท (ใกล้จำนวนที่เข้ามาทั้งหมด)</p>

<h2>ขั้นที่ 5 (ข): สอน NeuralNet</h2>
{screenshot("assets/images/ai/03-10.jpg", "NeuralNet แท็บ Input, Training (3000 รอบ, Best mean error 9.967 %) และ Forecast")}
{step_list([
    "<strong>ลาก</strong> <code>ExperimentManager</code> ไปวางบน <code>NeuralNet</code> — NeuralNet นำเข้า Input 2 ตัว และ Output 2 ตัวจากผล 25 ชุด",
    "ดับเบิลคลิก <code>NeuralNet</code> › แท็บ <code>Input</code>: Data source = <strong>ExperimentManager</strong>",
    "แท็บ <code>Training</code>: Number of training steps = <strong>3000</strong> (ตั้งไว้แล้ว) › <code>Start</code> — ใช้เวลาประมาณ 10 วินาที",
    "ดู <code>Best mean error</code> (ในภาพ 9.967 %) และ <code>Training quality › Show</code>",
    "แท็บ <code>Forecast</code>: <code>As a table / As a chart › Show</code> เทียบค่าจริงกับค่าที่ NeuralNet ทำนาย",
])}
<div class="note"><strong>รอบสอนน้อยไปทำนายไม่ได้:</strong> ค่าเริ่มต้น 100 รอบยังทำนายคลาดมาก — ตั้ง Training steps ≥ 3,000
(ทดสอบบน 2504 กับอีกแบบจำลองหนึ่ง: 100 รอบคลาด 7–11 %, 3,000 รอบคลาด 1–3 %) · ถ้าเปลี่ยน Training steps หรือข้อมูลใน ExperimentManager ค่าที่ทำนายจะเปลี่ยนตาม</div>

<h2>ขั้นที่ 6 (ข): ทำนายชุดที่ไม่ได้รัน แล้วตรวจด้วยการรันจริง</h2>
<p>เราให้ NeuralNet ทำนาย 3 ชุดที่ไม่มีในตาราง (เวลายกไม่ตรงกับ 25 ชุด) แล้วแก้ค่าใน <code>Putaway</code> รันจริง 8 ชม. เทียบ:</p>
<table>
<tr><th>Forklift / เวลายก</th><th>พาเลท: AI ทำนาย</th><th>พาเลท: รันจริง</th><th>เวลาเฉลี่ย: AI</th><th>เวลาเฉลี่ย: จริง</th></tr>
<tr><td>2 คัน / 225 วินาที</td><td>218</td><td>228</td><td>24.1 นาที</td><td>15.4 นาที</td></tr>
<tr><td>3 คัน / 195 วินาที</td><td>242</td><td>239</td><td>1.3 นาที</td><td>5.1 นาที</td></tr>
<tr><td>4 คัน / 285 วินาที</td><td>239</td><td>238</td><td>5.4 นาที</td><td>6.8 นาที</td></tr>
</table>
<p>จำนวนพาเลท AI ทำนายคลาดเพียง 1–4 % แต่<strong>เวลาเฉลี่ยคลาดมาก</strong> — เวลารอเปลี่ยนแบบกระโดดเมื่อใกล้คอขวด
(2 คันเริ่มยกไม่ทัน) และ 25 ชุดยังน้อยเกินจะเรียนรูปแบบนี้ได้</p>
<div class="tip"><strong>สรุปการใช้ AI กับแบบจำลอง:</strong> NeuralNet ตอบทันทีเหมาะกับการกรองตัวเลือกจำนวนมาก
แต่<strong>ก่อนตัดสินใจจริงต้องรันแบบจำลองยืนยันเสมอ</strong> โดยเฉพาะค่าที่ใกล้คอขวด</div>
<p>ทำนายด้วยโค้ด (Method ในเฟรม NN_Predict) — ลำดับ Input / Output เหมือนใน ExperimentManager:</p>
{PREDICT}
'''
