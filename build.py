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

# LinkedIn posts shown on /posts/ (newest first). Blocks: a string = paragraph, ("ul"|"ol", [items]) = list.
POSTS = [
  {"date": (2025, 12, 8), "title": "Agent in Production Reality Check: Reliability &gt; Autonomy",
   "body": ["A new study of 306 practitioners across 26 domains confirms what many of us have experienced: reliability beats autonomy every single time.",
            ("ol", ["<strong>Structure over freestyling.</strong> The most successful agents aren't self-determining their paths. 80% of them use structured, static workflows. In production, success is found in predictable subtasks.",
                    "<strong>Reliability is the #1 challenge.</strong> Teams implement massive guardrails, human-written prompts and strict manual control loops over automated, stochastic methods.",
                    "<strong>Humans are the benchmark.</strong> Automated evaluation isn't there yet. 74% of teams rely on human-in-the-loop evaluation, because generic benchmarks can't handle domain-specific nuances.",
                    "<strong>Quality over latency.</strong> 66% of organizations trade speed for correctness, accepting response times of minutes to ensure the output outperforms human baselines."]),
            "Production-grade agents survive by operating within tight bounds. To make it to production, we often sacrifice open-ended autonomy for the win of predictability."],
   "links": [("Paper", "https://lnkd.in/eAM6tTsX")]},
  {"date": (2025, 10, 1), "title": "From Chaos to Control: A Two-Phase Playbook for Bulletproof LLM Evaluations",
   "body": ["Ever pushed a \"harmless\" prompt change that silently broke your LLM app? Traditional tests fall short for non-deterministic AI, so here is a continuous two-phase strategy to stay in control:",
            ("ol", ["<strong>Pre-launch safety net.</strong> Before shipping, run a curated, high-quality golden dataset through your CI/CD pipeline. This validates the quality of LLM outputs after any change in prompt, settings, or model version. It may combine deterministic checks (like verifying a keyword's presence) and LLM-as-a-Judge evaluations to catch regressions before they ever see a user.",
                    "<strong>Watching in the wild.</strong> Once in production, capture user traces and monitor performance through automated evaluations on real-world, recent data, running either continuously or on sampled batches (daily/weekly). Techniques like LLM-as-a-Judge enforce quality and safety at scale, complemented by others like semantic similarity, depending on the product's needs."]),
            "However, the real magic is the feedback loop. What we learn from Phase 2's production data (edge cases, user behaviors, or failure modes) is used to enrich Phase 1's golden dataset. This constant iteration elevates evaluation from a mere task to the engine that drives continuous improvement."],
   "links": [("Full playbook on the BotiqueAI blog", "https://www.botiqueai.com/")]},
  {"date": (2025, 9, 24), "title": "Why the Future of AI Agents is Small (and Smart)",
   "body": ["While LLMs get the spotlight, new NVIDIA research argues the future of AI agents is the Small Language Model (SLM). The reason is simple: most agentic tasks are repetitive, narrow, and structured. They don't always require the heavy compute and cost of LLMs.",
            "Why SLMs are useful for agentic AI:",
            ("ul", ["<strong>Powerful enough.</strong> Modern SLMs (e.g., Hugging Face SmolLM2) match larger models on agent tasks like reasoning and tool calling.",
                    "<strong>More economical and faster.</strong> With lower latency and 10-30x cheaper to run, they enable real-time responses with less cloud expenses. Fine-tuning is also dramatically faster.",
                    "<strong>Operationally superior.</strong> SLMs are perfect for edge and on-device AI, with better privacy and user control. They ensure easily formatted outputs for reliable tool use."]),
            "<strong>Suggested approach.</strong> The path forward isn't about replacing LLMs, but building smarter:",
            ("ul", ["Build hybrid, heterogeneous architectures: modular agents with a mix of models.",
                    "Fine-tune SLMs when possible for specific, high-volume skills.",
                    "Gradually migrate sub-agents and repetitive tasks from LLMs to SLMs."]),
            "<strong>The future is hybrid.</strong> This approach is more than a technical fix. It's a move toward responsible and sustainable AI that unlocks cost savings, broader accessibility, and more scalable systems."],
   "links": [("Paper: SLMs for Agentic AI", "https://lnkd.in/e7uKxbWV"), ("BotiqueAI blog", "https://lnkd.in/epsAVGNf")]},
  {"date": (2025, 6, 18), "title": "LLMs Get Lost in Conversation, and We're Not Evaluating That Enough",
   "body": ["A new large-scale study by Microsoft and Salesforce researchers reveals a critical issue some of us have experienced: LLMs perform on average 39% worse in multi-turn conversations compared to single-turn prompts.",
            "<strong>What's going wrong?</strong>",
            ("ul", ["LLMs jump to premature assumptions and cling to flawed prior outputs.",
                    "They rarely recover once off track.",
                    "Lowering temperature, even to zero, doesn't fix it.",
                    "Restarting conversations often works better than continuing them.",
                    "Consolidating instructions into one prompt helps, but that's unrealistic for most users."]),
            "Benchmarks still focus on fully-specified, single-turn tasks. Multi-turn evaluations are rare, often non-reproducible, and don't reflect real-world use. Let's shift the focus toward multi-turn robustness and reproducibility in model development and evaluation."],
   "links": [("Paper: LLMs Get Lost in Multi-turn Conversation", "https://lnkd.in/gwRF2q8P")]},
]
MARQUEE = [("thefork.png", "TheFork"), ("acolad.png", "Acolad"), ("qlip-ai.png", "qlip.ai"), ("stanford.png", "Stanford University"),
           ("ens.png", "ENS Paris"), ("malt.png", "Malt"), ("sup-de-vinci.png", "Sup de Vinci"), ("openclassrooms.png", "OpenClassrooms"),
           ("botiqueai.png", "BotiqueAI"), ("universit-de-paris.png", "Université Paris Diderot")]

