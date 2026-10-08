"""Generate the profile SVG assets (Olimpo Labs look) and README.md.

Usage: python scripts/build_assets.py
"""
import textwrap
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

MARBLE, INK, MUTED = "#f2eee4", "#16130f", "#5e564a"
AEGEAN, GOLD, LINE = "#17406b", "#a98532", "#d6d0c3"
TITLE = "Cinzel, 'Trajan Pro', Georgia, serif"
TEXT = "'Cormorant Garamond', Garamond, Georgia, serif"
LAMBDA = "M56 14 L68 14 L99 102 L112 102 L112 106 L74 106 L74 102 L84 102 L61 36 L33 102 L40 102 L40 106 L16 106 L16 102 L27 102 Z"
USER = "https://github.com/PabloRS98"

T = {
    "en": {
        "eyebrow": "OLIMPO LABS  ·  SOLO-FOUNDER APP STUDIO",
        "tagline": "Zero-friction apps for health, nutrition & personal wealth.",
        "eco_tag": "THE ECOSYSTEM", "eco_title": "Four projects, one idea",
        "eco_lead": "Each one removes manual work from a part of daily life: money, training, food and software development.",
        "os_tag": "OPEN SOURCE", "os_title": "Built in the open",
        "os_lead": "Public repositories from the same workshop.",
        "view": "VIEW ON GITHUB  ↗",
        "email": "EMAIL", "linkedin": "LINKEDIN",
        "projects": [
            ("midas", "I", "Midas", "Live", "Local-first wealth and spending tracker for households. Per-person accounts, XIRR and TWR analytics, Spanish voice entry through Telegram.", GOLD, f"{USER}/finance-tracker"),
            ("icor", "II", "Icor", "Pre-launch", "Strength training as an RPG: XP, quests, rankings and offline-first sync, with around 200 exercises mapped to muscle activation.", "#9c3f2c", None),
            ("hestia", "III", "Hestia", "In design", "Smart pantry and anti-waste kitchen: what is at home, what to cook, what to buy. Market research done, build next.", "#b3722a", None),
            ("agora", "IV", "Ágora", "Internal", "Telegram workspace where AI agents run development tasks per project, with human approval on every merge.", AEGEAN, None),
        ],
        "oss": [
            ("projects-dashboard", "Multi-forge project manager (GitHub, GitLab, Bitbucket) with local scanning and Telegram alerts."),
            ("Content-Media-Manager", "Self-hosted catalog for books, movies, series, games and podcasts. One Docker container, no cloud."),
            ("arquitectura-doble-agente", "Reference architecture for two Hermes agents talking over NATS and Telegram."),
        ],
    },
    "es": {
        "eyebrow": "OLIMPO LABS  ·  ESTUDIO DE APPS DE UNA PERSONA",
        "tagline": "Apps sin fricción para salud, nutrición y patrimonio personal.",
        "eco_tag": "EL ECOSISTEMA", "eco_title": "Cuatro proyectos, una idea",
        "eco_lead": "Cada uno quita trabajo manual de una parte de la vida diaria: dinero, entrenamiento, comida y desarrollo de software.",
        "os_tag": "CÓDIGO ABIERTO", "os_title": "Construido en abierto",
        "os_lead": "Repositorios públicos del mismo taller.",
        "view": "VER EN GITHUB  ↗",
        "email": "EMAIL", "linkedin": "LINKEDIN",
        "projects": [
            ("midas", "I", "Midas", "En marcha", "Seguimiento de patrimonio y gasto local-first para hogares. Cuentas por persona, analítica XIRR y TWR, entrada por voz en español vía Telegram.", GOLD, f"{USER}/finance-tracker"),
            ("icor", "II", "Icor", "Pre-lanzamiento", "Entrenamiento de fuerza como RPG: XP, misiones, rankings y sincronización offline-first, con unos 200 ejercicios mapeados a activación muscular.", "#9c3f2c", None),
            ("hestia", "III", "Hestia", "En diseño", "Despensa inteligente y cocina anti-desperdicio: qué hay en casa, qué cocinar, qué comprar. Investigación hecha, construcción por delante.", "#b3722a", None),
            ("agora", "IV", "Ágora", "Interno", "Espacio en Telegram donde agentes de IA ejecutan tareas de desarrollo por proyecto, con aprobación humana en cada merge.", AEGEAN, None),
        ],
        "oss": [
            ("projects-dashboard", "Gestor de proyectos multi-forge (GitHub, GitLab, Bitbucket) con escaneo local y alertas por Telegram."),
            ("Content-Media-Manager", "Catálogo autoalojado de libros, películas, series, juegos y podcasts. Un contenedor Docker, sin nube."),
            ("arquitectura-doble-agente", "Arquitectura de referencia para dos agentes Hermes que se comunican por NATS y Telegram."),
        ],
    },
}


