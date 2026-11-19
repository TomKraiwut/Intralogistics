# -*- coding: utf-8 -*-
"""Generator for the Intralogistics tutorial site (same engine as the PlantSimulation site).
All body/nav content is authored using flat filenames (e.g. "simulation-02.html") as href
targets -- write() below relocates every page into its section folder (simulation/02.html, ...)
and rewrites every href/src that points at a known flat filename to the correct relative path
for the new location. Chapter bodies never need to know their own folder depth.

Course: DSD course "ระบบการจัดการคลังสินค้าอัตโนมัติ (INTRALOGISTICS)", 18 h,
Plant Simulation 2504. Sections = the subjects of the course document, in teaching order (user 2026-11-18:
doc subjects 1 -> 3 -> 4 -> 2 -> 5, numbered 1-5 by menu position, no "วิชา" word and no codes on the site);
chapters follow the teaching units of course_plan_TH.md.
"""
import hashlib
import os
import re
import posixpath

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SITE_NAME = "Intralogistics with Plant Simulation"
PTS_VERSION = "Plant Simulation 2504"


def _asset_version(relpath):
    """Short content hash appended as ?v=... so browsers (and phones especially) fetch a
    changed style.css / main.js right away instead of keeping a cached copy."""
    with open(os.path.join(ROOT, *relpath.split("/")), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


CSS_HREF = f"assets/style.css?v={_asset_version('assets/style.css')}"
JS_SRC = f"assets/main.js?v={_asset_version('assets/main.js')}"

FONT_LINKS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap">'''

# Course structure. The number shown (1.x, 2.x ...) is the section's position in SECTION_ORDER ("start" = 0).
# "hours" = theory : practice from the course document. Each chapter's content lives in
# tools/chapters/<section>_<NN>.py -- see gen_chapters.py. "kind" per chapter: ท = theory, ป = practice.
SECTIONS = {
    "start": {
        "label": "เริ่มต้น: ติดตั้งโปรแกรม",
        "hub": "start.html",
        "chapters": [
            "ติดตั้ง Plant Simulation 2504",
            "โหลดไฟล์ตัวอย่างของหลักสูตร",
        ],
        "kinds": ["ป", "ป"],
    },
    "logistics": {
        "hours": "1 : 1",
        "label": "หลักการจัดการโลจิสติกส์และซัพพลายเชน",
        "short": "โลจิสติกส์และซัพพลายเชน",
        "hub": "logistics.html",
        "chapters": [
            "โลจิสติกส์ ซัพพลายเชน และการจัดการคลังสินค้า",
            "Factory 51: ระบบสารสนเทศ อุปกรณ์เคลื่อนย้าย และการขนส่ง",
            "สร้างโมเดลแรก: Source → Station → Drain",
            "หาคอขวด (Bottleneck) และแก้ด้วยเครื่องขนาน",
        ],
        "kinds": ["ท", "ป", "ป", "ป"],
    },
    "strategy": {
        "hours": "1 : 1",
        "label": "การจัดการเชิงกลยุทธ์และการตัดสินใจทางวิศวกรรม",
        "short": "กลยุทธ์และการตัดสินใจ",
        "hub": "strategy.html",
        "chapters": [
            "กลยุทธ์ การประเมินการลงทุน และต้นทุนคาร์บอน",
            "ประเมินทางเลือกระบบขนถ่าย และข้อเสนอการลงทุน",
        ],
        "kinds": ["ท", "ป"],
    },
    "simulation": {
        "hours": "2 : 7",
        "label": "สินค้าคงคลังและแบบจำลองเสมือนจริงด้วย Plant Simulation",
        "short": "สินค้าคงคลังและ Plant Simulation",
        "hub": "simulation.html",
        "chapters": [
            "สินค้าคงคลัง และแบบจำลองเสมือนจริง",
            "สร้างคลังสินค้าแรก",
            "ป้อนข้อมูลสินค้าเข้า – ออก, Method และการแสดงข้อมูลสินค้าคงคลัง",
            "คน และกะทำงาน (Workers & Shifts)",
            "ระบบขนถ่ายในคลังสินค้าอัตโนมัติ",
            "Track และ Transporter (AGV)",
            "AMR ด้วย AGVPool และ GAWizard",
            "Advanced 3D Animation",
        ],
        "kinds": ["ท", "ป", "ป", "ป", "ท", "ป", "ป", "ป"],
    },
    "ai": {
        "hours": "1 : 2",
        "label": "วิเคราะห์ข้อมูลจากแบบจำลองด้วย AI",
        "short": "แบบจำลองและ AI",
        "hub": "ai.html",
        "chapters": [
            "แบบจำลอง ข้อมูล และ AI ช่วยตัดสินใจ",
            "นำเข้าข้อมูล และจำลองสถานการณ์",
            "หาค่าที่เหมาะสม และ AI คาดการณ์",
        ],
        "kinds": ["ท", "ป", "ป"],
    },
    "evaluation": {
        "hours": "1 : 1",
        "label": "การวัดและประเมินผล",
        "short": "การวัดและประเมินผล",
        "hub": "evaluation.html",
        "chapters": [
            "สอบภาคทฤษฎี",
            "สอบภาคปฏิบัติ",
        ],
        "kinds": ["ท", "ป"],
    },
}

# Reading order of the menu and of the prev/next links = the classroom order (course_plan_TH.md).
# Section numbers on the site follow this list, so reordering renumbers every chapter.
SECTION_ORDER = ["start", "logistics", "simulation", "ai", "strategy", "evaluation"]


def section_no(section):
    return SECTION_ORDER.index(section)


def section_title(section):
    """Section name as shown on the site: "1. หลักการจัดการ..." ("start" has no number)."""
    label = SECTIONS[section]["label"]
    return label if section == "start" else f"{section_no(section)}. {label}"

# Model files per chapter, attached to the newest GitHub Release (see DOWNLOAD_BASE). Add a
# "downloads" list (one name or None per chapter) to a section once its .spp files are final.
DOWNLOAD_BASE = "https://github.com/TomKraiwut/Intralogistics/releases/latest/download/"

# Pre-/post-test pages, written by gen_quiz.py. "form" is the Google Form .../viewform link;
# empty = the page says the test is not open yet.
QUIZ_PAGES = {
    "pre-test.html": {"title": "แบบทดสอบก่อนเรียน", "form": ""},
    "post-test.html": {"title": "แบบทดสอบหลังเรียน และแบบประเมิน", "form": ""},
}


def _chapter_stem(idx):
    return f"{idx:02d}" if isinstance(idx, int) else idx


def chapter_filename(section, idx):
    return f"{section}-{_chapter_stem(idx)}.html"


def chapter_numbers(section):
    """Chapter ids of a section in reading order: 1..N."""
    return SECTIONS[section].get("ids") or list(range(1, len(SECTIONS[section]["chapters"]) + 1))


def chapter_title(section, idx):
    return SECTIONS[section]["chapters"][chapter_numbers(section).index(idx)]


def chapter_kind(section, idx):
    """"ท" (theory) or "ป" (practice)."""
    kinds = SECTIONS[section].get("kinds")
    return kinds[chapter_numbers(section).index(idx)] if kinds else ""


def chapter_download(section, idx):
    """File name of the chapter's model download, or None."""
    files = SECTIONS[section].get("downloads")
    return files[chapter_numbers(section).index(idx)] if files else None


def chapter_label(section, idx):
    """Chapter number as shown to readers: <subject>.<chapter>, e.g. "3.2"."""
    return f'{section_no(section)}.{idx}'


def sidebar_html(expand_section=None, active_top=None, active_chapter=None):
    parts = []
    parts.append('      <nav id="menu">')
    parts.append('        <header class="major"><button class="sidebar-close" aria-label="ปิดเมนู">✕</button><h2>เมนู</h2></header>')
    parts.append('        <ul>')
    home_active = ' class="active"' if active_top == "index" else ''
    parts.append(f'          <li{home_active}><a href="index.html">หน้าแรก</a></li>')
    pre_active = ' class="active"' if active_top == "pre-test.html" else ''
    parts.append(f'          <li{pre_active}><a href="pre-test.html">{QUIZ_PAGES["pre-test.html"]["title"]}</a></li>')

    for sec in SECTION_ORDER:
        info = SECTIONS[sec]
        li_classes = ["has-children"]
        if expand_section == sec:
            li_classes.append("expanded")
        if active_top == sec and active_chapter is None:
            li_classes.append("active")
        cls = " ".join(li_classes)
        parts.append(f'          <li class="{cls}">')
        parts.append(f'            <a href="{info["hub"]}">{section_title(sec)}</a>')
        parts.append(f'            <button class="submenu-toggle" aria-label="แสดง/ซ่อนเมนู {sec}">▾</button>')
        parts.append('            <ul class="submenu">')
        for i in chapter_numbers(sec):
            fname = chapter_filename(sec, i)
            li_active = ' class="active"' if (active_top == sec and active_chapter == i) else ''
            parts.append(f'              <li{li_active}><a href="{fname}">{chapter_label(sec, i)} {chapter_title(sec, i)}</a></li>')
        parts.append('            </ul>')
        parts.append('          </li>')

    post_active = ' class="active"' if active_top == "post-test.html" else ''
    parts.append(f'          <li{post_active}><a href="post-test.html">{QUIZ_PAGES["post-test.html"]["title"]}</a></li>')
    parts.append('        </ul>')
    parts.append('      </nav>')
    return "\n".join(parts)


def page_html(title, body, expand_section=None, active_top=None, active_chapter=None):
    sb = sidebar_html(expand_section, active_top, active_chapter)
    return f'''<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {SITE_NAME}</title>
{FONT_LINKS}
<link rel="stylesheet" href="{CSS_HREF}">
</head>
<body>
<div id="wrapper">
  <div id="main">
    <div class="inner">
      <header id="header">
        <a href="index.html" class="logo"><span>{SITE_NAME}</span></a>
        <button class="menu-toggle" aria-label="เปิดเมนู" aria-expanded="false">☰</button>
      </header>

      <main>
{body}
      </main>

      <footer class="site-footer">
        {SITE_NAME} · หลักสูตรระบบการจัดการคลังสินค้าอัตโนมัติ (INTRALOGISTICS)
      </footer>
    </div>
  </div>

  <div id="sidebar">
    <div class="inner">
{sb}
      <footer id="footer"><p class="copyright">{SITE_NAME}</p></footer>
    </div>
  </div>
  <div id="sidebar-overlay"></div>
</div>
<script src="{JS_SRC}"></script>
</body>
</html>
'''


KIND_TEXT = {"ท": "ทฤษฎี", "ป": "ปฏิบัติ"}


def card_html(section, i, desc):
    kind = KIND_TEXT.get(chapter_kind(section, i), "")
    kind_html = f"<strong>{kind}</strong> · " if kind else ""
    return f'''          <a href="{chapter_filename(section, i)}" class="card">
            <div class="icon number">{chapter_label(section, i)}</div>
            <h3>{chapter_title(section, i)}</h3>
            <p>{kind_html}{desc}</p>
          </a>'''


def subject_meta(section):
    """One line with the theory : practice hours from the course document."""
    info = SECTIONS[section]
    if "hours" not in info:
        return ""
    return f'<p class="lead">ทฤษฎี : ปฏิบัติ = {info["hours"]} ชั่วโมง</p>'


def hub_page(section):
    info = SECTIONS[section]
    cards_html = "\n".join(card_html(section, i, HUB_CARD_DESC[section][n])
                           for n, i in enumerate(chapter_numbers(section)))

    idx = SECTION_ORDER.index(section)
    prev_html = '<a href="index.html">← กลับหน้าแรก</a>'
    if idx > 0:
        prev_sec = SECTION_ORDER[idx - 1]
        prev_html = f'<a href="{SECTIONS[prev_sec]["hub"]}">← ก่อนหน้า: {section_title(prev_sec)}</a>'
    first_no = chapter_numbers(section)[0]
    first_chapter = chapter_filename(section, first_no)

    body = f'''        <h1>{section_title(section)}</h1>
        {subject_meta(section)}
        <p style="max-width:46em;">{HUB_INTRO[section]}</p>

        <div class="card-grid">
{cards_html}
        </div>

        <div class="page-nav">
          {prev_html}
          <a href="{first_chapter}">เริ่ม {chapter_label(section, first_no)} {info["chapters"][0]} →</a>
        </div>'''
    return page_html(section_title(section), body, expand_section=section, active_top=section)


# Hub intro per section: the subject's objective in the course document, in site wording.
HUB_INTRO = {
    "start": "ติดตั้ง Plant Simulation 2504 และเตรียมไฟล์ตัวอย่างของหลักสูตรให้พร้อม <strong>ก่อนวันอบรม</strong> "
             "เพื่อให้เวลาในห้องเรียนใช้กับเนื้อหาได้เต็มที่",
    "logistics": "พื้นฐานการจัดการโลจิสติกส์และซัพพลายเชน โดยเน้นที่คลังสินค้า — การจัดการคลัง ระบบสารสนเทศ "
                 "อุปกรณ์เคลื่อนย้าย การขนส่ง ความปลอดภัย และปัญหาของสินค้าคงคลัง แล้วดูของจริงในแบบจำลองคลังสินค้า",
    "strategy": "วิเคราะห์เชิงกลยุทธ์และตัดสินใจลงทุนระบบอัตโนมัติในคลังสินค้า โดยใช้ตัวเลขจากแบบจำลอง — "
                "ต้นทุนตลอดอายุการใช้งาน ระยะเวลาคืนทุน NPV IRR การให้คะแนนหลายเกณฑ์ ความเสี่ยง และต้นทุนคาร์บอน",
    "simulation": "หัวใจของหลักสูตร: คำนวณสินค้าคงคลัง แล้วสร้างแบบจำลองคลังสินค้าใน Plant Simulation 2504 ด้วยตัวเอง "
                  "ตั้งแต่คลังเปล่าจนถึงระบบอัตโนมัติ — คน, Forklift, AGV, AMR, AS/RS (Library HBW) และ 3D Animation",
    "ai": "ใช้แบบจำลองเสมือนจริงเป็นแหล่งข้อมูลให้ AI — นำเข้าและเตรียมข้อมูล จำลองสถานการณ์ หาค่าที่เหมาะสมด้านพื้นที่จัดเก็บ "
          "การจัดวางสินค้า และสินค้าคงคลัง แล้วนำผลมาประกอบการตัดสินใจปรับปรุงคลังสินค้า",
    "evaluation": "ประเมินความรู้และความสามารถทั้งภาคทฤษฎีและภาคปฏิบัติ — ผ่านหลักสูตรเมื่อเวลาเรียนไม่น้อยกว่าร้อยละ 80 "
                  "และผลการประเมินไม่น้อยกว่าร้อยละ 60",
}

HUB_CARD_DESC = {
    "start": [
        "ความต้องการของเครื่อง, License, ดาวน์โหลดและติดตั้ง, เปิดโปรแกรมครั้งแรก และปัญหาที่พบบ่อย",
        "ดาวน์โหลดชุดไฟล์ของหลักสูตร แตกไฟล์ไปโฟลเดอร์ที่ถูกต้อง และเปิดโมเดลแรกเพื่อทดสอบ",
    ],
    "logistics": [
        "โลจิสติกส์และโซ่อุปทาน, การจัดการคลังสินค้า, WMS, อุปกรณ์เคลื่อนย้าย, ความปลอดภัย และปัญหาสินค้าคงคลัง",
        "เดินชมโรงงานตัวอย่าง Factory 51 ที่มากับโปรแกรม: รถรับ–ส่งของ, Forklift, AGV, คลัง HBW พร้อม WMS และสั่งรันด้วย EventController",
        "สร้างโมเดลแรกเอง: วาง Source → Station → Drain ต่อ Connector ตั้งค่า ใส่ Display รัน 1 ชั่วโมง ได้ 359 ชิ้น แล้วบันทึก",
        "ไลน์ 5 สถานี ใส่ Display และ Chart หาคอขวดจากสีของสถานะเครื่อง แล้วเพิ่มเครื่องขนาน (177 → 354 ชิ้น/ชม.)",
    ],
    "strategy": [
        "วิเคราะห์สภาพแวดล้อม, Make or Buy, TCO, คืนทุน, NPV, IRR, หลายเกณฑ์, ความไว และคาร์บอนเครดิต",
        "เทียบทางเลือกระบบขนถ่ายจากผลแบบจำลอง วิเคราะห์ความไว ให้คะแนน และทำข้อเสนอการลงทุนต่อผู้บริหาร",
    ],
    "simulation": [
        "ABC, EOQ, Safety Stock, ROP, การจัดวางสินค้า และ Object ใน Plant Simulation ที่แทนอุปกรณ์จริง",
        "เพิ่ม Library HBW วาด Conveyor วาง RackLane + WMS รัน 8 ชม. หาคอขวด แล้วฝึกแก้ 3 ปัญหา: sensor userSetTarget, RSU 2 m/s, คลังเต็ม",
        "HBW H05–H12: รอบการนำออก สินค้า 2 ชนิด กลยุทธ์จัดเก็บ 4 แบบ Method Init / OrderControl และสถิติ RSU เมื่อเครื่องเสีย",
        "Workplace / WorkerPool / Broker จำนวนคน ความเร็ว กะทำงาน ผัง I กับ U คนขนของ ช่างตั้งเครื่อง และช่างซ่อม (94 → 356 ชิ้น/ชม.)",
        "คน, Forklift, AGV, AMR, AS/RS และ 3D — แต่ละแบบใช้ Object อะไร และวัดผลอะไร",
        "วาด Track วงปิดให้รถ Transporter วิ่ง ใช้ PickAndPlace โหลด / ขนถ่ายชิ้นงานโดยไม่เขียน Method และ TwoLaneTrack รถวิ่งสวน 2 เลน",
        "AMR วิ่งอิสระด้วย AGVPool + Marker สั่งรถด้วย Method หาจำนวนรถที่พอดี แล้วใช้ GAWizard หาเส้นทางที่สั้นที่สุด",
        "จัดผัง 3D นำเข้าชั้นวาง 3D และทำภาพ / วิดีโอสำหรับนำเสนอ",
    ],
    "ai": [
        "แบบจำลองกับการตัดสินใจ การรวบรวมข้อมูล AI วิเคราะห์และคาดการณ์ และเทคนิคหาค่าที่เหมาะสม",
        "นำเข้าข้อมูลออเดอร์จาก Excel ทำความสะอาดข้อมูล และจำลองหลายสถานการณ์ด้วย ExperimentManager",
        "หาค่าที่เหมาะสมด้านพื้นที่จัดเก็บ การจัดวางสินค้า สินค้าคงคลัง และใช้ AI คาดการณ์ผลลัพธ์",
    ],
    "evaluation": [
        "ขอบเขตและรูปแบบการสอบภาคทฤษฎีของทุกหัวข้อ",
        "ขอบเขตและรูปแบบการสอบภาคปฏิบัติด้วยแบบจำลอง Plant Simulation",
    ],
}


def youtube_embed(video_id, title, caption=None):
    """Responsive 16:9 YouTube embed. video_id is just the id (the part after
    watch?v= or youtu.be/), not the full URL. Uses youtube-nocookie.com."""
    cap_html = f'\n<p class="video-caption">{caption}</p>' if caption else ""
    return f'''<div class="video-embed">
  <iframe src="https://www.youtube-nocookie.com/embed/{video_id}" title="{title}"
          loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
</div>{cap_html}'''


def screenshot(img_path, alt, caption=None):
    """img_path is authored as a repo-root-relative path, e.g.
    'assets/images/simulation/02-01.jpg' -- write() rewrites it for the page's
    actual folder depth automatically (see _relocate_links)."""
    cap_html = f'\n  <figcaption>{caption}</figcaption>' if caption else ""
    return f'''<figure class="screenshot">
  <a href="{img_path}" target="_blank" rel="noopener"><img src="{img_path}" alt="{alt}" loading="lazy"></a>{cap_html}
</figure>'''


def step_list(items):
    """Numbered circular-badge list instead of a plain browser <ol> counter.
    items is a list of HTML strings."""
    lis = "\n".join(
        f'    <li><span class="num">{i}</span><span class="text">{text}</span></li>'
        for i, text in enumerate(items, start=1)
    )
    return f'''<ol class="step-list">
{lis}
  </ol>'''


def side_by_side(left_html, right_html):
    """Two-column layout (image on the left, explanation on the right) -- stacks on narrow screens."""
    return f'''<div class="side-by-side">
  <div>{left_html}</div>
  <div>{right_html}</div>
</div>'''


def _build_old_to_new():
    mapping = {
        "index.html": "index.html",
        "pre-test.html": "pre-test.html",
        "post-test.html": "post-test.html",
        "assets/style.css": "assets/style.css",
        "assets/main.js": "assets/main.js",
    }
    for sec in SECTION_ORDER:
        info = SECTIONS[sec]
        mapping[info["hub"]] = f"{sec}/index.html"
        for i in chapter_numbers(sec):
            mapping[chapter_filename(sec, i)] = f"{sec}/{_chapter_stem(i)}.html"
    return mapping


OLD_TO_NEW = _build_old_to_new()
_LINK_RE = re.compile(r'(href|src)="([^"]+)"')


def _relocate_links(html, new_relpath):
    cur_dir = posixpath.dirname(new_relpath) or "."

    def repl(m):
        attr, target = m.group(1), m.group(2)
        new_target = OLD_TO_NEW.get(target)
        if new_target is None:
            # assets/* always live at the repo root, whatever folder the page is in
            if target.startswith("assets/"):
                new_target = target
            else:
                return m.group(0)
        rel = posixpath.relpath(new_target, start=cur_dir)
        return f'{attr}="{rel}"'

    return _LINK_RE.sub(repl, html)


def write(relpath, content):
    new_relpath = OLD_TO_NEW.get(relpath, relpath)
    content = _relocate_links(content, new_relpath)
    path = os.path.join(ROOT, *new_relpath.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", new_relpath)


if __name__ == "__main__":
    for sec in SECTION_ORDER:
        write(SECTIONS[sec]["hub"], hub_page(sec))
