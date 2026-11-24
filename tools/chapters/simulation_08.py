# -*- coding: utf-8 -*-
"""simulation 8 (practice): 3D Factory and Warehouse -- user 2026-11-24: chapter 2.8 = slides 46-51 of
2606_Step_By_Step\\2504_Plant Simulation_Basic.pptx ("Create 3D Factory"). Images 08-01..06 = those slides exported
1920x1080, cropped to the content area (Confidential footer removed); the Open dialog folder pane (08-03) and the
logo image path (08-04) are blurred. Screens are Plant Simulation 2504 (Open dialog path still shows 2201)."""
from gen_site import screenshot, step_list, side_by_side

TOPICS = []

OBJECTIVES = [
    "สร้างผนังโรงงาน ชั้นวาง ชั้นลอย บันได และรั้ว ด้วย Insert Shape ในหน้าต่าง 3D ได้",
    "ใช้ Graphic Structure แก้ชิ้นส่วน 3D และเปิดดูสิ่งกีดขวาง (Obstacles) ของคนงานได้",
    "นำเข้าไฟล์ 3D (JT, STEP ฯลฯ) และติดรูปภาพบนผนังด้วย Textured Plate ได้",
    "นำเข้าผัง DWG เป็นพื้น ล็อกไม่ให้เลื่อน และปรับให้โปร่งแสงได้",
]

