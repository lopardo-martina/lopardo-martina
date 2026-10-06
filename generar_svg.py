import os
OUT = "/mnt/user-data/outputs/lopardomartina"
A = OUT + "/assets"
os.makedirs(A, exist_ok=True)
for f in os.listdir(A): os.remove(os.path.join(A, f))

T = {
 "dark": dict(txt="#ffffff", txt2="#a1a1aa", card="#14141c", card2="#191923", border="rgba(167,139,250,0.22)",
              acc="#a78bfa", acc2="#c4b5fd", strong="#8b5cf6", kw="#c084fc", fn="#7dd3fc", st="#fdba74",
              slf="#f9a8d4", num="#52525b", btntxt="#ffffff", green="#22c55e", pill="rgba(167,139,250,0.08)"),
 "light": dict(txt="#0a0a0a", txt2="#64748b", card="#eeedf5", card2="#ffffff", border="rgba(91,62,145,0.22)",
              acc="#6d28d9", acc2="#8b5cf6", strong="#6d28d9", kw="#7e22ce", fn="#0369a1", st="#c2410c",
              slf="#be185d", num="#a1a1aa", btntxt="#ffffff", green="#16a34a", pill="rgba(91,62,145,0.06)"),
}
SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, Menlo, 'DejaVu Sans Mono', monospace"

def svg(w, h, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}">\n{body}\n</svg>\n')

def save(name, mode, content):
    open(f"{A}/{name}-{mode}.svg", "w", encoding="utf-8").write(content)

# ---------- HERO ----------
def hero(c):
    b = []
    b.append(f'<rect x="1" y="10" width="318" height="30" rx="15" fill="{c["pill"]}" stroke="{c["border"]}"/>')
    b.append(f'<circle cx="20" cy="25" r="4.5" fill="{c["green"]}"/>')
    b.append(f'<text x="34" y="29.5" font-family="{MONO}" font-size="11.5" letter-spacing="1" fill="{c["acc"]}">ABIERTA A OPORTUNIDADES LABORALES</text>')
    for i, (t, col) in enumerate([("Automatizo", c["txt"]), ("procesos y", c["txt"]), ("construyo web.", c["acc"])]):
        b.append(f'<text x="0" y="{112+i*62}" font-family="{SANS}" font-size="58" font-weight="800" letter-spacing="-2.5" fill="{col}">{t}</text>')
    S = lambda s: f'<tspan font-weight="700" fill="{c["txt"]}">{s}</tspan>'
    lines = [f'Soy Martina Lopardo, desarrolladora {S("Python")}',
             f'especializada en {S("automatización RPA")} y en',
             f'{S("desarrollo web")} con React y Next.js.']
    for i, l in enumerate(lines):
        b.append(f'<text x="0" y="{318+i*30}" font-family="{SANS}" font-size="17.5" fill="{c["txt2"]}">{l}</text>')
    # code window
    X, Y, W, H = 505, 18, 440, 400
    b.append(f'<rect x="{X}" y="{Y}" width="{W}" height="{H}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>')
    for i, col in enumerate(["#ef4444", "#eab308", "#22c55e"]):
        b.append(f'<circle cx="{X+22+i*16}" cy="{Y+22}" r="5" fill="{col}"/>')
    b.append(f'<text x="{X+W/2}" y="{Y+26}" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{c["txt2"]}">~/lopardomartina/perfil.py</text>')
    b.append(f'<text x="{X+W-20}" y="{Y+26}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["txt2"]}">&gt;_</text>')
    b.append(f'<line x1="{X}" y1="{Y+44}" x2="{X+W}" y2="{Y+44}" stroke="{c["border"]}"/>')
    k, f, s, sl, t = c["kw"], c["fn"], c["st"], c["slf"], c["txt"]
    code = [
      [(k,"class "),(f,"Martina"),(t,":")],
      [(k,"    def "),(f,"__init__"),(t,"("),(sl,"self"),(t,"):")],
      [(sl,"        self"),(t,".rol = "),(s,'"Python Developer"')],
      [(sl,"        self"),(t,".stack = [")],
      [(s,'            "python"'),(t,",")],
      [(s,'            "rpa"'),(t,",")],
      [(s,'            "web"'),(t,",")],
      [(t,"        ]")],
      [],
      [(k,"    def "),(f,"aprender"),(t,"("),(sl,"self"),(t,", tema):")],
      [(k,"        return "),(s,'f"{tema} ✓"')],
      [],
    ]
    for i, line in enumerate(code):
        y = Y + 80 + i * 24
        b.append(f'<text x="{X+20}" y="{y}" font-family="{MONO}" font-size="12.5" fill="{c["num"]}">{i+1:02d}</text>')
        if line:
            spans = "".join(f'<tspan fill="{col}">{txt.replace(chr(38),"&amp;")}</tspan>' for col, txt in line)
            b.append(f'<text x="{X+56}" y="{y}" font-family="{MONO}" font-size="13" xml:space="preserve">{spans}</text>')
    b.append(f'<rect x="{X+56}" y="{Y+80+11*24-14}" width="9" height="17" fill="{c["acc2"]}"/>')
    b.append(f'<line x1="{X}" y1="{Y+H-38}" x2="{X+W}" y2="{Y+H-38}" stroke="{c["border"]}"/>')
    b.append(f'<circle cx="{X+22}" cy="{Y+H-19}" r="3.5" fill="{c["green"]}"/>')
    b.append(f'<text x="{X+34}" y="{Y+H-15}" font-family="{MONO}" font-size="11" fill="{c["txt2"]}">main</text>')
    b.append(f'<text x="{X+W-20}" y="{Y+H-15}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{c["txt2"]}">UTF-8 · Python</text>')
    return svg(960, 430, "Martina Lopardo: automatizo procesos y construyo web. Desarrolladora Python especializada en automatización RPA y en desarrollo web con React y Next.js.", "\n".join(b))