def svg(w, h, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
        f'<title>{escape(title)}</title>'
        f'<defs><filter id="m"><feTurbulence type="fractalNoise" baseFrequency="0.006 0.018" numOctaves="4" seed="7"/>'
        f'<feColorMatrix values="0 0 0 0 0.45  0 0 0 0 0.42  0 0 0 0 0.37  0 0 0 0.85 -0.38"/></filter></defs>'
        f'<rect width="{w}" height="{h}" fill="{MARBLE}"/><rect width="{w}" height="{h}" filter="url(#m)" opacity="0.5"/>'
        f"{body}</svg>"
    )


def text(x, y, s, size, fill, family=TEXT, weight=400, spacing=0, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{spacing}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def lines(x, y, s, size, fill, width, lh):
    out = []
    for i, ln in enumerate(textwrap.wrap(s, width)):
        out.append(text(x, y + i * lh, ln, size, fill))
    return "".join(out)


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")


def header(lang):
    t = T[lang]
    body = (
        f'<rect x="0.5" y="0.5" width="829" height="259" fill="none" stroke="{LINE}"/>'
        f'<rect x="48" y="52" width="76" height="76" fill="{AEGEAN}"/>'
        f'<g transform="translate(55 57) scale(0.47)"><path d="{LAMBDA}" fill="{MARBLE}"/></g>'
        + text(148, 80, t["eyebrow"], 12.5, AEGEAN, TITLE, 600, 3.2)
        + text(146, 130, "PABLO RS", 50, INK, TITLE, 500, 5)
        + text(148, 168, t["tagline"], 22, MUTED)
        + f'<line x1="48" y1="206" x2="782" y2="206" stroke="{GOLD}" stroke-width="1.2">'
          f'<animate attributeName="x2" from="48" to="782" dur="1.6s" fill="freeze"/></line>'
        + text(48, 234, "PYTHON  ·  AUTOMATION  ·  AI AGENTS  ·  FLUTTER", 11.5, MUTED, TITLE, 600, 3.4)
    )
    write(f"header.{lang}.svg", svg(830, 260, body, "Pablo RS — Olimpo Labs"))


def section(lang, key):
    t = T[lang]
    tag, title, lead = t[f"{key}_tag"], t[f"{key}_title"], t[f"{key}_lead"]
    body = (
        text(48, 44, tag, 12.5, AEGEAN, TITLE, 600, 4.4)
        + text(48, 86, title.upper(), 30, INK, TITLE, 500, 2)
        + lines(48, 118, lead, 19, MUTED, 84, 24)
    )
    write(f"section-{key}.{lang}.svg", svg(830, 160, body, title))


def card(lang, p):
    pid, num, name, status, desc, accent, repo = p
    w, h = 415, 262
    pill_w = 14 + len(status) * 8.2
    body = (
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="none" stroke="{LINE}"/>'
        f'<rect x="0" y="0" width="{w}" height="3" fill="{accent}"/>'
        + text(30, 58, num, 15, accent, TITLE, 600, 4.5)
        + f'<rect x="{w-30-pill_w}" y="40" width="{pill_w}" height="22" fill="none" stroke="{accent}"/>'
        + text(w - 30 - pill_w / 2, 55, status.upper(), 9.5, accent, TITLE, 600, 1.8, "middle")
        + text(30, 106, name.upper(), 29, INK, TITLE, 500, 3)
        + lines(30, 138, desc, 17, MUTED, 50, 22)
        + (text(30, h - 24, T[lang]["view"], 10.5, accent, TITLE, 600, 2.4) if repo else "")
    )
    write(f"card-{pid}.{lang}.svg", svg(w, h, body, f"{name} — {status}"))


def repo_row(lang, name, desc):
    w, h = 830, 74
    body = (
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="none" stroke="{LINE}"/>'
        f'<rect x="0" y="0" width="3" height="{h}" fill="{GOLD}"/>'
        + text(28, 32, name, 15, AEGEAN, TITLE, 600, 1.6)
        + text(28, 56, desc, 16.5, MUTED)
        + text(w - 28, 42, "↗", 22, GOLD, TEXT, 400, 0, "end")
    )
    write(f"repo-{name}.{lang}.svg", svg(w, h, body, name))


def button(lang, key, filled):
    w, h = 190, 48
    label = T[lang][key]
    fill, color = (AEGEAN, MARBLE) if filled else ("none", AEGEAN)
    body = (
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="{fill}" stroke="{AEGEAN}"/>'
        + text(w / 2, 29, label, 12, color, TITLE, 600, 3.4, "middle")
    )
    write(f"btn-{key}.{lang}.svg", svg(w, h, body, label))


def readme_block(lang):
    t = T[lang]
    cards = "\n".join(
        (f'<a href="{p[6]}"><img src="assets/card-{p[0]}.{lang}.svg" width="49%" alt="{p[2]}"></a>'
         if p[6] else f'<img src="assets/card-{p[0]}.{lang}.svg" width="49%" alt="{p[2]}">')
        for p in t["projects"])
    rows = "\n".join(
        f'<a href="{USER}/{n}"><img src="assets/repo-{n}.{lang}.svg" width="100%" alt="{n}"></a>' for n, _ in t["oss"])
    return f'''<div align="center">
<img src="assets/header.{lang}.svg" width="100%" alt="Pablo RS — Olimpo Labs">
<br>
<a href="mailto:pablorgz98@gmail.com"><img src="assets/btn-email.{lang}.svg" height="44" alt="Email"></a>
<a href="https://www.linkedin.com/in/pablors98"><img src="assets/btn-linkedin.{lang}.svg" height="44" alt="LinkedIn"></a>
</div>

<br>

<img src="assets/section-eco.{lang}.svg" width="100%" alt="{t['eco_title']}">
<div align="center">
{cards}
</div>

<br>

<img src="assets/section-os.{lang}.svg" width="100%" alt="{t['os_title']}">
{rows}
'''


def build_readme():
    lang_en = readme_block("en")
    lang_es = readme_block("es")
    return f'''<!-- Generated by scripts/build_assets.py — edit the script, not this file. -->
{lang_en}
<div align="center"><sub>🇬🇧 English · <a href="#-en-español">🇪🇸 Léelo en español</a></sub></div>

<br>

> [!TIP]
> **Open to junior developer roles, internships and collaborative projects.** Fastest way to reach me: [email](mailto:pablorgz98@gmail.com) or [LinkedIn](https://www.linkedin.com/in/pablors98).

<details>
<summary><b>🧠 How my agents talk to each other</b></summary>

<br>

```mermaid
flowchart LR
    U(["👤 User"]) <--> TG["📱 Telegram Bot"]
    TG <--> H1["🤖 Hermes Agent 1"]
    H1 <--> N{{{{"⚡ NATS<br>message bus"}}}}
    N <--> H2["🤖 Hermes Agent 2"]

    style U fill:#17406b,stroke:#a98532,color:#f2eee4
    style TG fill:#17406b,stroke:#a98532,color:#f2eee4
    style H1 fill:#f2eee4,stroke:#17406b,color:#16130f
    style H2 fill:#f2eee4,stroke:#17406b,color:#16130f
    style N fill:#a98532,stroke:#16130f,color:#16130f
```

</details>

<details>
<summary><b>📈 Activity</b> <sub>(auto-updated)</sub></summary>

<br>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/PabloRS98/PabloRS98/output/github-snake-dark.svg">
  <img src="https://raw.githubusercontent.com/PabloRS98/PabloRS98/output/github-snake.svg" alt="Contribution snake" width="100%">
</picture>
</div>

**Latest repositories**

<!--START_SECTION:repos-->
<!--END_SECTION:repos-->

**Recent commits**

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

</details>

<br>

---

<h2 id="-en-español">🇪🇸 En español</h2>

<details>
<summary><b>Haz clic para desplegar la versión en español</b></summary>

<br>

{lang_es}
> [!TIP]
> **Abierto a puestos junior, prácticas y proyectos en colaboración.**

</details>
'''


if __name__ == "__main__":
    for lang in T:
        header(lang)
        section(lang, "eco")
        section(lang, "os")
        for p in T[lang]["projects"]:
            card(lang, p)
        for n, d in T[lang]["oss"]:
            repo_row(lang, n, d)
        button(lang, "email", True)
        button(lang, "linkedin", False)
    (ROOT / "README.md").write_text(build_readme(), encoding="utf-8")
    print("ok")
