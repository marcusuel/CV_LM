import streamlit as st
 
st.set_page_config(
    page_title="Marc Le Moing – Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600;700&display=swap');
 
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #f5f4f0; color: #1a1a1a; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 4rem 3rem; max-width: 1050px; }
 
/* SIDEBAR */
[data-testid="stSidebar"] { background: #1c1c1e !important; border-right: none; }
[data-testid="stSidebar"] > div:first-child { padding: 2rem 1.5rem; }
.sb-avatar {
    width: 80px; height: 80px; border-radius: 50%;
    background: linear-gradient(135deg, #f59e0b, #ef4444);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; font-weight: 800; color: white;
    margin: 0 auto 1rem auto; letter-spacing: -0.05em;
}
.sb-name { font-weight: 700; font-size: 1rem; color: #fff; text-align: center; margin-bottom: 0.15rem; }
.sb-role { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: #6b7280; text-align: center; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.5rem; }
.sb-sep { border: none; border-top: 1px solid #2d2d2f; margin: 1.1rem 0; }
.sb-label { font-family: 'DM Mono', monospace; font-size: 0.58rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 0.6rem; }
.sb-row { display: flex; align-items: flex-start; gap: 0.6rem; padding: 0.5rem 0.6rem; border-radius: 7px; margin-bottom: 0.3rem; text-decoration: none; transition: background 0.15s; }
.sb-row:hover { background: #2a2a2d; }
.sb-icon { font-size: 0.95rem; flex-shrink: 0; width: 18px; text-align: center; margin-top: 1px; }
.sb-clabel { font-family: 'DM Mono', monospace; font-size: 0.56rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.08em; }
.sb-cval { font-size: 0.78rem; color: #f9fafb; font-weight: 500; word-break: break-all; }
.sb-dispo { display: flex; align-items: center; gap: 0.5rem; background: #052e16; border: 1px solid #166534; border-radius: 7px; padding: 0.6rem 0.8rem; margin-top: 0.75rem; }
.sb-dot { width: 7px; height: 7px; border-radius: 50%; background: #4ade80; flex-shrink: 0; box-shadow: 0 0 5px #4ade80; animation: blink 2s ease-in-out infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }
.sb-dispo-txt { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: #4ade80; }
 
/* TABS */
.stTabs [data-baseweb="tab-list"] { gap: 0; background: transparent; border-bottom: 2px solid #e5e1d8; margin-bottom: 2.25rem; }
.stTabs [data-baseweb="tab"] { background: transparent; border: none; color: #9ca3af; font-family: 'DM Mono', monospace; font-size: 0.72rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.7rem 1.25rem; border-bottom: 2px solid transparent; transition: all 0.2s; margin-bottom: -2px; }
.stTabs [aria-selected="true"] { color: #1a1a1a !important; border-bottom: 2px solid #f59e0b !important; background: transparent !important; }
.stTabs [data-baseweb="tab"]:hover { color: #374151 !important; background: transparent !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }
 
/* TYPOGRAPHY */
.page-eyebrow { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 0.4rem; }
.page-title { font-size: 2rem; font-weight: 700; color: #111827; letter-spacing: -0.03em; line-height: 1.1; margin: 0 0 0.5rem 0; }
.page-sub { font-size: 1rem; color: #6b7280; line-height: 1.65; max-width: 680px; }
.section-head { font-family: 'DM Mono', monospace; font-size: 0.62rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.2em; border-bottom: 1px solid #e5e1d8; padding-bottom: 0.5rem; margin: 2rem 0 1.25rem 0; }
 
/* CARDS */
.card { background: #ffffff; border: 1px solid #e5e1d8; border-radius: 10px; padding: 1.4rem 1.75rem; margin-bottom: 1rem; position: relative; overflow: hidden; transition: box-shadow 0.2s, transform 0.2s; }
.card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.07); transform: translateY(-1px); }
 
/* TAGS */
.tag-wrap { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.85rem; }
.tag { font-family: 'DM Mono', monospace; font-size: 0.62rem; font-weight: 500; letter-spacing: 0.05em; padding: 0.2rem 0.6rem; border-radius: 4px; text-transform: uppercase; }
.tag-amber  { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
.tag-blue   { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
.tag-green  { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
.tag-slate  { background: #f1f5f9; color: #334155; border: 1px solid #cbd5e1; }
.tag-rose   { background: #fff1f2; color: #9f1239; border: 1px solid #fecdd3; }
 
/* HERO */
.hero-name { font-size: 3.2rem; font-weight: 700; letter-spacing: -0.04em; color: #111827; line-height: 1; margin: 0 0 0.3rem 0; }
.hero-accent { color: #f59e0b; }
.hero-title { font-family: 'DM Mono', monospace; font-size: 0.78rem; color: #9ca3af; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.25rem; }
.hero-bio { font-size: 1rem; color: #374151; line-height: 1.75; max-width: 640px; }
.stat-box { background: #fff; border: 1px solid #e5e1d8; border-radius: 10px; padding: 1.1rem; text-align: center; margin-bottom: 0.65rem; }
.stat-num { font-size: 1.8rem; font-weight: 700; color: #f59e0b; line-height: 1; }
.stat-label { font-family: 'DM Mono', monospace; font-size: 0.58rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.25rem; }
.skill-group-title { font-family: 'DM Mono', monospace; font-size: 0.62rem; font-weight: 500; color: #6b7280; text-transform: uppercase; letter-spacing: 0.15em; margin: 0 0 0.5rem 0; }
 
/* LANG */
.lang-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.6rem; }
.lang-name { font-weight: 600; color: #374151; width: 80px; font-size: 0.88rem; }
.lang-bar-bg { flex: 1; height: 5px; background: #e5e1d8; border-radius: 3px; overflow: hidden; }
.lang-bar-fill { height: 100%; border-radius: 3px; background: #f59e0b; }
.lang-level { font-family: 'DM Mono', monospace; font-size: 0.62rem; color: #9ca3af; width: 80px; text-align: right; }
 
/* TIMELINE */
.timeline-item { display: flex; gap: 1.25rem; margin-bottom: 1.5rem; align-items: flex-start; }
.tl-left { flex-shrink: 0; width: 80px; text-align: right; }
.tl-year { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: #9ca3af; margin-top: 0.15rem; }
.tl-dot-col { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
.tl-dot { width: 10px; height: 10px; border-radius: 50%; background: #f59e0b; margin-top: 0.2rem; flex-shrink: 0; }
.tl-line { flex: 1; width: 1px; background: #e5e1d8; margin-top: 4px; min-height: 40px; }
.tl-content { flex: 1; padding-bottom: 0.5rem; }
.tl-title { font-weight: 700; color: #111827; font-size: 0.95rem; }
.tl-org { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: #f59e0b; margin-bottom: 0.4rem; margin-top: 0.15rem; }
.tl-desc { font-size: 0.85rem; color: #6b7280; line-height: 1.65; }
 
/* FORMATION CARD */
.fcard { background: #fff; border: 1px solid #e5e1d8; border-radius: 10px; padding: 1.1rem 1.4rem; margin-bottom: 0.75rem; display: flex; align-items: flex-start; gap: 0.9rem; }
.fcard-icon { font-size: 1.3rem; flex-shrink: 0; margin-top: 0.1rem; }
.fcard-year { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: #9ca3af; margin-bottom: 0.1rem; }
.fcard-name { font-weight: 700; color: #111827; font-size: 0.9rem; }
.fcard-org { font-size: 0.8rem; color: #6b7280; margin-top: 0.15rem; }
.fcard-desc { font-size: 0.82rem; color: #9ca3af; margin-top: 0.4rem; line-height: 1.6; }
 
/* EXP HEADER */
.exp-header { background: #fff; border: 1px solid #e5e1d8; border-radius: 12px; padding: 1.75rem 2rem; margin-bottom: 1.5rem; display: flex; align-items: flex-start; gap: 1.5rem; }
.exp-logo { width: 52px; height: 52px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; }
.exp-htitle { font-size: 1.4rem; font-weight: 700; color: #111827; margin-bottom: 0.15rem; }
.exp-hsubtitle { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: #f59e0b; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
.exp-hdesc { font-size: 0.88rem; color: #6b7280; line-height: 1.65; max-width: 600px; }
 
/* MISSION BLOCK */
.mission-block { background: #fafaf9; border: 1px solid #e5e1d8; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 0.75rem; }
.mission-title { font-weight: 600; color: #374151; font-size: 0.88rem; margin-bottom: 0.4rem; }
.mission-body { font-size: 0.84rem; color: #6b7280; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)
 
# ── HELPERS ───────────────────────────────────────────────────────────────────
def tags(items, color="slate"):
    html = '<div class="tag-wrap">'
    for it in items:
        html += f'<span class="tag tag-{color}">{it}</span>'
    html += "</div>"
    return html
 
def mixed_tags(pairs):
    html = '<div class="tag-wrap">'
    for label, c in pairs:
        html += f'<span class="tag tag-{c}">{label}</span>'
    html += "</div>"
    return html
 
def mission_block(title, body, tag_pairs=None):
    t = mixed_tags(tag_pairs) if tag_pairs else ""
    return f"""
    <div class="mission-block">
        <div class="mission-title">{title}</div>
        <div class="mission-body">{body}</div>
        {t}
    </div>"""
 
# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""<style>
[data-testid="stSidebar"] { background: #1c1c1e !important; }
[data-testid="stSidebar"] .stDownloadButton button { background: #2d2d2f !important; color: #f3f4f6 !important; border: 1px solid #3d3d3f !important; border-radius: 7px !important; font-size: 0.82rem !important; width: 100% !important; }
</style><div style="text-align:center;padding:0 0 1rem 0;"><div style="width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,#f59e0b,#ef4444);display:flex;align-items:center;justify-content:center;font-size:1.4rem;font-weight:800;color:white;margin:0 auto 0.85rem;">ML</div><div style="font-weight:700;font-size:1rem;color:#fff;margin-bottom:0.2rem;">Marc LE MOING</div><div style="font-size:0.6rem;color:#9ca3af;letter-spacing:0.08em;text-transform:uppercase;">Data Analyst · Mathématiques Appliquées</div></div><div style="border-top:1px solid #2d2d2f;margin:0.5rem 0 0.8rem;"></div><div style="font-size:0.6rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.5rem;">Me contacter</div><a href="tel:+33767642433" style="display:flex;align-items:center;gap:0.6rem;padding:0.4rem 0.5rem;border-radius:6px;text-decoration:none;"><span style="color:#9ca3af;width:16px;flex-shrink:0;font-size:0.9rem;">✆</span><div><div style="font-size:0.56rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.06em;">Téléphone</div><div style="font-size:0.8rem;color:#f3f4f6;font-weight:500;">(+33)7 67 64 24 33</div></div></a><a href="mailto:marclemoing@laposte.net" style="display:flex;align-items:center;gap:0.6rem;padding:0.4rem 0.5rem;border-radius:6px;text-decoration:none;"><span style="color:#9ca3af;width:16px;flex-shrink:0;font-size:0.9rem;">✉</span><div><div style="font-size:0.56rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.06em;">Email</div><div style="font-size:0.8rem;color:#f3f4f6;font-weight:500;">marclemoing@laposte.net</div></div></a><a href="https://www.linkedin.com/in/marc-le-moing-a21003201/" target="_blank" style="display:flex;align-items:center;gap:0.6rem;padding:0.4rem 0.5rem;border-radius:6px;text-decoration:none;"><span style="color:#9ca3af;width:16px;flex-shrink:0;font-size:0.9rem;font-weight:700;">in</span><div><div style="font-size:0.56rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.06em;">LinkedIn</div><div style="font-size:0.8rem;color:#f3f4f6;font-weight:500;">marc-le-moing</div></div></a><div style="display:flex;align-items:center;gap:0.6rem;padding:0.4rem 0.5rem;border-radius:6px;"><span style="color:#9ca3af;width:16px;flex-shrink:0;font-size:0.9rem;">📍</span><div><div style="font-size:0.56rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.06em;">Mobilité</div><div style="font-size:0.8rem;color:#f3f4f6;font-weight:500;">France · Espagne · Suisse</div></div></div><div style="border-top:1px solid #2d2d2f;margin:0.75rem 0;"></div><div style="display:flex;align-items:center;gap:0.5rem;background:#052e16;border:1px solid #166534;border-radius:7px;padding:0.55rem 0.8rem;"><div style="width:7px;height:7px;border-radius:50%;background:#4ade80;box-shadow:0 0 5px #4ade80;flex-shrink:0;"></div><span style="font-size:0.65rem;color:#4ade80;"> En Poste - Disponible sous 3 mois </span></div><div style="border-top:1px solid #2d2d2f;margin:0.75rem 0 0.4rem;"></div><div style="font-size:0.6rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.3rem;">Télécharger</div>""", unsafe_allow_html=True)

    try:
        with open("CV_LEMOING_Marc.pdf", "rb") as f:
            pdf_bytes = f.read()
    except FileNotFoundError:
        pdf_bytes = b""
    st.download_button("📄  CV en PDF", data=pdf_bytes, file_name="CV_Marc_Le_Moing.pdf", mime="application/pdf", use_container_width=True)
# ── TABS ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["🏠  Accueil", "🎓  Formations", "🔬  Stages & Alternance", "💨  AirBreizh", "🏙️  AUDAP"])
 
# ═══ TAB 1 – ACCUEIL ══════════════════════════════════════════════════════════
with tabs[0]:
    col_h, col_s = st.columns([3, 1], gap="large")
    with col_h:
        st.markdown("""
        <p class="hero-name">Marc <span class="hero-accent">LE MOING</span></p>
        <p class="hero-title">Data Analyst · Ingénieur Mathématiques Appliquées · INSA Rennes</p>
        <p class="hero-bio">Diplômé de l'INSA de Rennes en Mathématiques Appliquées, passionné par la découverte
        de nouveaux éléments via le prisme de la Data. Curieux, motivé, à l'aise en contexte pluridisciplinaire,
        j'aime transformer des données brutes en livrables concrets et utiles.</p>
        """, unsafe_allow_html=True)
    with col_s:
        for num, label in [("4+", "Ans d'XP"), ("5", "Structures"), ("C1", "TOEIC 990")]:
            st.markdown(f'<div class="stat-box"><div class="stat-num">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Compétences techniques</div>', unsafe_allow_html=True)
 
    skill_groups = [
        ("Langages", ["Python", "R", "SQL"], "amber"),
        ("Visualisation", ["Power BI", "Grafana", "Matplotlib", "Jupyter"], "blue"),
        ("Data & Modélisation", ["Random Forest", "Time Series", "Scoring", "Statistiques"], "green"),
        ("Infra & Outils", ["IA","Git / GitLab", "InfluxDB", "QGIS", "Crontab", "VMs", "Linux", "PostgreSQL"], "slate"),
        ("Simulation", ["MATSim", "SIRANE", "Plus proches voisins"], "rose"),
    ]
 
    col1, col2, col3 = st.columns(3, gap="medium")
    for i, (cat, items, color) in enumerate(skill_groups):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f'<div class="card" style="margin-bottom:0.85rem"><div class="skill-group-title">{cat}</div>{tags(items, color)}</div>', unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Langues</div>', unsafe_allow_html=True)
    for lang, pct, lvl in [("Français", 100, "Natif"), ("Anglais", 95, "C1 · TOEIC 990"), ("Espagnol", 80, "B2/C1")]:
        st.markdown(f'<div class="lang-row"><span class="lang-name">{lang}</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:{pct}%"></div></div><span class="lang-level">{lvl}</span></div>', unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Centres d\'intérêt</div>', unsafe_allow_html=True)
    st.markdown(mixed_tags([
        ("⚽ Football", "slate"), ("🏋️ Musculation", "slate"), ("📈 Finance & Chiffres", "blue"),
        ("✈️ GroundHopping", "green"), ("🌍 Langues étrangères", "amber"), ("👥 Travail d'équipe", "rose"),
    ]), unsafe_allow_html=True)
 
# ═══ TAB 2 – FORMATIONS ═══════════════════════════════════════════════════════
with tabs[1]:
    st.markdown('<div class="page-eyebrow">Parcours académique</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="page-title">Formations</h2>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Un parcours construit autour des mathématiques, de l\'informatique et de la data, avec une forte ouverture interculturelle et interdisciplinaire.</p>', unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Diplômes</div>', unsafe_allow_html=True)
 
    for annee, icon, titre, org, desc, tag_pairs in [
        ("2020–2023", "🎓", "Ingénieur Mathématiques Appliquées", "INSA Rennes · Génie Mathématique",
         "Spécialisation ingénieur en 3 ans combinant deux grandes approches :<br><br>"
         "<strong>Optimisation</strong> — modélisation de problèmes complexes via équations, optimisation sous incertitude, recherche opérationnelle, simulation numérique.<br><br>"
         "<strong>Data Science</strong> — statistiques appliquées, développement Python, analyse et visualisation de données, machine learning, traitement de données massives.<br><br>"
         "Ouverture interculturelle et interdisciplinaire forte grâce aux différents stages et à l'alternance.",
         [("Python", "amber"), ("R", "amber"), ("Statistiques", "blue"), ("Optimisation", "green"), ("Machine Learning", "slate")]),
        ("2018–2020", "📐", "Prépa Intégrée INSA Rennes", "Classes préparatoires intégrées",
         "Deux années de préparation au cycle ingénieur couvrant mathématiques, physique, mécanique, chimie et langues. "
         "C'est durant cette période qu'a émergé une vraie appétence pour les mathématiques et l'informatique.",
         [("Mathématiques", "blue"), ("Physique", "slate"), ("Algorithmique", "green")]),
        ("2018", "🏫", "Bac S – Sciences de l'Ingénieur", "Lycée",
         "Point de départ d'une orientation vers les domaines techniques, avec une curiosité naturelle pour la modélisation et les systèmes.",
         []),
    ]:
        t = mixed_tags(tag_pairs) if tag_pairs else ""
        tag_section = f'<div style="margin-top:0.6rem">{t}</div>' if t else ""
        st.markdown(f"""<div class="timeline-item"><div class="tl-left"><div class="tl-year">{annee}</div></div><div class="tl-dot-col"><div class="tl-dot"></div><div class="tl-line"></div></div><div class="tl-content"><div class="tl-title">{icon} {titre}</div><div class="tl-org">{org}</div><div class="tl-desc">{desc}</div>{tag_section}</div></div>""", unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Formations suivies en entreprise</div>', unsafe_allow_html=True)
    for annee, icon, nom, org, desc in [
        ("2023", "🐍", "Formation Python", "Certification interne", "Bonnes pratiques Python pour la data : manipulation, automatisation, scripts de traitement."),
        ("Mai 2025", "🦊", "Formation GitLab", "Formation professionnelle", "Gestion de projets collaboratifs, versioning, CI/CD, travail en équipe sur dépôts partagés."),
        ("Juin 2025", "⚡", "Calcul parallélisé", "Formation professionnelle", "Techniques de parallélisation pour accélérer les traitements de données volumineuses en Python."),
        ("Oct–Déc 2025", "🗄️", "SQL avancé", "Formation professionnelle", "Requêtes complexes, optimisation, gestion de bases de données relationnelles, PostgreSQL."),
        ("Oct 2025", "📊", "Power BI", "Formation professionnelle", "Construction de tableaux de bord et rapports analytiques."),
        ("Nov 2025", "🖥️", "Machines Virtuelles & Management du parc", "Formation professionnelle", "Administration de VMs, migration de serveurs, maintenance d'infrastructure."),
    ]:
        st.markdown(f'<div class="fcard"><div class="fcard-icon">{icon}</div><div><div class="fcard-year">{annee}</div><div class="fcard-name">{nom}</div><div class="fcard-org">{org}</div><div class="fcard-desc">{desc}</div></div></div>', unsafe_allow_html=True)
 
# ═══ TAB 3 – STAGES & ALTERNANCE ══════════════════════════════════════════════
with tabs[2]:
    st.markdown('<div class="page-eyebrow">Expériences académiques</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="page-title">Stages & Alternance</h2>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Trois premières expériences terrain menées en parallèle du cursus ingénieur.</p>', unsafe_allow_html=True)
 
    # STALAVEN
    st.markdown("""
    <div class="exp-header">
        <div class="exp-logo" style="background:#fef3c7">🐖</div>
        <div>
            <div class="exp-htitle">Alternance – Data Scientist</div>
            <div class="exp-hsubtitle">STALAVEN · Yffiniac, France · Sept 2022 – Août 2023</div>
            <div class="exp-hdesc">Intégration au pôle prévision des ventes d'une entreprise agroalimentaire bretonne.
            Mission centrale : poser les premières briques d'un traitement data structuré et créer un outil de prévision des ventes clef en main.</div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(mission_block("🌲 Modèle de prévision des ventes",
        "Création d'un modèle de prévision clef en main sous Python basé sur un algorithme de forêt aléatoire (Random Forest). "
        "Objectif : permettre à l'entreprise de maîtriser ses propres chiffres et d'envisager de se détacher de son prestataire externe. "
        "Traitement des données, entraînement, validation et restitution des résultats.",
        [("Python", "amber"), ("Random Forest", "green"), ("Time Series", "blue"), ("Neural Network", "slate")]), unsafe_allow_html=True)
    st.markdown(mission_block("⚙️ Automatisation & amélioration de process",
        "Migration de traitements existants d'Excel vers Python pour gagner en fiabilité. "
        "Soutien aux prévisionnistes par l'automatisation de tâches récurrentes et études comportementales consommateurs.",
        [("Python", "amber"), ("Automatisation", "slate"), ("Data Analyse", "blue"), ("Communication", "rose")]), unsafe_allow_html=True)
 
    st.divider()
 
    # HUPI
    st.markdown("""
    <div class="exp-header">
        <div class="exp-logo" style="background:#eff6ff">📦</div>
        <div>
            <div class="exp-htitle">Stage – Data Scientist Junior</div>
            <div class="exp-hsubtitle">HUPI Iberica · Donostia, Espagne · Mai – Août 2022</div>
            <div class="exp-hdesc">Stage de 4 mois en immersion au sein d'une équipe de data scientists à Donostia (Saint-Sébastien). Expérience doublement formatrice : techniquement et linguistiquement.</div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(mission_block("🚚 Outil de pricing transport",
        "Contribution à un outil de pricing pour un intermédiaire entre sociétés de livraison et transporteurs. "
        "Mise en place d'un modèle Random Forest pour la prédiction du coût de transport, modélisation mathématique et création d'indicateurs visuels.",
        [("Python", "amber"), ("Random Forest", "green"), ("SQL", "blue"), ("Data Visualisation", "slate"), ("Communication", "rose")]), unsafe_allow_html=True)
    st.markdown(mission_block("🤝 Accompagnement data scientists senior",
        "Participation aux missions quotidiennes : traitement de données SQL, modélisation Python, outils de visualisation. "
        "Amélioration significative du niveau d'espagnol en contexte professionnel.",
        [("SQL", "blue"), ("Python", "amber"), ("Espagnol C1", "rose")]), unsafe_allow_html=True)
 
    st.divider()
 
    # BIGARD
    st.markdown("""
    <div class="exp-header">
        <div class="exp-logo" style="background:#f0fdf4">📊</div>
        <div>
            <div class="exp-htitle">Stage – Statisticien Junior</div>
            <div class="exp-hsubtitle">BIGARD · Quimperlé, France · Juin – Août 2021</div>
            <div class="exp-hdesc">Premier stage en entreprise au sein d'un abattoir porcin. Exploration statistique sur de grands volumes de données avec restitution aux équipes métier.</div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(mission_block("🔍 Analyse statistique des comportements atypiques",
        "Étude approfondie des données de production pour identifier les comportements atypiques dans le processus d'abattage. "
        "Exploration, nettoyage et analyse de bases volumineuses, puis présentation des résultats sous forme lisible aux responsables.",
        [("Python", "amber"), ("Statistiques", "blue"), ("Bases de données", "slate"), ("Communication", "rose")]), unsafe_allow_html=True)
 
# ═══ TAB 4 – AIRBREIZH ════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown('<div class="page-eyebrow">Sept 2023 – Sept 2025 · CDD 2 ans</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="page-title">AirBreizh</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="exp-header">
        <div class="exp-logo" style="background:#ecfdf5">💨</div>
        <div>
            <div class="exp-htitle">Ingénieur en Modélisation</div>
            <div class="exp-hsubtitle">AirBreizh · Rennes · Pôle Data & Technique</div>
            <div class="exp-hdesc">Association de surveillance de la qualité de l'air en Bretagne (&lt;30 salariés),
            avec des stations de mesure implantées sur tout le territoire régional.
            Structure pluridisciplinaire (pôles technique, data, études) favorisant des échanges riches.
            Interactions régulières avec le responsable infrastructure réseau — découverte fondamentale
            des notions de serveurs et VMs, déterminantes pour la suite du parcours.</div>
        </div>
    </div>""", unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Missions</div>', unsafe_allow_html=True)
 
    st.markdown(mission_block("📡 Outil de visualisation des stations (Grafana / InfluxDB)",
        "Construction d'un outil de visualisation interne des mesures et métriques techniques des stations de surveillance. "
        "Traitement Python des données, mise en forme pour stockage dans InfluxDB, intégration dans Grafana via passerelle dédiée. "
        "Automatisation par crontab. Discussions techniques avec les responsables pour définir les indicateurs pertinents. "
        "Enrichissement du système avec des données de comptage routier (microcapteurs + API) et météo (API Météo-France).",
        [("Python", "amber"), ("InfluxDB", "blue"), ("Grafana", "blue"), ("Crontab", "slate"), ("API REST", "green"), ("Communication", "rose")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("🚗 Simulation du trafic routier breton (MATSim / SIRANE)",
        "Prise en main et paramétrage du simulateur open-source MATSim pour modéliser le trafic à l'échelle régionale. "
        "Post-traitement des sorties par la méthode des plus proches voisins pour intégrer les données de comptage fixe. "
        "Développement sous Jupyter Notebook, travail collaboratif sur GitHub. "
        "Lancement de simulations SIRANE pour calculer les émissions de GES à partir des flux routiers. "
        "Participation à une plénière à l'École Supérieure de Lyon.",
        [("MATSim", "rose"), ("SIRANE", "rose"), ("Python", "amber"), ("GitHub", "slate"), ("Jupyter", "amber"), ("Plus proches voisins", "blue")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("🗺️ Données cartographiques & géospatiales",
        "Découverte et manipulation de données cartographiques : GeoPackage et QGIS pour la visualisation et l'analyse spatiale des flux de trafic et des données qualité de l'air.",
        [("QGIS", "green"), ("GeoPackage", "green"), ("Géospatial", "slate")]), unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Stack technique</div>', unsafe_allow_html=True)
    st.markdown(mixed_tags([
        ("Python", "amber"), ("InfluxDB", "blue"), ("Grafana", "blue"), ("MATSim", "rose"),
        ("SIRANE", "rose"), ("QGIS", "green"), ("GitHub", "slate"), ("Jupyter", "amber"),
        ("API REST", "green"), ("Crontab", "slate"), ("Calcul parallélisé", "blue"),
    ]), unsafe_allow_html=True)
 
# ═══ TAB 5 – AUDAP ════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown('<div class="page-eyebrow">Oct 2025 – Aujourd\'hui</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="page-title">AUDAP</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="exp-header">
        <div class="exp-logo" style="background:#fef3c7">🏙️</div>
        <div>
            <div class="exp-htitle">Data Analyst · Responsable Infrastructure Réseau</div>
            <div class="exp-hsubtitle">AUDAP · Bayonne · Oct 2025 – Présent</div>
            <div class="exp-hdesc">Agence d'urbanisme du Pays Basque et des Pyrénées-Atlantiques.
            Poste à double casquette : missions d'analyse de données et de construction d'outils livrables,
            et responsabilité croissante de l'infrastructure réseau interne.</div>
        </div>
    </div>""", unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Missions Data</div>', unsafe_allow_html=True)
 
    st.markdown(mission_block("🛣️ Metrosat – Suivi des temps de trajet routiers",
        "Récupération automatisée via API Google des temps de trajet sur différents tronçons routiers, "
        "enrichis des données météo (API). Automatisation Python + crontab pour alimenter une base SQL, "
        "servant à la construction d'un Power BI clef en main livré aux partenaires.",
        [("Python", "amber"), ("API Google", "blue"), ("SQL", "blue"), ("Power BI", "rose"), ("Crontab", "slate")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("📊 Indicateur de Vitalité des Communes (IVR)",
        "Construction d'un outil de scoring des communes selon leur vitalité. "
        "Récupération et traitement de données INSEE en Python, élaboration d'un Power BI complet pour restitution aux partenaires.",
        [("Python", "amber"), ("INSEE", "slate"), ("Scoring", "green"), ("Power BI", "rose")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("🌡️ Rapports réchauffement climatique",
        "Études d'indicateurs de réchauffement climatique en notebook Python. Traitement, analyse et restitution sous forme de rapports exploitables.",
        [("Python", "amber"), ("Jupyter", "amber"), ("Data Analyse", "blue")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("🌄 Observatoire Pays de Béarn (pilotage de mission)",
        "Accompagnement de deux stagiaires dans la construction d'un observatoire territorial : "
        "sélection des indicateurs, modélisations, structuration du livrable final.",
        [("Management", "rose"), ("Power BI", "rose"), ("Indicateurs territoriaux", "slate")]), unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Pilote IA & Infrastructure</div>', unsafe_allow_html=True)
 
    st.markdown(mission_block("🤖 Pilote de mission IA",
        "Référent sur l'intégration de l'IA au sein de l'AUDAP : veille technologique, enquête interne, "
        "réflexion sur les usages et les outils adaptés au contexte de l'agence.",
        [("IA", "green"), ("Veille", "slate"), ("Pilotage", "rose")]), unsafe_allow_html=True)
 
    st.markdown(mission_block("🖥️ Responsable Infrastructure Réseau",
        "Diagnostic complet de l'infrastructure héritée (VMs non maintenues, applications obsolètes dont PostgreSQL). "
        "Réalisation de la migration des serveurs — forte montée en compétences sur l'administration système. "
        "Capitalisation des acquis d'AirBreizh et usage de l'IA comme levier d'apprentissage.",
        [("VMs", "slate"), ("PostgreSQL", "blue"), ("Migration serveurs", "rose"), ("Administration système", "slate")]), unsafe_allow_html=True)
 
    st.markdown('<div class="section-head">Stack technique</div>', unsafe_allow_html=True)
    st.markdown(mixed_tags([
        ("Python", "amber"), ("SQL", "blue"), ("Power BI", "rose"), ("API REST", "green"),
        ("Crontab", "slate"), ("VMs", "slate"), ("PostgreSQL", "blue"), ("IA", "green"),
        ("Jupyter", "amber"), ("Pilotage", "rose"),
    ]), unsafe_allow_html=True)