MONTHS = {"en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
          "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]}

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
  "stats": [("9 years", "AI research &amp; industry"), ("Co-Founder", "BotiqueAI, Paris"), ("PhD", "AI, ENS Paris")],
  "tabs": {"experience": "Experience", "speaking": "Selected Speaking", "teaching": "Selected Teaching", "publications": "Selected Publications", "about": "About"},
  "h": {"now": "Now", "prev": "Previously", "edu": "Education", "podcast": "Podcast", "talks": "Selected Talks &amp; Events",
        "teaching": "Selected Courses &amp; Mentoring", "pubs": "Selected Publications", "beyond": "Beyond Work"},
  "now": [
    {"logo": "botiqueai.png", "role": "Co-Founder", "org": "BotiqueAI, Paris", "date": "2025 – Present", "shot": "botiqueai-site.jpg", "badge": "CII-certified",
     "body": ["An AI consulting studio helping companies navigate AI adoption, from strategic advisory and integration roadmaps to end-to-end delivery of production AI systems (agents, RAG, chatbots). Clients span <strong>20+ companies across 10+ sectors</strong>, including retail, hospitality, legal and education.",
              "Key project: <strong>Aria</strong>, an AI chatbot platform for Shopify and WordPress merchants, with 24/7 customer support, real-time product search and lead capture."],
     "chips": ["Agentic AI", "RAG", "AI Strategy", "Chatbots"],
     "links": [("Watch the Aria demo →", "https://www.youtube.com/watch?v=iWUjmfBZiLE"), ("botiqueai.com", "https://www.botiqueai.com/"),
               ("LinkedIn", "https://www.linkedin.com/company/botique-ai"), ("Instagram", "https://www.instagram.com/botiqueai/")]},
  ],
  "prev": [
    ("thefork.png", "Lead AI Engineer · TheFork, a Tripadvisor company", "2025 – 2026",
     "Owned the product vision of <strong>AskTheFork</strong>, an AI-powered restaurant discovery experience that replaces traditional filters with natural-language search over menus, photos and reviews (RAG), shipped with a <strong>5% higher conversion rate</strong>. Led the architecture (LangGraph, GPT-4o, OpenSearch), built an LLM restaurant classifier across 300 tags and evaluation pipelines (Arize), and defined the team's AI roadmap with the Head of AI and Product. <a href=\"https://www.media.thiga.co/en/ai-strategy-why-thefork-ditched-the-chatbot\" target=\"_blank\" rel=\"noopener\">Read the case study →</a>"),
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
     "Designed and taught a 35-hour NLP and Generative AI course for Master 2 Data Science students: transformers, LLMs, embeddings, prompt engineering, RAG and conversational AI, with hands-on case studies such as Amazon review analysis and a RAG-based Q&amp;A system."),
    ("thefork.png", "AI Upskilling &amp; Mentoring", "TheFork · 2025",
     "Shared AI expertise with an existing tech team and upskilled engineers on LLMs and agentic AI."),
    ("openclassrooms.png", "Data Science Mentor", "OpenClassrooms · 2022 – 2024",
     "Mentored professionals through Data Science and Machine Learning certification projects and career transitions into AI/ML."),
    ("ens.png", "Teaching Assistant", "CogMaster, ENS Paris · 2019 – 2020",
     "Language Processing &amp; Acquisition, Advanced Master."),
    ("ens.png", "Workshop Organizer &amp; Research Supervisor", "ENS Paris · 2017 – 2020",
     "Organized workshops on open-source and programming best practices, and supervised 7 research interns."),
  ],
  "scholar": "Full list on Google Scholar →",
  "beyond": ["Trained in theater and critical thinking for science communication. Communicating AI well matters as much as building it.",
             "Classically trained musician, with degrees in Piano Performance and in Harmony, Theory &amp; Composition.",
             "Traveled to 50+ countries, and counting."],
  "cta_title": "Chat with me", "marquee": "Where I've worked, taught &amp; spoken",
  "nav_posts": "Posts", "posts_intro": "Notes on AI in production, evaluation and adoption, also shared on LinkedIn.",
  "posts_follow": "Follow me on LinkedIn →", "posts_paper": "Read", "home": "Home",
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
  "stats": [("9 ans", "recherche en IA &amp; industrie"), ("Cofondatrice", "BotiqueAI, Paris"), ("Doctorat", "IA, ENS Paris")],
  "tabs": {"experience": "Expérience", "speaking": "Interventions choisies", "teaching": "Enseignements choisis", "publications": "Publications choisies", "about": "À propos"},
  "h": {"now": "Aujourd'hui", "prev": "Auparavant", "edu": "Formation", "podcast": "Podcast", "talks": "Conférences &amp; événements choisis",
        "teaching": "Cours &amp; mentorat choisis", "pubs": "Publications choisies", "beyond": "En dehors du travail"},
  "now": [
    {"logo": "botiqueai.png", "role": "Cofondatrice", "org": "BotiqueAI, Paris", "date": "2025 – aujourd'hui", "shot": "botiqueai-site.jpg", "badge": "Agréée CII",
     "body": ["Studio de conseil en IA qui accompagne les entreprises dans l'adoption de l'IA, du conseil stratégique et des feuilles de route d'intégration jusqu'à la livraison de systèmes d'IA en production (agents, RAG, chatbots). Plus de <strong>20 entreprises clientes dans plus de 10 secteurs</strong>, dont le commerce, l'hôtellerie, le juridique et l'éducation.",
              "Projet phare : <strong>Aria</strong>, une plateforme de chatbot IA pour les marchands Shopify et WordPress, avec support client 24h/24, recherche de produits en temps réel et capture de leads."],
     "chips": ["IA agentique", "RAG", "Stratégie IA", "Chatbots"],
     "links": [("Voir la démo d'Aria →", "https://www.youtube.com/watch?v=iWUjmfBZiLE"), ("botiqueai.com", "https://www.botiqueai.com/"),
               ("LinkedIn", "https://www.linkedin.com/company/botique-ai"), ("Instagram", "https://www.instagram.com/botiqueai/")]},
  ],
  "prev": [
    ("thefork.png", "Lead AI Engineer · TheFork, une entreprise Tripadvisor", "2025 – 2026",
     "Responsable de la vision produit d'<strong>AskTheFork</strong>, une expérience de découverte de restaurants propulsée par l'IA qui remplace les filtres traditionnels par une recherche en langage naturel sur les menus, photos et avis (RAG), lancée avec un <strong>taux de conversion supérieur de 5 %</strong>. Pilotage de l'architecture (LangGraph, GPT-4o, OpenSearch), classifieur de restaurants par LLM sur 300 tags, pipelines d'évaluation (Arize) et feuille de route IA de l'équipe avec le Head of AI et le Produit. <a href=\"https://www.media.thiga.co/en/ai-strategy-why-thefork-ditched-the-chatbot\" target=\"_blank\" rel=\"noopener\">Lire l'étude de cas →</a>"),
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
     "Conception et enseignement d'un cours de 35 heures sur le TAL et l'IA générative pour des étudiants de Master 2 Data Science : transformers, LLM, embeddings, prompt engineering, RAG et IA conversationnelle, avec des cas pratiques comme l'analyse d'avis Amazon et un système de questions-réponses basé sur RAG."),
    ("thefork.png", "Montée en compétences IA &amp; mentorat", "TheFork · 2025",
     "Partage d'expertise IA avec l'équipe tech et montée en compétences des ingénieurs sur les LLM et l'IA agentique."),
    ("openclassrooms.png", "Mentore Data Science", "OpenClassrooms · 2022 – 2024",
     "Accompagnement de professionnels dans leurs projets de certification en Data Science et Machine Learning et dans leur reconversion vers l'IA."),
    ("ens.png", "Chargée de TD", "CogMaster, ENS Paris · 2019 – 2020",
     "Traitement et acquisition du langage, master avancé."),
    ("ens.png", "Organisatrice d'ateliers &amp; encadrante de recherche", "ENS Paris · 2017 – 2020",
     "Organisation d'ateliers sur l'open source et les bonnes pratiques de programmation, et encadrement de 7 stagiaires de recherche."),
  ],
  "scholar": "Liste complète sur Google Scholar →",
  "beyond": ["Formée au théâtre et à l'esprit critique pour la médiation scientifique. Bien expliquer l'IA compte autant que la construire.",
             "Musicienne de formation classique, diplômée en interprétation au piano ainsi qu'en harmonie, théorie et composition.",
             "Plus de 50 pays visités, et ce n'est pas fini."],
  "cta_title": "Discutons", "marquee": "Là où j'ai travaillé, enseigné et pris la parole",
  "nav_posts": "Posts", "posts_intro": "Notes sur l'IA en production, l'évaluation et l'adoption, également publiées sur LinkedIn (en anglais).",
  "posts_follow": "Me suivre sur LinkedIn →", "posts_paper": "Lire", "home": "Accueil",
  "cta_chips": ["Stratégie &amp; conseil IA", "Systèmes d'IA sur mesure", "Conférences &amp; ateliers", "Formation &amp; acculturation IA"],
  "cta_body": "J'aide les entreprises à définir leur stratégie IA et à construire des systèmes qui apportent une vraie valeur. Que vous ayez besoin d'ingénierie, de conseil auprès de la direction ou d'une intervention qui va au-delà des effets d'annonce, parlons-en.",
  "footer": "Georgia Loukatou · Paris, France",
  "photo_alt": "Portrait de Georgia Loukatou",
},
}

