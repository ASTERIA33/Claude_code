from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import pptx.oxml.ns as nsmap
from lxml import etree

# ── Palette M&M ──────────────────────────────────────────────
DARK_BG    = RGBColor(0x0D, 0x1B, 0x2A)   # bleu nuit
ACCENT     = RGBColor(0xFF, 0xB7, 0x00)   # jaune/or
GREEN      = RGBColor(0x2E, 0xCC, 0x71)   # vert succès
BLUE_CARD  = RGBColor(0x16, 0x2A, 0x44)   # carte foncée
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
GREY_TEXT  = RGBColor(0xAA, 0xBB, 0xCC)
ORANGE     = RGBColor(0xFF, 0x6B, 0x35)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

def fill_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_rect(slide, l, t, w, h, color, alpha=None):
    shape = slide.shapes.add_shape(
        pptx.enum.shapes.MSO_SHAPE_TYPE.AUTO_SHAPE if False else 1,
        l, t, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_text_box(slide, text, l, t, w, h,
                 font_size=14, bold=False, color=WHITE,
                 align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txb = slide.shapes.add_textbox(l, t, w, h)
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = Pt(font_size)
    run.font.bold  = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return txb

def add_rounded_rect(slide, l, t, w, h, color, radius_emu=Emu(120000)):
    from pptx.util import Emu
    shape = slide.shapes.add_shape(
        5,  # rounded rectangle
        l, t, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    # adjust corner radius
    adj = shape.adjustments
    try:
        adj[0] = 0.05
    except Exception:
        pass
    return shape

# ── Background ────────────────────────────────────────────────
fill_bg(slide, DARK_BG)

# ── Top accent bar ────────────────────────────────────────────
add_rect(slide, Inches(0), Inches(0), SLIDE_W, Inches(0.07), ACCENT)

# ── Title ─────────────────────────────────────────────────────
add_text_box(slide, "Intégrer l'IA sur Shopify",
             Inches(0.5), Inches(0.15), Inches(8), Inches(0.55),
             font_size=28, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

add_text_box(slide, "Roadmap M&M — De la connexion rapide à l'orchestration intelligente",
             Inches(0.5), Inches(0.65), Inches(10), Inches(0.4),
             font_size=13, bold=False, color=GREY_TEXT, align=PP_ALIGN.LEFT, italic=True)

# badge
badge = add_rounded_rect(slide, Inches(11.2), Inches(0.18), Inches(1.9), Inches(0.45), ACCENT)
add_text_box(slide, "M&M PROJECT",
             Inches(11.2), Inches(0.2), Inches(1.9), Inches(0.4),
             font_size=10, bold=True, color=DARK_BG, align=PP_ALIGN.CENTER)

# ── Separator line ────────────────────────────────────────────
add_rect(slide, Inches(0.5), Inches(1.05), Inches(12.3), Inches(0.025), ACCENT)

# ══════════════════════════════════════════════════════════════
# OPTION 1 — left column  (x=0.4, w=3.6)
# ══════════════════════════════════════════════════════════════
C1_L = Inches(0.35)
C1_W = Inches(3.7)

# card bg
add_rounded_rect(slide, C1_L, Inches(1.15), C1_W, Inches(5.9), BLUE_CARD)

# header strip
add_rounded_rect(slide, C1_L, Inches(1.15), C1_W, Inches(0.65), RGBColor(0x1A, 0x3A, 0x5C))

add_text_box(slide, "⚡  OPTION 1 — Connexion Rapide",
             C1_L + Inches(0.12), Inches(1.2), C1_W - Inches(0.2), Inches(0.55),
             font_size=12, bold=True, color=ACCENT, align=PP_ALIGN.LEFT)

add_text_box(slide, "IA existantes, plug & play",
             C1_L + Inches(0.15), Inches(1.78), C1_W - Inches(0.25), Inches(0.35),
             font_size=10, bold=True, color=WHITE)

tools = [
    ("Tidio / Gorgias AI",    "Chat + tickets automatisés"),
    ("Shopify Inbox AI",      "Natif, FAQ & recommandations"),
    ("Klaviyo AI",            "Emails personnalisés auto"),
    ("ChatGPT Plugin",        "Réponses contextuelles"),
]
y = 2.2
for name, desc in tools:
    dot = add_rounded_rect(slide, C1_L + Inches(0.18), Inches(y + 0.08),
                           Inches(0.12), Inches(0.12), ACCENT)
    add_text_box(slide, name,
                 C1_L + Inches(0.38), Inches(y), C1_W - Inches(0.5), Inches(0.28),
                 font_size=10, bold=True, color=WHITE)
    add_text_box(slide, desc,
                 C1_L + Inches(0.38), Inches(y + 0.25), C1_W - Inches(0.5), Inches(0.28),
                 font_size=9, bold=False, color=GREY_TEXT)
    y += 0.62

# pros
add_rect(slide, C1_L + Inches(0.15), Inches(4.72), C1_W - Inches(0.3), Inches(0.02), ACCENT)
add_text_box(slide, "✅  Avantages",
             C1_L + Inches(0.15), Inches(4.75), C1_W - Inches(0.25), Inches(0.3),
             font_size=10, bold=True, color=GREEN)
pros = ["Déploiement en 1–2 semaines", "Coût prévisible (SaaS)", "0 dev requis"]
for i, p in enumerate(pros):
    add_text_box(slide, f"• {p}",
                 C1_L + Inches(0.2), Inches(5.05 + i * 0.32), C1_W - Inches(0.3), Inches(0.3),
                 font_size=9, color=GREY_TEXT)

add_text_box(slide, "→ Vision : exécution immédiate",
             C1_L + Inches(0.15), Inches(6.75), C1_W - Inches(0.25), Inches(0.32),
             font_size=9, bold=True, color=ACCENT, italic=True)

# ══════════════════════════════════════════════════════════════
# Arrow between columns
# ══════════════════════════════════════════════════════════════
add_text_box(slide, "➜",
             Inches(4.13), Inches(3.5), Inches(0.45), Inches(0.45),
             font_size=22, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
add_text_box(slide, "Évolue\nvers",
             Inches(4.08), Inches(3.92), Inches(0.55), Inches(0.5),
             font_size=8, color=GREY_TEXT, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════
# OPTION 2 — right large column  (x=4.75, w=8.25)
# ══════════════════════════════════════════════════════════════
C2_L = Inches(4.75)
C2_W = Inches(8.25)

add_rounded_rect(slide, C2_L, Inches(1.15), C2_W, Inches(5.9), BLUE_CARD)
add_rounded_rect(slide, C2_L, Inches(1.15), C2_W, Inches(0.65), RGBColor(0x0A, 0x2A, 0x1A))
add_text_box(slide, "🤖  OPTION 2 — Orchestration Multi-Agents  (Vision Cible)",
             C2_L + Inches(0.15), Inches(1.2), C2_W - Inches(0.2), Inches(0.55),
             font_size=12, bold=True, color=GREEN, align=PP_ALIGN.LEFT)

# ── Flow diagram ──────────────────────────────────────────────
FY   = 1.92   # top of flow
FSTEP = 1.08  # vertical step
BW   = Inches(2.05)
BH   = Inches(0.72)
BL   = C2_L + Inches(0.3)

steps = [
    (ACCENT,                  "❓  Question client",          "Via chat Shopify, email, WhatsApp…"),
    (RGBColor(0x1A,0x6A,0xC8), "🔍  Agent 1 — Retrieval",     "Fiche produit · stock · retour · historique commande"),
    (RGBColor(0x7B,0x2F,0xBE), "✍️   Agent 2 — Rédacteur",     "Reformule avec le ton de marque M&M\n(bienveillant · expert parental · rassurant)"),
    (RGBColor(0x0A,0x6E,0x4A), "🛡  Agent 3 — Validation",    "Vérifie cohérence, mots interdits, sécurité avant envoi"),
    (GREEN,                   "✅  Réponse finale au client",  "Personnalisée · on-brand · fiable"),
]

for i, (color, title, sub) in enumerate(steps):
    y_pos = FY + i * FSTEP
    box = add_rounded_rect(slide, BL, Inches(y_pos), BW, BH, color)
    add_text_box(slide, title,
                 BL + Inches(0.1), Inches(y_pos + 0.05), BW - Inches(0.15), Inches(0.32),
                 font_size=10, bold=True, color=WHITE)
    add_text_box(slide, sub,
                 BL + Inches(0.1), Inches(y_pos + 0.36), BW - Inches(0.15), Inches(0.36),
                 font_size=8, color=WHITE)
    # arrow down (except last)
    if i < len(steps) - 1:
        add_text_box(slide, "▼",
                     BL + Inches(0.85), Inches(y_pos + BH/Inches(1) + 0.02),
                     Inches(0.35), Inches(0.22),
                     font_size=11, color=GREY_TEXT, align=PP_ALIGN.CENTER)

# ── Why powerful — right sub-column ──────────────────────────
RCL = C2_L + Inches(2.5)
RCW = C2_W - Inches(2.65)

add_text_box(slide, "Pourquoi c'est puissant pour M&M",
             RCL, Inches(1.82), RCW, Inches(0.38),
             font_size=11, bold=True, color=WHITE)

bullets = [
    ("Agent 1",  ACCENT,                  "Optimisé RAG + API Shopify\n→ info toujours à jour"),
    ("Agent 2",  RGBColor(0x7B,0x2F,0xBE),"Prompt système sur ton de marque\n→ mots interdits, valeurs M&M"),
    ("Agent 3",  GREEN,                   "Garde-fou avant envoi\n→ zéro réponse incohérente"),
    ("Évolutif", RGBColor(0x1A,0x6A,0xC8),"Ajouter un agent upsell, traduction,\nnotif stock facilement"),
]

for i, (tag, col, desc) in enumerate(bullets):
    yb = 2.28 + i * 1.18
    badge_s = add_rounded_rect(slide, RCL, Inches(yb), Inches(0.75), Inches(0.28), col)
    add_text_box(slide, tag,
                 RCL, Inches(yb + 0.01), Inches(0.75), Inches(0.27),
                 font_size=8, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text_box(slide, desc,
                 RCL + Inches(0.82), Inches(yb - 0.02), RCW - Inches(0.88), Inches(0.55),
                 font_size=9, color=GREY_TEXT)

# Recommendation footer in option 2
add_rounded_rect(slide, C2_L + Inches(0.15), Inches(6.7), C2_W - Inches(0.3), Inches(0.28),
                 RGBColor(0x0A, 0x2A, 0x1A))
add_text_box(slide,
             "→ Vision terme : architecture souveraine, différenciante, 100 % aux couleurs de M&M",
             C2_L + Inches(0.25), Inches(6.72), C2_W - Inches(0.4), Inches(0.26),
             font_size=9, bold=True, color=GREEN, italic=True)

# ── Bottom bar ────────────────────────────────────────────────
add_rect(slide, Inches(0), Inches(7.43), SLIDE_W, Inches(0.07), ACCENT)

out = "/home/user/Claude_code/MM_Shopify_IA_Slide.pptx"
prs.save(out)
print(f"Saved → {out}")