BODY = f'''
<p class="lead" style="max-width:46em;">แบบจำลองจากบทก่อน ๆ ทำงานได้แล้ว บทนี้ทำให้<strong>ดูเหมือนโรงงานและคลังสินค้าจริง</strong>ในหน้าต่าง 3D —
สร้างผนัง ชั้นวาง ชั้นลอย และบันไดด้วยเมาส์ นำเข้าไฟล์ 3D ติดป้ายหรือโลโก้บนผนัง แล้ววางผัง DWG ของโรงงานไว้ใต้แบบจำลอง
ภาพ 3D ที่ดีช่วยให้ผู้บริหารและหน้างานเข้าใจผลจำลองได้ทันที</p>

<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Plant Simulation 2504 · แบบจำลองที่เปิดหน้าต่าง 3D ได้ (เช่น จากบท <a href="simulation-04.html">2.4</a>)
· ไฟล์ผัง DWG ของโรงงาน (ในภาพใช้ <code>2D_Layout.dwg</code>) · รูปภาพโลโก้หรือป้าย (.jpg / .png)
</div>

<h2>ภาพรวม: 6 ขั้น</h2>
<table>
<tr><th>ขั้นที่</th><th>เรื่อง</th><th>ได้อะไร</th></tr>
<tr><td>1</td><td>Create 3D Factory</td><td>ผนังโรงงาน ชั้นวาง ชั้นลอย บันได รั้ว จาก Insert Shape</td></tr>
<tr><td>2</td><td>Edit 3D Structure และ Obstacles</td><td>ลบชิ้นส่วนที่ไม่ต้องการ ดูว่าคนงานเดินผ่านตรงไหนไม่ได้</td></tr>
<tr><td>3</td><td>Import Graphics</td><td>อาคารหรือเครื่องจักรจากไฟล์ 3D</td></tr>
<tr><td>4</td><td>Textured Plate</td><td>โลโก้หรือป้ายติดผนัง</td></tr>
<tr><td>5</td><td>Import DWG</td><td>ผังโรงงาน 2D เป็นพื้น ล็อกไว้ไม่ให้เลื่อน</td></tr>
<tr><td>6</td><td>Set Transparency</td><td>ผังโปร่งแสง มองเห็นแบบจำลองชัดขึ้น</td></tr>
</table>
<div class="tip"><strong>default กับ deco:</strong> ของตกแต่ง 3D ทุกชิ้นอยู่ใน <strong>Graphic group</strong> ของเฟรม —
<code>deco (internal)</code> เก็บในไฟล์ .spp (ผนัง ชั้นวาง ป้าย) ส่วน <code>default (external)</code> ใช้กับไฟล์ที่นำเข้า เช่น ผัง DWG
ดูและแก้ได้ที่ <code>Show Graphic Structure</code></div>

<h2>ขั้นที่ 1: Create 3D Factory — ผนัง ชั้นวาง ชั้นลอย</h2>
{screenshot("assets/images/simulation/08-01.jpg", "Insert Shape แท็บ Edit, หน้าต่าง Create Factory Walls, Graphic Structure และโรงงาน 3D")}
{step_list([
    "เปิดหน้าต่าง 3D ของเฟรม แล้วเลือกแท็บ <code>Edit</code> (กลุ่ม <code>3D</code>)",
    "คลิกลูกศร ▾ ของกลุ่ม <code>Insert Shape</code> เพื่อดูรูปทรงทั้งหมด",
    "เลือก <code>Factory Walls</code> — ในกลุ่มเดียวกันมี <code>Rack</code>, <code>Mezzanine</code> (ชั้นลอย), <code>Stairs</code>, <code>Fence</code>, <code>Barred Area</code> และ <code>Dimensioning</code>",
    "หน้าต่าง <code>Create Factory Walls</code>: Graphic group <code>deco (internal)</code> · Dimension X <strong>25 m</strong>, Y <strong>10 m</strong>, Z <strong>5 m</strong> · Thickness <strong>0.3 m</strong> · เลือกสีผนัง กระจก และกรอบ → <code>Create</code>",
    "คลิกขวาที่<strong>ที่ว่าง</strong>ในหน้าต่าง 3D (ไม่ใช่บนวัตถุ)",
    "เลือก <code>Show Graphic Structure</code>",
    "ใน <code>.Models.Model › deco</code> จะเห็นชิ้นที่สร้าง: [1] Factory Walls, [2] Rack, [3] Mezzanine, [4] Stairs, [5] Fence — กด &gt; เพื่อดูชิ้นย่อย",
    "ผล: โรงงานมีผนังและหน้าต่าง ชั้นวาง ชั้นลอยพร้อมราวกันตก และบันไดขึ้นชั้นลอย",
])}
<div class="tip"><strong>วางแล้วค่อยปรับ:</strong> รูปทรงทุกชิ้นลากย้ายได้ในหน้าต่าง 3D และแก้ขนาดหรือตำแหน่งละเอียดได้ที่
คลิกขวา › <code>Edit 3D Properties...</code> (Ctrl+3)</div>

<h2>ขั้นที่ 2: Edit 3D Structure และ Show Obstacles</h2>
{screenshot("assets/images/simulation/08-02.jpg", "ลบชิ้นราวกันตกใน Graphic Structure และ Obstacles สีแดงในหน้าต่าง 3D")}
{step_list([
    "<strong>ลบชิ้นส่วนย่อย:</strong> ใน Graphic Structure ขยายชิ้นที่ต้องการ (เช่น ราวของ Mezzanine) คลิกขวาที่ชิ้นย่อย (เช่น [14]) › <code>Delete</code> — ใช้เปิดช่องราวตรงที่บันไดขึ้นมาถึงชั้นลอย",
    "<strong>ดูสิ่งกีดขวาง:</strong> แท็บ <code>View</code> › <code>Obstacles</code> (Show Obstacles, ปุ่มลัด O) — พื้นที่สีแดงคือที่คนงานเดินผ่านไม่ได้",
    "หน้าต่าง <code>Worker Walking Heights</code> บอกจำนวนสิ่งกีดขวางแต่ละระดับ — ในภาพ: พื้น 0.00 m มี 10 ชิ้น, ชั้นลอย 2.50 m มี 25 ชิ้น",
])}
<div class="note"><strong>ผนังและชั้นวางเป็นสิ่งกีดขวางของคนงาน:</strong> ในภาพ คนงาน (WorkerPool + Broker แบบบท <a href="simulation-04.html">2.4</a>)
เดินอ้อมผนังและใช้บันไดขึ้นชั้นลอย — ถ้าลบหรือย้ายชิ้น 3D เส้นทางเดินและเวลาเดินจะเปลี่ยนด้วย ตรวจด้วย Obstacles ทุกครั้ง</div>

<h2>ขั้นที่ 3: Import Graphics — นำเข้าไฟล์ 3D</h2>
{screenshot("assets/images/simulation/08-03.jpg", "Import Graphics, หน้าต่าง Open โฟลเดอร์ jt-graphics และรายการชนิดไฟล์ที่รองรับ")}
{step_list([
    "แท็บ <code>Edit</code> › <code>Import Graphics</code>",
    "ไปที่โฟลเดอร์ตัวอย่างของโปรแกรม <code>C:\\Program Files\\Siemens\\Tecnomatix Plant Simulation 2504\\3D\\jt-graphics</code> (ภาพเป็นโฟลเดอร์ของรุ่น 2201 — ใน 2504 มีไฟล์ชุดเดียวกัน)",
    "เลือก <code>Building</code> › <code>Open</code> — ได้อาคารพร้อมเสาและผนังกั้นห้อง",
])}
<p>ชนิดไฟล์ที่นำเข้าได้: JT, Parasolid, IGES, STEP, VRML, STL, CATIA V4 และ CAD Layout (DGN, DWG, DXF) — ไฟล์ STEP จากโปรแกรม CAD ใช้ได้เลย</p>

<h2>ขั้นที่ 4: Textured Plate — ติดโลโก้หรือป้ายบนผนัง</h2>
{screenshot("assets/images/simulation/08-04.jpg", "หน้าต่าง Create Textured Plate และการหมุนแผ่นภาพขึ้นติดผนังด้วย Edit 3D Properties")}
{step_list([
    "แท็บ <code>Edit</code>",
    "<code>Insert Shape</code> › <code>Textured Plate</code> (แผ่นที่มีรูปภาพ)",
    "Graphic Group <code>deco (internal)</code>",
    "Image: คลิกไอคอนโฟลเดอร์ เลือกรูป .jpg / .png ของโลโก้หรือป้าย",
    "Orientation <code>Floor (on XY Plane)</code> · Size X <strong>10 m</strong> · Thickness 0.1 m · Texture: ☑ Use Transparency, ● Fit Texture to Plate",
    "<code>Create</code> — แผ่นภาพวางราบบนพื้น",
    "คลิกขวาที่แผ่นภาพ › <code>Edit 3D Properties...</code>",
    "แท็บ <code>Transformation</code> › Rotation: Angle <strong>90°</strong>, Axis X = 1 → แผ่นตั้งขึ้น แล้วใส่ Position X, Y, Z ให้ชิดผนัง (ในภาพ 14, 21, 4.19 m) → <code>OK</code>",
])}

<h2>ขั้นที่ 5: Import DWG — ผังโรงงานเป็นพื้น</h2>
{screenshot("assets/images/simulation/08-05.jpg", "Import Graphics ไฟล์ 2D_Layout.dwg, หน้าต่าง Insert Layout Graphic และล็อกกลุ่ม default")}
{step_list([
    "แท็บ <code>Edit</code>",
    "<code>Import Graphics</code>",
    "เลือกไฟล์ผัง <code>2D_Layout.dwg</code>",
    "หน้าต่าง <code>Insert Layout Graphic</code>: Graphic group <code>default (external)</code> · Default unit ตามหน่วยที่เขียนแบบไว้ (ในภาพ <code>cm</code>) · Corrective scaling 1",
    "<code>OK</code> — ผังวางเป็นพื้นของเฟรม",
    "คลิกขวาที่ว่าง › <code>Show Graphic Structure</code>",
    "ขยาย <code>Model1</code> จะเห็น <code>default</code> › [1] 2D_Layout",
    "คลิกขวาที่กลุ่ม <code>default</code>",
    "เลือก <code>Locked</code> — ผังจะไม่ขยับเวลาคลิกหรือลากวัตถุที่อยู่บนผัง",
])}
<div class="note"><strong>หน่วยต้องตรงกับแบบ:</strong> ถ้าผังที่นำเข้ามาใหญ่หรือเล็กผิดปกติ 10 หรือ 100 เท่า แปลว่าเลือก Default unit ผิด
(mm / cm / m) — ลบแล้วนำเข้าใหม่ แล้ววัดความยาวผนังที่รู้ขนาดเทียบดู</div>

<h2>ขั้นที่ 6: Set Transparency — ผังโปร่งแสง</h2>
{screenshot("assets/images/simulation/08-06.jpg", "Edit 3D Properties ของ 2D_Layout แท็บ Material ตั้ง Transparency 0.5")}
{step_list([
    "คลิกขวาที่ว่าง › <code>Show Graphic Structure</code>",
    "ขยาย <code>default</code> แล้วเลือก <code>[1] 2D_Layout</code>",
    "คลิกขวา › <code>Edit 3D Properties...</code>",
    "แท็บ <code>Material</code>",
    "☑ <code>Material active</code>",
    "Transparency <strong>0.5</strong> (0 = ทึบ, 1 = ใสหมด)",
    "<code>OK</code> — ผังจางลง วัตถุและรถที่วิ่งบนผังเด่นขึ้น",
])}

<h2>สรุป</h2>
<table>
<tr><th>อยากได้</th><th>ใช้</th></tr>
<tr><td>ผนัง ชั้นวาง ชั้นลอย บันได รั้ว</td><td><code>Edit › Insert Shape</code> (Factory Walls, Rack, Mezzanine, Stairs, Fence)</td></tr>
<tr><td>แก้ / ลบชิ้นย่อย</td><td>คลิกขวาที่ว่าง › <code>Show Graphic Structure</code></td></tr>
<tr><td>รู้ว่าคนงานเดินผ่านตรงไหนไม่ได้</td><td><code>View › Obstacles</code></td></tr>
<tr><td>อาคาร / เครื่องจักรจาก CAD</td><td><code>Edit › Import Graphics</code> (JT, STEP, STL …)</td></tr>
<tr><td>โลโก้ ป้าย</td><td><code>Textured Plate</code> + หมุน 90° รอบแกน X</td></tr>
<tr><td>ผังโรงงาน 2D</td><td><code>Import Graphics</code> ไฟล์ DWG → กลุ่ม <code>default</code> → <code>Locked</code> → Transparency</td></tr>
</table>
'''
