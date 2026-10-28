"""Build the site in English (/) and French (/fr/).

Edit the text in CONTENT below, then run:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://georgialoukatou.github.io"
EMAIL = "georgial@botiqueai.com"
CALENDLY = "https://calendly.com/hello-botiqueai/30min"
LINKEDIN = "https://www.linkedin.com/in/georgia-loukatou/"
SCHOLAR = "https://scholar.google.com/citations?user=S5Yad6wAAAAJ&amp;hl=en"
SPOTIFY = "https://open.spotify.com/episode/1CCXQMo2HDLczHjX9s8Fl1"
LANGS = {"en": "/", "fr": "/fr/"}
LANG_LABEL = {"en": "EN", "fr": "FR"}

PUBLICATIONS = [
    "<strong>Loukatou, G.</strong>, Stoll, S., Blasi, D., &amp; Cristia, A. (2022). Does morphological complexity affect word segmentation? Evidence from computational modeling. <em>Cognition</em>, 220.",
    "<strong>Loukatou, G.*</strong>, Tan, A.W.M.*, Braginsky, M., Mankewitz, J., &amp; Frank, M.C. (2024). Predicting ages of acquisition for children's early vocabulary across 27 languages and dialects. <em>CogSci 2024</em>.",
    "<strong>Loukatou, G.</strong>, Kachergis, G., &amp; Frank, M.C. (2022). Identifying the distributional sources of children's early vocabulary. <em>CogSci 2022</em>.",
    "<strong>Loukatou, G.</strong>, Stoll, S., Blasi, D., &amp; Cristia, A. (2019). Is Word Segmentation Child's Play in All Languages? <em>ACL 2019</em>, Florence.",
]

CONTENT = {
# ───────────────────────────── ENGLISH ─────────────────────────────
"en": {
  "title": "Georgia Loukatou · AI Engineer &amp; Co-Founder of BotiqueAI",
  "desc": "Georgia Loukatou, AI Engineer, Co-Founder of BotiqueAI and PhD (ENS Paris). 9 years bridging AI research and industry: AI strategy advisory and custom AI systems.",
  "skip": "Skip to content",
  "name": "Georgia Loukatou",
  "eyebrow": "AI Engineer · AI Adoption Lead · PhD · Co-Founder",
  "lead": "I help companies adopt AI where it genuinely helps, from strategy and roadmaps to production systems that people actually use.",
  "points": ["9 years bridging AI research and industry.",
             "I advise executives on AI integration strategy and build custom AI systems.",
             "PhD in AI from ENS Paris, with publications in ACL and <em>Cognition</em>."],
  "book": "Book a call", "email_btn": "Email me", "cii": "CII-certified",
  "stats": [("9 years", "AI research &amp; industry"), ("20+", "companies advised, 10+ sectors"), ("PhD", "AI, ENS Paris")],
  "tabs": {"experience": "Experience", "teaching": "Teaching &amp; Speaking", "publications": "Publications", "about": "About"},
  "h": {"now": "Now", "prev": "Previously", "edu": "Education", "podcast": "Podcast", "talks": "Talks &amp; Events",
        "teaching": "Teaching", "pubs": "Selected Publications", "beyond": "Beyond Work"},
  "now": [
    {"logo": "botiqueai.png", "role": "Co-Founder", "org": "BotiqueAI, Paris", "date": "2025 – Present",
     "body": ["An AI consulting studio helping companies navigate AI adoption, from strategic advisory and integration roadmaps to end-to-end delivery of production AI systems (agents, RAG, chatbots). Clients span <strong>20+ companies across 10+ sectors</strong>, including retail, hospitality, legal and education.",
              "Key project: <strong>Aria</strong>, an AI chatbot platform for Shopify and WordPress merchants, with 24/7 customer support, real-time product search and lead capture."],
     "chips": ["Agentic AI", "RAG", "AI Strategy", "Chatbots"],
     "links": [("Watch the Aria demo →", "https://www.youtube.com/watch?v=iWUjmfBZiLE"), ("botiqueai.com", "https://www.botiqueai.com/"),
               ("LinkedIn", "https://www.linkedin.com/company/botique-ai"), ("Instagram", "https://www.instagram.com/botiqueai/")]},
    {"logo": "thefork.png", "role": "Lead AI Engineer", "org": "TheFork, a Tripadvisor company", "date": "2025 – Present",
     "body": ["Owned the product vision of <strong>AskTheFork</strong>, an AI-powered restaurant discovery experience that replaces traditional filters with natural-language search. It interprets complex queries by analysing menus, photos and reviews via RAG, and shipped with a <strong>5% higher conversion rate</strong>.",
              "Led the full architecture (LangGraph, GPT-4o, OpenSearch), built an LLM restaurant classifier across 300 tags and evaluation pipelines (Arize, custom metrics), upskilled engineers on AI, and defined the team's AI roadmap with the Head of AI and Product."],
     "chips": ["LangGraph", "LLM Evaluation", "Semantic Search"],
     "links": [("Read the case study →", "https://www.media.thiga.co/en/ai-strategy-why-thefork-ditched-the-chatbot")]},
  ],
  "prev": [
    ("acolad.png", "AI Engineer · Acolad Group, Paris", "2024 – 2025",
     "European leader in language and content services. Led AI adoption and defined the roadmap with the Head of AI and PM. Shipped agentic RAG translation (LangChain, BentoML, vector search) with a <strong>40% quality improvement</strong> and zero human intervention, an internal AI assistant, and an LLM-as-a-Judge quality validation system."),
    ("qlip-ai.png", "Founding ML Engineer · qlip.ai, Station F", "2022 – 2024",
     "First hire at an AI startup building a video highlights generator. Built the full ML pipeline from scratch (topic modeling, sentiment analysis, summarization, multilingual LLM integration on AWS) and took product decisions as part of the founding team."),
    ("stanford.png", "Data Scientist · Language &amp; Cognition Lab, Stanford University", "2020 – 2022",
     "NLP research on language acquisition across typologically diverse languages, with large-scale datasets (<strong>1 billion words, 70,000 reports, 17 languages</strong>). Collaborated with Stanford HAI; published at CogSci and a NeurIPS workshop. <strong>Fyssen Foundation Fellow</strong>, a competitive international postdoctoral grant."),
    ("ens.png", "AI Researcher · École Normale Supérieure (ENS), Paris", "2017 – 2020",
     "Unsupervised NLP for low-resource language segmentation, achieving <strong>+30% accuracy</strong> with the University of Zurich. Published in ACL, <em>Cognition</em>, CogSci and TALN. Supervised 7 research interns. <strong>PRAIRIE member</strong> (Paris Artificial Intelligence Research Institute) since 2020."),
  ],
  "edu": [
    ("ens.png", "Ph.D., Artificial Intelligence", "École Normale Supérieure (ENS), Paris · 2020", "Félicitations du jury à l'unanimité. Selective doctoral funding (ED3C)."),
    ("universit-de-paris.png", "M.Sc., Natural Language Processing", "Université Paris Diderot · 2017", "Class rank: top 20%."),
  ],
  "podcast": {"kicker": "New · October 2026",
              "show": "Guest on <em>Does Anyone Think Anymore?</em> with Ashley Portillo",
              "body": "How can a small business use AI to save time without losing what makes it valuable? I talk about how we help businesses find practical use cases, test solutions and build them into everyday workflows. We also cover employee training, AI ambassadors, data protection, job concerns, and the shift toward reviewing and supervising AI.",
              "btn": "Listen on Spotify →",
              "alt": "Georgia Loukatou and Ashley Portillo recording the podcast Does Anyone Think Anymore?"},
  "malt": {"role": "Invited speaker", "org": "Malt × BotiqueAI · 2025",
           "body": "Enterprise AI enablement for freelancers and businesses: RAG architecture, agentic design, evaluation frameworks and human handoff.",
           "link": "Watch: AI Chatbot Strategy That Scales →", "alt": "Georgia Loukatou speaking in a Malt video"},
  "legrain": ("Moderator &amp; Session Organizer", "Olivier Legrain Conference · 2018",
              "Organized and moderated the NLP and Chatbots round table with M. Baroni, F. Yvon, F. Béchet and others, plus an Industrial Challenges session."),
  "teaching": [
    ("sup-de-vinci.png", "NLP &amp; AI Instructor", "Sup de Vinci, Paris · 2024",
     "Designed and taught a 35-hour NLP and Generative AI course for Master 2 Data Science students: transformers, LLMs, embeddings, prompt engineering, RAG and conversational AI."),
    ("openclassrooms.png", "Data Science Mentor", "OpenClassrooms · 2022 – 2024",
     "Mentored professionals through Data Science and Machine Learning certification projects and career transitions into AI/ML."),
    ("ens.png", "Teaching Assistant", "CogMaster, ENS Paris · 2019 – 2020",
     "Language Processing &amp; Acquisition, Advanced Master."),
  ],
  "scholar": "Full list on Google Scholar →",
  "beyond": ["Trained in theater and critical thinking for science communication. Communicating AI well matters as much as building it.",
             "Classically trained musician, with degrees in Piano Performance and in Harmony, Theory &amp; Composition.",
             "Traveled to 50+ countries, and counting."],
  "cta_title": "Work with me",
  "cta_chips": ["AI Strategy &amp; Advisory", "Custom AI Systems", "Speaking &amp; Workshops", "AI Training &amp; Enablement"],
  "cta_body": "I help companies navigate AI strategy and build systems that deliver real value. Whether you need hands-on engineering, executive advisory, or a talk that cuts through the hype, let's talk.",
  "footer": "Georgia Loukatou · Paris, France",
  "photo_alt": "Portrait of Georgia Loukatou",
},
# ───────────────────────────── FRANÇAIS ─────────────────────────────
"fr": {
  "title": "Georgia Loukatou · Ingénieure IA &amp; cofondatrice de BotiqueAI",
  "desc": "Georgia Loukatou, ingénieure IA, cofondatrice de BotiqueAI et docteure de l'ENS Paris. 9 ans entre recherche en IA et industrie : conseil en stratégie IA et systèmes d'IA sur mesure.",
  "skip": "Aller au contenu",
  "name": "Georgia Loukatou",
  "eyebrow": "Ingénieure IA · Responsable adoption de l'IA · Docteure · Cofondatrice",
  "lead": "J'aide les entreprises à adopter l'IA là où elle apporte vraiment quelque chose, de la stratégie et de la feuille de route jusqu'aux systèmes en production réellement utilisés.",
  "points": ["9 ans entre recherche en IA et industrie.",
             "Je conseille les dirigeants sur leur stratégie d'intégration de l'IA et je conçois des systèmes d'IA sur mesure.",
             "Doctorat en IA à l'ENS Paris, avec des publications à ACL et dans <em>Cognition</em>."],
  "book": "Prendre rendez-vous", "email_btn": "M'écrire", "cii": "Agréée CII",
  "stats": [("9 ans", "recherche en IA &amp; industrie"), ("20+", "entreprises accompagnées, 10+ secteurs"), ("Doctorat", "IA, ENS Paris")],
  "tabs": {"experience": "Expérience", "teaching": "Enseignement &amp; interventions", "publications": "Publications", "about": "À propos"},
  "h": {"now": "Aujourd'hui", "prev": "Auparavant", "edu": "Formation", "podcast": "Podcast", "talks": "Conférences &amp; événements",
        "teaching": "Enseignement", "pubs": "Publications choisies", "beyond": "En dehors du travail"},
  "now": [
    {"logo": "botiqueai.png", "role": "Cofondatrice", "org": "BotiqueAI, Paris", "date": "2025 – aujourd'hui",
     "body": ["Studio de conseil en IA qui accompagne les entreprises dans l'adoption de l'IA, du conseil stratégique et des feuilles de route d'intégration jusqu'à la livraison de systèmes d'IA en production (agents, RAG, chatbots). Plus de <strong>20 entreprises clientes dans plus de 10 secteurs</strong>, dont le commerce, l'hôtellerie, le juridique et l'éducation.",
              "Projet phare : <strong>Aria</strong>, une plateforme de chatbot IA pour les marchands Shopify et WordPress, avec support client 24h/24, recherche de produits en temps réel et capture de leads."],
     "chips": ["IA agentique", "RAG", "Stratégie IA", "Chatbots"],
     "links": [("Voir la démo d'Aria →", "https://www.youtube.com/watch?v=iWUjmfBZiLE"), ("botiqueai.com", "https://www.botiqueai.com/"),
               ("LinkedIn", "https://www.linkedin.com/company/botique-ai"), ("Instagram", "https://www.instagram.com/botiqueai/")]},
    {"logo": "thefork.png", "role": "Lead AI Engineer", "org": "TheFork, une entreprise Tripadvisor", "date": "2025 – aujourd'hui",
     "body": ["Responsable de la vision produit d'<strong>AskTheFork</strong>, une expérience de découverte de restaurants propulsée par l'IA qui remplace les filtres traditionnels par une recherche en langage naturel. Elle interprète des requêtes complexes en analysant menus, photos et avis via RAG, et a été lancée avec un <strong>taux de conversion supérieur de 5 %</strong>.",
              "Pilotage de toute l'architecture (LangGraph, GPT-4o, OpenSearch), conception d'un classifieur de restaurants par LLM sur 300 tags et de pipelines d'évaluation (Arize, métriques sur mesure), montée en compétences des ingénieurs sur l'IA et définition de la feuille de route IA de l'équipe avec le Head of AI et le Produit."],
     "chips": ["LangGraph", "Évaluation de LLM", "Recherche sémantique"],
     "links": [("Lire l'étude de cas →", "https://www.media.thiga.co/en/ai-strategy-why-thefork-ditched-the-chatbot")]},
  ],
  "prev": [
    ("acolad.png", "Ingénieure IA · Acolad Group, Paris", "2024 – 2025",
     "Leader européen des services linguistiques et de contenu. Pilotage de l'adoption de l'IA et définition de la feuille de route avec le Head of AI et le PM. Mise en production d'une traduction par RAG agentique (LangChain, BentoML, recherche vectorielle) avec <strong>40 % d'amélioration de la qualité</strong> sans intervention humaine, d'un assistant IA interne et d'un système de validation qualité LLM-as-a-Judge."),
    ("qlip-ai.png", "Founding ML Engineer · qlip.ai, Station F", "2022 – 2024",
     "Première recrue d'une startup IA développant un générateur de temps forts vidéo. Construction de tout le pipeline ML de zéro (topic modeling, analyse de sentiment, résumé automatique, intégration de LLM multilingues sur AWS) et participation aux décisions produit au sein de l'équipe fondatrice."),
    ("stanford.png", "Data Scientist · Language &amp; Cognition Lab, Université Stanford", "2020 – 2022",
     "Recherche en TAL sur l'acquisition du langage dans des langues typologiquement variées, sur des données à grande échelle (<strong>1 milliard de mots, 70 000 rapports, 17 langues</strong>). Collaboration avec Stanford HAI ; publications à CogSci et dans un workshop NeurIPS. <strong>Lauréate de la Fondation Fyssen</strong>, bourse postdoctorale internationale très sélective."),
    ("ens.png", "Chercheuse en IA · École normale supérieure (ENS), Paris", "2017 – 2020",
     "TAL non supervisé pour la segmentation de langues peu dotées, avec <strong>+30 % de précision</strong> en collaboration avec l'Université de Zurich. Publications à ACL, dans <em>Cognition</em>, à CogSci et TALN. Encadrement de 7 stagiaires de recherche. <strong>Membre de PRAIRIE</strong> (Institut de recherche en intelligence artificielle de Paris) depuis 2020."),
  ],
  "edu": [
    ("ens.png", "Doctorat en intelligence artificielle", "École normale supérieure (ENS), Paris · 2020", "Félicitations du jury à l'unanimité. Contrat doctoral obtenu sur concours (ED3C)."),
    ("universit-de-paris.png", "Master en traitement automatique des langues", "Université Paris Diderot · 2017", "Classée dans les 20 % premiers de la promotion."),
  ],
  "podcast": {"kicker": "Nouveau · octobre 2026",
              "show": "Invitée de <em>Does Anyone Think Anymore?</em> avec Ashley Portillo (épisode en anglais)",
              "body": "Comment une petite entreprise peut-elle utiliser l'IA pour gagner du temps sans perdre ce qui fait sa valeur ? J'explique comment nous aidons les entreprises à identifier des cas d'usage concrets, à tester des solutions et à les intégrer dans leur quotidien. Nous parlons aussi de formation des équipes, d'ambassadeurs IA, de protection des données, des inquiétudes sur l'emploi et du passage à un rôle de relecture et de supervision de l'IA.",
              "btn": "Écouter sur Spotify →",
              "alt": "Georgia Loukatou et Ashley Portillo pendant l'enregistrement du podcast Does Anyone Think Anymore?"},
  "malt": {"role": "Intervenante invitée", "org": "Malt × BotiqueAI · 2025",
           "body": "L'IA en entreprise pour les freelances et les entreprises : architecture RAG, conception agentique, cadres d'évaluation et passage de relais à l'humain.",
           "link": "Voir : AI Chatbot Strategy That Scales →", "alt": "Georgia Loukatou dans une vidéo Malt"},
  "legrain": ("Modératrice et organisatrice de sessions", "Conférence Olivier Legrain · 2018",
              "Organisation et modération de la table ronde TAL et chatbots avec M. Baroni, F. Yvon, F. Béchet et d'autres, ainsi que d'une session sur les défis industriels."),
  "teaching": [
    ("sup-de-vinci.png", "Enseignante en TAL et IA", "Sup de Vinci, Paris · 2024",
     "Conception et enseignement d'un cours de 35 heures sur le TAL et l'IA générative pour des étudiants de Master 2 Data Science : transformers, LLM, embeddings, prompt engineering, RAG et IA conversationnelle."),
    ("openclassrooms.png", "Mentore Data Science", "OpenClassrooms · 2022 – 2024",
     "Accompagnement de professionnels dans leurs projets de certification en Data Science et Machine Learning et dans leur reconversion vers l'IA."),
    ("ens.png", "Chargée de TD", "CogMaster, ENS Paris · 2019 – 2020",
     "Traitement et acquisition du langage, master avancé."),
  ],
  "scholar": "Liste complète sur Google Scholar →",
  "beyond": ["Formée au théâtre et à l'esprit critique pour la médiation scientifique. Bien expliquer l'IA compte autant que la construire.",
             "Musicienne de formation classique, diplômée en interprétation au piano ainsi qu'en harmonie, théorie et composition.",
             "Plus de 50 pays visités, et ce n'est pas fini."],
  "cta_title": "Travaillons ensemble",
  "cta_chips": ["Stratégie &amp; conseil IA", "Systèmes d'IA sur mesure", "Conférences &amp; ateliers", "Formation &amp; acculturation IA"],
  "cta_body": "J'aide les entreprises à définir leur stratégie IA et à construire des systèmes qui apportent une vraie valeur. Que vous ayez besoin d'ingénierie, de conseil auprès de la direction ou d'une intervention qui va au-delà des effets d'annonce, parlons-en.",
  "footer": "Georgia Loukatou · Paris, France",
  "photo_alt": "Portrait de Georgia Loukatou",
},
}

EXT = 'target="_blank" rel="noopener"'


def chips(items, cls="chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{c}</li>" for c in items) + "</ul>"


def render(lang):
    c = CONTENT[lang]
    alt_links = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">' for l, p in LANGS.items())
    switch = "".join(
        f'<a href="{p}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else "") + f">{LANG_LABEL[l]}</a>"
        for l, p in LANGS.items())
    tabs = "".join(
        f'<button role="tab" id="tab-{k}" aria-controls="panel-{k}" data-tab="{k}">{v}</button>' for k, v in c["tabs"].items())

    now_cards = ""
    for r in c["now"]:
        body = "".join(f"<p>{p}</p>" for p in r["body"])
        links = "".join(f'<a href="{u}" {EXT}>{t}</a>' for t, u in r["links"])
        now_cards += f'''
        <article class="card">
          <header class="card-head">
            <img src="/assets/{r["logo"]}" alt="" width="44" height="44">
            <div><h4>{r["role"]}</h4><p class="org">{r["org"]}</p></div>
            <span class="date">{r["date"]}</span>
          </header>
          {body}
          {chips(r["chips"])}
          <p class="links">{links}</p>
        </article>'''

    timeline = "".join(f'''
        <li>
          <img src="/assets/{logo}" alt="" width="36" height="36">
          <div>
            <div class="tl-head"><h4>{title}</h4><span class="date">{date}</span></div>
            <p>{desc}</p>
          </div>
        </li>''' for logo, title, date, desc in c["prev"])

    edu = "".join(f'''
        <li>
          <img src="/assets/{logo}" alt="" width="36" height="36">
          <div><h4>{t}</h4><p class="org">{o}</p><p>{d}</p></div>
        </li>''' for logo, t, o, d in c["edu"])

    teach = "".join(f'''
        <article class="card compact">
          <header class="card-head"><img src="/assets/{logo}" alt="" width="36" height="36"><div><h4>{role}</h4><p class="org">{org}</p></div></header>
          <p>{desc}</p>
        </article>''' for logo, role, org, desc in c["teaching"])

    pubs = "".join(f"<li><span>{p}</span></li>" for p in PUBLICATIONS)
    beyond = "".join(f"<p>{b}</p>" for b in c["beyond"])
    pc, m, lg = c["podcast"], c["malt"], c["legrain"]
    stats = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["stats"])
    points = "".join(f"<li>{p}</li>" for p in c["points"])
    h = c["h"]

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["title"]}</title>
<meta name="description" content="{c["desc"]}">
<link rel="canonical" href="{SITE}{LANGS[lang]}">
{alt_links}
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{LANGS[lang]}">
<meta property="og:title" content="{c["title"]}">
<meta property="og:description" content="{c["desc"]}">
<meta property="og:image" content="{SITE}/assets/georgia.jpg">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip" href="#main">{c["skip"]}</a>

<nav class="nav" aria-label="Main">
  <div class="wrap nav-inner">
    <a class="monogram" href="{LANGS[lang]}" aria-label="{c["name"]}">GL</a>
    <div class="lang-switch" aria-label="Language">{switch}</div>
    <a class="btn btn-small" href="{CALENDLY}" {EXT}>{c["book"]}</a>
  </div>
</nav>

<header class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <p class="eyebrow">{c["eyebrow"]}</p>
      <h1>{c["name"]}</h1>
      <p class="lead">{c["lead"]}</p>
      <ul class="hero-points">{points}</ul>
      <div class="cta-row">
        <a class="btn" href="{CALENDLY}" {EXT}>{c["book"]}</a>
        <a class="btn btn-ghost" href="{LINKEDIN}" {EXT}>LinkedIn</a>
        <a class="btn btn-ghost" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <span class="cii-badge">{c["cii"]}</span>
    </div>
    <div class="hero-photo"><img src="/assets/georgia.jpg" alt="{c["photo_alt"]}" width="300" height="300"></div>
  </div>
  <div class="wrap"><dl class="stats">{stats}</dl></div>
</header>

<main id="main" class="tabs-area">
  <div class="tabbar-wrap">
    <div class="wrap"><div class="tabbar" role="tablist">{tabs}</div></div>
  </div>

  <!-- EXPERIENCE -->
  <div class="panel" role="tabpanel" id="panel-experience" aria-labelledby="tab-experience">
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">01</span>{h["now"]}</h2>
        <div class="cards two">{now_cards}</div>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">02</span>{h["prev"]}</h2>
        <ol class="timeline">{timeline}</ol>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">03</span>{h["edu"]}</h2>
        <ul class="edu">{edu}</ul>
      </div>
    </section>
  </div>

  <!-- TEACHING & SPEAKING -->
  <div class="panel" role="tabpanel" id="panel-teaching" aria-labelledby="tab-teaching">
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">01</span>{h["podcast"]}</h2>
        <article class="feature">
          <a class="feature-media" href="{SPOTIFY}" {EXT}><img src="/assets/podcast.jpg" alt="{pc["alt"]}" width="1600" height="892" loading="lazy"></a>
          <div class="feature-body">
            <p class="kicker"><span class="new">{pc["kicker"]}</span></p>
            <h3>How Small Businesses Can Adopt AI Without Losing the Human Touch</h3>
            <p class="show">{pc["show"]}</p>
            <p>{pc["body"]}</p>
            <a class="btn" href="{SPOTIFY}" {EXT}>{pc["btn"]}</a>
          </div>
        </article>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">02</span>{h["talks"]}</h2>
        <div class="talks">
          <article class="talk">
            <a class="talk-media" href="https://www.youtube.com/watch?v=tpxlaazMlQc" {EXT}><img src="/assets/malt-talk.jpg" alt="{m["alt"]}" width="730" height="1300" loading="lazy"></a>
            <div>
              <header class="card-head"><img src="/assets/malt.png" alt="" width="36" height="36"><div><h4>{m["role"]}</h4><p class="org">{m["org"]}</p></div></header>
              <p>{m["body"]}</p>
              <p class="links"><a href="https://www.youtube.com/watch?v=tpxlaazMlQc" {EXT}>{m["link"]}</a></p>
            </div>
          </article>
          <article class="card compact">
            <header class="card-head"><img src="/assets/legrain-conference.png" alt="" width="36" height="36"><div><h4>{lg[0]}</h4><p class="org"><a href="https://olivierlegrain.ens.psl.eu/" {EXT}>{lg[1]}</a></p></div></header>
            <p>{lg[2]}</p>
          </article>
        </div>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">03</span>{h["teaching"]}</h2>
        <div class="cards three">{teach}</div>
      </div>
    </section>
  </div>

  <!-- PUBLICATIONS -->
  <div class="panel" role="tabpanel" id="panel-publications" aria-labelledby="tab-publications">
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">01</span>{h["pubs"]}</h2>
        <ol class="pubs">{pubs}</ol>
        <p class="links"><a href="{SCHOLAR}" {EXT}>{c["scholar"]}</a></p>
      </div>
    </section>
  </div>

  <!-- ABOUT -->
  <div class="panel" role="tabpanel" id="panel-about" aria-labelledby="tab-about">
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">01</span>{h["beyond"]}</h2>
        <div class="beyond">{beyond}</div>
      </div>
    </section>
  </div>
</main>

<section class="cta-section" id="contact">
  <div class="wrap">
    <div class="cta">
      <h2>{c["cta_title"]}</h2>
      {chips(c["cta_chips"], "chips light")}
      <p>{c["cta_body"]}</p>
      <div class="cta-row">
        <a class="btn btn-light" href="{CALENDLY}" {EXT}>{c["book"]}</a>
        <a class="btn btn-outline-light" href="mailto:{EMAIL}">{c["email_btn"]}</a>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="wrap footer-inner">
    <p>© <span id="year">2026</span> {c["footer"]}</p>
    <p class="links">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{LINKEDIN}" {EXT}>LinkedIn</a>
      <a href="https://www.botiqueai.com/" {EXT}>BotiqueAI</a>
      <a href="{SCHOLAR}" {EXT}>Google Scholar</a>
    </p>
  </div>
</footer>

<script>
(function () {{
  document.getElementById('year').textContent = new Date().getFullYear();
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  var ids = tabs.map(function (t) {{ return t.dataset.tab; }});
  function show(id, focus) {{
    if (ids.indexOf(id) < 0) id = ids[0];
    tabs.forEach(function (t) {{
      var on = t.dataset.tab === id;
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      document.getElementById('panel-' + t.dataset.tab).hidden = !on;
      if (on && focus) t.focus();
    }});
  }}
  tabs.forEach(function (t, i) {{
    t.addEventListener('click', function () {{
      show(t.dataset.tab);
      history.replaceState(null, '', '#' + t.dataset.tab);
      var bar = document.querySelector('.tabbar-wrap');
      if (bar.getBoundingClientRect().top < 0) bar.scrollIntoView({{behavior: 'smooth'}});
    }});
    t.addEventListener('keydown', function (e) {{
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (d) {{ var n = tabs[(i + d + tabs.length) % tabs.length]; show(n.dataset.tab, true); history.replaceState(null, '', '#' + n.dataset.tab); }}
    }});
  }});
  show(location.hash.slice(1));
  window.addEventListener('hashchange', function () {{ show(location.hash.slice(1)); }});
  // keep the open tab when switching language
  document.querySelectorAll('.lang-switch a').forEach(function (a) {{
    a.addEventListener('click', function () {{ if (location.hash) a.href = a.getAttribute('href') + location.hash; }});
  }});
}})();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    for lang, path in LANGS.items():
        out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
