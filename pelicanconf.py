#####################################################################
#                                                                   #
#                     FICHIER DE CONFIGURATION                      #
#                          DU PORTFOLIO                             #
#                                                                   #
#####################################################################

# IMPORTS :
# ---------
from datetime import datetime



# CONFIGURATION & INFORMATIONS GENERALES :
# ----------------------------------------
# Cette section contient les variables générales associé au site/portefolio.

SITENAME = 'Portfolio BTS SIO SLAM'
SITESUBTITLE = "Anis LOUCIF — Développeur d'applications en formation"
AUTHOR = 'Anis LOUCIF'
SITEURL = "https://anisloucif.github.io/Pelican-Portfolio" # URL publique (utilisée par le flux RSS ; les liens des pages restent relatifs)
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
CURRENT_YEAR = datetime.now().year
RELATIVE_URLS = True # Est surchargé par la valeur False dans le fichier publishconf.py


# CONFIGURATION DES DOSSIERS :
# ----------------------------
# Cette section définit la structure des dossiers

PATH = "content"                # Dossier des contenus (pages et articles)
THEME = 'themes/sio_portfolio'  # Dossier du thème
ARTICLE_PATHS = ['veille']      # Sous-dossier de PATH qui contient les articles de veille.
PAGE_PATHS = ['pages']          # Sous-dossier de PATH qui contient les pages statiques du site. 


# Pour les fichiers statiques :
STATIC_PATHS = ['images', 'downloads']

# Dossier de sortie pour la publication :
OUTPUT_PATH = 'docs'           # Attention, pour la publication sur GitHub Pages le dossier doit être "/docs"



# URL & FICHIERS GENERES :
# ------------------------
# Cette section définit les constante utilisée par Pelican pour générer les url et nom des fichiers
# articles (veille) et pages.

ARTICLE_URL = 'veille/{slug}.html'
ARTICLE_SAVE_AS = 'veille/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'



# STRUCTURE DU MENU DE NAVIGATION:
# --------------------------------

# ((nom, url, icone, (nom, url, icone),description, couleur)...)
MENUITEMS = (
    ("Accueil", "/index", "house", None, "Page d'accueil du portfolio", None),

    ("Présentation", "/pages/parcours", "person-vcard",
        (
            ("Présentation & CV", "/pages/parcours"),
            ("Parcours scolaire", "/pages/parcours-scolaire"),
            ("Le BTS SIO", "/pages/bts-sio")
        ),
        "Qui je suis, mon CV, mon parcours scolaire et professionnel.", "primary"
    ),

    ("Réalisations", "/pages/realisations", "kanban",
        (
            ("Stage de 1re année (ButeurIA)", "/pages/stage-sio1"),
            ("Stage de 2e année", "/pages/stage-sio2"),
            ("Projets scolaires (AP)", "/pages/projets-scolaires"),
            ("Projets personnels", "/pages/projets-personnels"),
            ("Certifications", "/pages/certifications-complementaires")
        ),
        "Mon stage, mes ateliers professionnels, mes projets et mes certifications.", "success"
     ),

    ("Veille techno.", "/ma-veille", "broadcast-pin",
        (
            ("Sujet, méthode & outils", "/ma-veille"),
            ("Archive des articles", "/archives"),
            ("Mots-clés", "/tags"),
            ("Flux RSS", "/feeds/veille.rss.xml")
        ),
        "Ma veille sur les agents IA et leurs protocoles (MCP, A2A), avec flux RSS.", "warning"
    ),

    ("Contact", "/pages/contact", "envelope", None, "Me contacter", None),
)

MAINITEMS = MENUITEMS[1:4] # Récupération de PARCOURS, REALISATION & VEILLE pour afficage dans index.html



# PLUGINS :
# ---------
PLUGIN_PATHS = ['plugins']
PLUGINS = []



# ARTICLES & PAGINATION :
# -----------------------
# Options associée à la génération et pagination des articles (veille).

# Résumé des articles
SUMMARY_MAX_LENGTH = 60

# Pagination
DEFAULT_PAGINATION = 10



# Flux RSS/Atom (veille technologique) :
# ---------------------------------------
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/veille.rss.xml'
FEED_ALL_ATOM = 'feeds/veille.atom.xml'
FEED_MAX_ITEMS = 20
RSS_FEED_SUMMARY_ONLY = True
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None

# Fichiers non publiés
IGNORE_FILES = ['.#*', '*.md~', 'monCV.md']