EXT = 'target="_blank" rel="noopener"'


def chips(items, cls="chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{c}</li>" for c in items) + "</ul>"


MAIL_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'


def lang_path(lang, page):
    """URL of `page` ('' for home, 'posts/' for posts) in `lang`."""
    return LANGS[lang] + page


def rel_fix(html, lang, page):
    """Make asset paths and internal links relative, so pages also work when opened from disk."""
    here = (LANGS[lang] + page).strip("/")
    base = "../" * (here.count("/") + 1 if here else 0)
    html = html.replace('src="/assets/', f'src="{base}assets/').replace('href="/assets/', f'href="{base}assets/')
    html = html.replace('href="/style.css"', f'href="{base}style.css"')
    for l in LANGS:
        for pg in ("posts/", ""):
            target = (LANGS[l] + pg).strip("/")
            html = html.replace(f'href="/{target + "/" if target else ""}"', f'href="{base}{target + "/index.html" if target else "index.html"}"')
    return html


def shell(lang, page, title, desc, main, script=""):
    return rel_fix(_shell(lang, page, title, desc, main, script), lang, page)


def _shell(lang, page, title, desc, main, script=""):
    c = CONTENT[lang]
    alt_links = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{lang_path(l, page)}">' for l in LANGS)
    switch = "".join(
        f'<a href="{lang_path(l, page)}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else "") + f">{LANG_LABEL[l]}</a>"
        for l in LANGS)
    posts_cur = ' aria-current="page"' if page == "posts/" else ""
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{lang_path(lang, page)}">
{alt_links}
<link rel="alternate" hreflang="x-default" href="{SITE}/{page}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{lang_path(lang, page)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
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
  <div class="progress" aria-hidden="true"></div>
  <div class="wrap nav-inner">
    <a class="monogram" href="{LANGS[lang]}" aria-label="{c["name"]}, {c["home"]}">GL</a>
    <a class="nav-link" href="{lang_path(lang, "posts/")}"{posts_cur}>{c["nav_posts"]}</a>
    <div class="lang-switch" aria-label="Language">{switch}</div>
    <a class="btn btn-small" href="{CALENDLY}" {EXT}>{c["book"]}</a>
  </div>