# ---------- BOTONES ----------
def btn_portfolio(c):
    return svg(224, 52, "Ver mi portfolio",
      f'<rect x="0" y="0" width="224" height="52" rx="10" fill="{c["strong"]}"/>'
      f'<text x="24" y="31.5" font-family="{SANS}" font-size="16" font-weight="600" fill="{c["btntxt"]}">Ver mi portfolio</text>'
      f'<path d="M186 33 L198 21 M189 21 H198 V30" stroke="{c["btntxt"]}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

def btn_email(c):
    return svg(150, 52, "Escribirme por correo",
      f'<rect x="12" y="18" width="20" height="15" rx="2.5" fill="none" stroke="{c["txt2"]}" stroke-width="1.6"/>'
      f'<path d="M13 20 L22 27 L31 20" fill="none" stroke="{c["txt2"]}" stroke-width="1.6" stroke-linejoin="round"/>'
      f'<text x="44" y="31.5" font-family="{SANS}" font-size="16" fill="{c["txt"]}">Escribirme</text>')

def eyebrow(c, text, y):
    return f'<text x="0" y="{y}" font-family="{MONO}" font-size="12" letter-spacing="1.2" fill="{c["acc"]}">{text}</text>'

# ---------- SOBRE MÍ ----------
def sobre(c):
    b = [eyebrow(c, "01 / SOBRE MÍ", 30)]
    b.append(f'<text x="290" y="48" font-family="{SANS}" font-size="38" font-weight="600" letter-spacing="-1.2" fill="{c["txt"]}">El código vale cuando</text>')
    b.append(f'<text x="290" y="94" font-family="{SANS}" font-size="38" font-weight="600" letter-spacing="-1.2" fill="{c["acc"]}">resuelve algo real.</text>')
    para = ["Estudio Ingeniería en Sistemas de Información en la UTN Facultad",
            "Regional Delta. Aprendo de forma autónoma lo que cada proyecto",
            "necesita y valoro el trabajo en equipo como parte central del desarrollo."]
    for i, l in enumerate(para):
        b.append(f'<text x="290" y="{146+i*30}" font-family="{SANS}" font-size="17" fill="{c["txt2"]}">{l}</text>')
    return svg(960, 240, "Sobre mí: el código vale cuando resuelve algo real. " + " ".join(para), "\n".join(b))

# ---------- LO QUE HAGO ----------
ICONS = {
 "code": 'M8 6 L2 12 L8 18 M16 6 L22 12 L16 18 M14 4 L10 20',
 "nodes": 'M3 3 H10 V10 H3 Z M14 14 H21 V21 H14 Z M10 6.5 H17.5 V14',
 "globe": 'M12 2 A10 10 0 1 0 12.01 2 Z M2 12 H22 M12 2 C15 5 15 19 12 22 C9 19 9 5 12 2',
 "window": 'M3 4 H21 V20 H3 Z M3 9 H21 M6 6.5 H6.01 M9 6.5 H9.01',
}
def hago(c):
    cards = [("code","Python",["Django, APIs REST","y SOAP"]),
             ("nodes","RPA",["Bots con","Robocorp"]),
             ("globe","Web",["React, Next.js","y Node.js"]),
             ("window","Escritorio",["Interfaces con","Tkinter"])]
    b = [eyebrow(c, "02 / LO QUE HAGO", 30)]
    for i, (ic, title, sub) in enumerate(cards):
        x = 290 + i * 166
        b.append(f'<rect x="{x}" y="10" width="154" height="166" rx="12" fill="{c["card"]}" stroke="{c["border"]}"/>')
        b.append(f'<g transform="translate({x+20} 30)"><path d="{ICONS[ic]}" fill="none" stroke="{c["acc"]}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></g>')
        b.append(f'<text x="{x+20}" y="112" font-family="{SANS}" font-size="17" font-weight="600" fill="{c["txt"]}">{title}</text>')
        for j, s in enumerate(sub):
            b.append(f'<text x="{x+20}" y="{138+j*18}" font-family="{SANS}" font-size="13" fill="{c["txt2"]}">{s}</text>')
    label = "Lo que hago: " + "; ".join(f'{t}: {" ".join(s)}' for _, t, s in cards)
    return svg(960, 186, label, "\n".join(b))

# ---------- PROYECTOS ----------
PROYECTOS = [
 ("gabi", "GABI", ["Aplicación de escritorio para orquestar y monitorear bots RPA:",
                    "registro en vivo, control de ejecución y avisos por correo."],
  ["Python", "Tkinter", "RPA"]),
 ("yl-nutricion", "YL-Nutricion", ["DESCRIPCIÓN PENDIENTE"], ["PENDIENTE"]),
 ("vialkids", "VialKids", ["Sitio web interactivo de educación vial para chicos."], ["PENDIENTE"]),
]
def proyecto(c, idx, slug, title, desc, tags):
    first = idx == 0
    off = 40 if first else 0
    b = []
    if first: b.append(eyebrow(c, "03 / PROYECTOS DESTACADOS", 22))
    b.append(f'<line x1="290" y1="{off+4}" x2="950" y2="{off+4}" stroke="{c["border"]}"/>')
    b.append(f'<text x="290" y="{off+46}" font-family="{MONO}" font-size="13" fill="{c["acc"]}">{idx+1:02d}</text>')
    b.append(f'<text x="360" y="{off+54}" font-family="{SANS}" font-size="30" font-weight="600" letter-spacing="-1" fill="{c["txt"]}">{title}</text>')
    for i, l in enumerate(desc):
        b.append(f'<text x="360" y="{off+88+i*24}" font-family="{SANS}" font-size="15.5" fill="{c["txt2"]}">{l}</text>')
    ty = off + 88 + len(desc) * 24 + 8
    x = 360
    for t in tags:
        w = len(t) * 7.4 + 26
        b.append(f'<rect x="{x}" y="{ty}" width="{w}" height="28" rx="14" fill="none" stroke="{c["border"]}"/>')
        b.append(f'<text x="{x+w/2}" y="{ty+18.5}" text-anchor="middle" font-family="{SANS}" font-size="12.5" fill="{c["txt2"]}">{t}</text>')
        x += w + 8
    b.append(f'<circle cx="920" cy="{off+46}" r="24" fill="none" stroke="{c["border"]}"/>')
    b.append(f'<path d="M913 {off+53} L927 {off+39} M917 {off+39} H927 V{off+49}" stroke="{c["txt"]}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    h = ty + 28 + 22
    return svg(960, h, f"Proyecto {title}: {' '.join(desc)} Tecnologías: {', '.join(tags)}.", "\n".join(b))

for mode, c in T.items():
    save("hero", mode, hero(c))
    save("btn-portfolio", mode, btn_portfolio(c))
    save("btn-email", mode, btn_email(c))
    save("sobre-mi", mode, sobre(c))
    save("lo-que-hago", mode, hago(c))
    for i, (slug, t, d, tg) in enumerate(PROYECTOS):
        save(f"proyecto-{slug}", mode, proyecto(c, i, slug, t, d, tg))
print(sorted(os.listdir(A)))
