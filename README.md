# Intralogistics

เว็บไซต์ประกอบหลักสูตร **ระบบการจัดการคลังสินค้าอัตโนมัติ (INTRALOGISTICS)** 18 ชั่วโมง (กรมพัฒนาฝีมือแรงงาน)
บน **Plant Simulation 2504** (ภาษาไทย) — เผยแพร่ผ่าน GitHub Pages
ที่ https://tomkraiwut.github.io/Intralogistics/ (เมื่อเปิด Pages แล้ว)

โครงสร้างและเครื่องมือเหมือนเว็บ [PlantSimulation](https://github.com/TomKraiwut/PlantSimulation)

## โครงสร้างเว็บ

เมนูเรียงตามลำดับสอนในห้อง บทในแต่ละหัวข้อตามหน่วยการสอนใน `course_plan_TH.md`
บนเว็บไม่แสดงคำว่า "วิชา" และไม่แสดงรหัสหลักสูตร / รหัสวิชา

| โฟลเดอร์ | เมนู (ทฤษฎี : ปฏิบัติ ชม.) | บท |
|---|---|---|
| `start/` | เริ่มต้น: ติดตั้งโปรแกรม | 0.1 ติดตั้ง Plant Simulation 2504 · 0.2 โหลดไฟล์ตัวอย่าง |
| `logistics/` | 1. หลักการจัดการโลจิสติกส์และซัพพลายเชน (1 : 1) | 1.1 – 1.2 |
| `simulation/` | 2. สินค้าคงคลังและแบบจำลองเสมือนจริงด้วย Plant Simulation (2 : 7) | 2.1 – 2.8 |
| `ai/` | 3. วิเคราะห์ข้อมูลจากแบบจำลองด้วย AI (1 : 2) | 3.1 – 3.3 |
| `strategy/` | 4. การจัดการเชิงกลยุทธ์และการตัดสินใจทางวิศวกรรม (1 : 1) | 4.1 – 4.2 |
| `evaluation/` | 5. การวัดและประเมินผล (1 : 1) | 5.1 – 5.2 |

ลำดับเมนูตั้งที่ `SECTION_ORDER` ใน `tools/gen_site.py` — เลขหัวข้อ (1., 2. …) และเลขบท (2.1 …) นับจากตำแหน่งในรายการนี้
ชื่อไฟล์เนื้อหา `tools/chapters/<section>_<NN>.py` ไม่เปลี่ยนตามเลข (เช่น บท 2.2 = `simulation_02.py`)

## สร้าง / แก้ไขหน้าเว็บด้วยสคริปต์ (ไม่แก้ไฟล์ .html ตรง ๆ)

- `tools/gen_site.py` — โครงเมนู (`SECTIONS`, `SECTION_ORDER`), คำอธิบายบนการ์ด (`HUB_CARD_DESC`), บทนำของแต่ละวิชา (`HUB_INTRO`),
  ลิงก์แบบทดสอบ (`QUIZ_PAGES`) และเทมเพลต HTML กลาง
- `tools/chapters/<section>_<NN>.py` — เนื้อหาบทละไฟล์: `OBJECTIVES`, `TOPICS` และ `BODY`
  ตอนนี้ทุกบทมีแค่ `OBJECTIVES` + `TOPICS` หน้าเว็บจึงแสดง "หัวข้อในบทนี้" + "กำลังจัดทำ" — เพิ่ม `BODY = f'''...'''` เมื่อเนื้อหาพร้อม
  (ปีกกาจริงในโค้ดต้องเขียน `{{` `}}`)
- `tools/gen_chapters.py` — สร้างหน้าบทและหน้ารวมของแต่ละวิชา · `tools/gen_index.py` — หน้าแรก · `tools/gen_quiz.py` — pre/post-test

ลิงก์ภายในเขียนแบบชื่อแบน เช่น `href="simulation-03.html"` — `write()` แปลงเป็น path จริงให้

```bash
cd tools
python gen_site.py
python gen_chapters.py
python gen_index.py
python gen_quiz.py
```

## รูปภาพ วิดีโอ และไฟล์โมเดล

- รูป: `assets/images/<section>/<NN>-<ลำดับ>.jpg` กว้างไม่เกิน 1600 px ~300 KB ต่อรูป ใส่ด้วย `screenshot()`
- วิดีโอ: อัปโหลด YouTube แล้วใช้ `youtube_embed()` — ห้าม commit `.mp4`
- ไฟล์ `.spp`: แนบใน **GitHub Release** (ไม่อยู่ใน repo) แล้วเพิ่ม `"downloads": [...]` ให้วิชานั้นใน `SECTIONS`
  ปุ่มดาวน์โหลดจะขึ้นเองและชี้ไป release ล่าสุด · **ไม่แนบไฟล์เฉลย / ข้อสอบ**

## เปิดเป็นเว็บ (GitHub Pages)

GitHub Pages ของบัญชีฟรีใช้ได้กับ repo **Public** เท่านั้น → Settings → General → Change visibility → Public
จากนั้น Settings → Pages → Deploy from a branch → `main` / `(root)` → Save

ทดสอบในเครื่อง: `python -m http.server 8000` จากโฟลเดอร์นี้ แล้วเปิด `http://localhost:8000/`