</nav>

{main}

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
document.getElementById('year').textContent = new Date().getFullYear();
{COMMON_SCRIPT}
{script}
</script>
</body>
</html>
'''


COMMON_SCRIPT = """(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // scroll progress bar
  var bar = document.querySelector('.progress');
  function prog() { var h = document.documentElement; var m = h.scrollHeight - h.clientHeight; bar.style.transform = 'scaleX(' + (m > 0 ? h.scrollTop / m : 0) + ')'; }
  if (bar) { window.addEventListener('scroll', prog, {passive: true}); prog(); }
  if (reduce || !('IntersectionObserver' in window)) return;
  // reveal on scroll, staggered within each group
  var sel = '.block-title, .cards > *, .timeline li, .edu li, .feature, .talks > *, .pubs li, .beyond p, .post, .cta, .posts-head .wrap > *';
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {rootMargin: '0px 0px -8% 0px'});
  function arm(root) {
    root.querySelectorAll(sel).forEach(function (el) {
      if (el.classList.contains('reveal')) return;
      var i = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.classList.add('reveal'); el.style.transitionDelay = Math.min(i, 5) * 70 + 'ms';
      io.observe(el);
    });
  }
  arm(document);
  window.armReveal = arm;
  // count-up for numbers in the stats row
  document.querySelectorAll('.stats dt').forEach(function (dt) {
    var m = dt.textContent.match(/^(\\d+)(.*)$/); if (!m) return;
    var end = +m[1], rest = m[2], t0 = null;
    var o = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; o.disconnect();
      function step(t) { if (!t0) t0 = t; var k = Math.min((t - t0) / 1100, 1); dt.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))) + rest; if (k < 1) requestAnimationFrame(step); }
      dt.textContent = '0' + rest; requestAnimationFrame(step);
      setTimeout(function () { dt.textContent = end + rest; }, 1500);
    });
    o.observe(dt);
  });
})();"""

TAB_SCRIPT = '''(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  var ids = tabs.map(function (t) { return t.dataset.tab; });
  function show(id, focus) {
    if (ids.indexOf(id) < 0) id = ids[0];
    tabs.forEach(function (t) {
      var on = t.dataset.tab === id;
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      var pnl = document.getElementById('panel-' + t.dataset.tab); pnl.hidden = !on;
      if (on && focus) t.focus();
    });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () {
      show(t.dataset.tab);
      history.replaceState(null, '', '#' + t.dataset.tab);
      var bar = document.querySelector('.tabbar-wrap');
      if (bar.getBoundingClientRect().top < 0) bar.scrollIntoView({behavior: 'smooth'});
    });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (d) { var n = tabs[(i + d + tabs.length) % tabs.length]; show(n.dataset.tab, true); history.replaceState(null, '', '#' + n.dataset.tab); }
    });
  });
  show(location.hash.slice(1));
  window.addEventListener('hashchange', function () { show(location.hash.slice(1)); });
  document.querySelectorAll('.lang-switch a').forEach(function (a) {
    a.addEventListener('click', function () { if (location.hash) a.href = a.getAttribute('href') + location.hash; });
  });
})();'''


def block(num, title, inner):
    return f'''
    <section class="block">
      <div class="wrap">
        <h2 class="block-title"><span class="num">{num:02d}</span>{title}</h2>
        {inner}
      </div>
    </section>'''


def render_home(lang):
    c = CONTENT[lang]
    h = c["h"]
    tabs = "".join(f'<button role="tab" id="tab-{k}" aria-controls="panel-{k}" data-tab="{k}">{v}</button>' for k, v in c["tabs"].items())

    now_cards = ""
    for r in c["now"]:
        body = "".join(f"<p>{p}</p>" for p in r["body"])
        links = "".join(f'<a href="{u}" {EXT}>{t}</a>' for t, u in r["links"])
        shot = (f'<a class="card-shot" href="https://www.botiqueai.com/" {EXT}><img src="/assets/{r["shot"]}" alt="botiqueai.com" width="1200" height="667" loading="lazy"></a>'
                if r.get("shot") else "")
        badge = f'<span class="badge-inline">{r["badge"]}</span>' if r.get("badge") else ""
        now_cards += f'''
        <article class="card">
          {shot}
          <header class="card-head">
            <img src="/assets/{r["logo"]}" alt="" width="44" height="44">
            <div><h4>{r["role"]}</h4><p class="org">{r["org"]}</p></div>
            <span class="date">{r["date"]}</span>
          </header>
          {badge}
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
    marquee = "".join(f'<span class="logo"><img src="/assets/{f}" alt="" width="28" height="28">{n}</span>' for f, n in MARQUEE)

    podcast = f'''<article class="feature">
          <a class="feature-media" href="{SPOTIFY}" {EXT}><img src="/assets/podcast.jpg" alt="{pc["alt"]}" width="1600" height="892" loading="lazy"></a>
          <div class="feature-body">
            <p class="kicker"><span class="new">{pc["kicker"]}</span></p>
            <h3>How Small Businesses Can Adopt AI Without Losing the Human Touch</h3>
            <p class="show">{pc["show"]}</p>
            <p>{pc["body"]}</p>
            <a class="btn" href="{SPOTIFY}" {EXT}>{pc["btn"]}</a>
          </div>
        </article>'''
    talks = f'''<div class="talks">
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
        </div>'''

    main = f'''<header class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <p class="eyebrow">{c["eyebrow"]}</p>
      <h1>{c["name"]}</h1>
      <p class="lead">{c["lead"]}</p>
      <ul class="hero-points">{points}</ul>
      <div class="cta-row">
        <a class="btn" href="{CALENDLY}" {EXT}>{c["book"]}</a>
        <a class="btn btn-ghost" href="{LINKEDIN}" {EXT}>LinkedIn</a>
      </div>
      <p class="contact-line"><a href="mailto:{EMAIL}">{MAIL_ICON}{EMAIL}</a></p>
    </div>
    <div class="hero-photo"><img src="/assets/georgia.jpg" alt="{c["photo_alt"]}" width="300" height="300"></div>
  </div>
  <div class="wrap"><dl class="stats">{stats}</dl></div>
  <div class="marquee" aria-label="{c["marquee"]}">
    <p class="marquee-label wrap">{c["marquee"]}</p>
    <div class="marquee-track"><div class="group">{marquee}</div><div class="group" aria-hidden="true">{marquee}</div></div>
  </div>
</header>

<main id="main" class="tabs-area">
  <div class="tabbar-wrap">
    <div class="wrap"><div class="tabbar" role="tablist">{tabs}</div></div>
  </div>
  <div class="panel" role="tabpanel" id="panel-experience" aria-labelledby="tab-experience">
    {block(1, h["now"], f'<div class="cards one">{now_cards}</div>')}
    {block(2, h["prev"], f'<ol class="timeline">{timeline}</ol>')}
    {block(3, h["edu"], f'<ul class="edu">{edu}</ul>')}
  </div>
  <div class="panel" role="tabpanel" id="panel-speaking" aria-labelledby="tab-speaking">
    {block(1, h["podcast"], podcast)}
    {block(2, h["talks"], talks)}
  </div>
  <div class="panel" role="tabpanel" id="panel-teaching" aria-labelledby="tab-teaching">
    {block(1, h["teaching"], f'<div class="cards three">{teach}</div>')}
  </div>
  <div class="panel" role="tabpanel" id="panel-publications" aria-labelledby="tab-publications">
    {block(1, h["pubs"], f'<ol class="pubs">{pubs}</ol><p class="links"><a href="{SCHOLAR}" {EXT}>{c["scholar"]}</a></p>')}
  </div>
  <div class="panel" role="tabpanel" id="panel-about" aria-labelledby="tab-about">
    {block(1, h["beyond"], f'<div class="beyond">{beyond}</div>')}
  </div>
</main>'''
    return shell(lang, "", c["title"], c["desc"], main, TAB_SCRIPT)


def render_blocks(blocks):
    out = ""
    for b in blocks:
        if isinstance(b, str):
            out += f"<p>{b}</p>"
        else:
            tag, items = b
            out += f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"
    return out


def render_posts(lang):
    c = CONTENT[lang]
    items = ""
    for p in POSTS:
        y, mo, d = p["date"]
        date_txt = f"{d} {MONTHS[lang][mo - 1]} {y}"
        links = "".join(f'<a href="{u}" {EXT}>{t} →</a>' for t, u in p["links"])
        items += f'''
      <article class="post">
        <time datetime="{y:04d}-{mo:02d}-{d:02d}">{date_txt}</time>
        <h2>{p["title"]}</h2>
        <div class="post-body">{render_blocks(p["body"])}</div>
        <p class="links">{links}</p>
      </article>'''
    main = f'''<main id="main" class="posts-page">
  <header class="posts-head">
    <div class="wrap">
      <h1>{c["nav_posts"]}</h1>
      <p class="lead">{c["posts_intro"]}</p>
      <p class="links"><a href="{LINKEDIN}recent-activity/all/" {EXT}>{c["posts_follow"]}</a></p>
    </div>
  </header>
  <div class="wrap posts-list">{items}
  </div>
</main>'''
    title = f'{c["nav_posts"]} · {c["name"]}'
    return shell(lang, "posts/", title, c["posts_intro"], main)


if __name__ == "__main__":
    for lang in LANGS:
        for page, fn in (("", render_home), ("posts/", render_posts)):
            out = ROOT / (LANGS[lang] + page).strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(lang), encoding="utf-8")
            print("wrote", out.relative_to(ROOT))
