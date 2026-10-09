Title: Projets personnels
Slug: projets-personnels
Date: 2026-10-09
Kicker: Réalisations · Projets personnels
Lead: Les projets que je mène en dehors des cours pour progresser.

## Ce portfolio (Pelican + GitHub Pages)

<p>
<a href="https://github.com/anisloucif/Pelican-Portfolio" target="_blank" rel="noopener" class="btn btn-outline-dark btn-sm"><i class="bi bi-github"></i> Code source</a>
<a href="https://anisloucif.github.io/Pelican-Portfolio/" class="btn btn-outline-primary btn-sm"><i class="bi bi-globe"></i> Site en ligne</a>
</p>

### Contexte

Le site que vous consultez est un **site statique** généré avec **Pelican**, un générateur écrit en Python, à partir d'un modèle fourni en cours. Je l'ai personnalisé (contenu, menu, thème) et je le publie moi-même sur **GitHub Pages**.

### Fonctionnement

<span class="skill">Python</span><span class="skill">Pelican</span><span class="skill">Markdown</span><span class="skill">Jinja2</span><span class="skill">Bootstrap 5</span><span class="skill">Git</span><span class="skill">GitHub Pages</span>

```text
Mon-portfolio/
├── content/          # contenu en Markdown
│   ├── pages/        # pages fixes (présentation, stage, projets…)
│   ├── veille/       # articles de veille (publiés aussi en flux RSS)
│   ├── images/
│   └── downloads/    # CV en PDF
├── themes/sio_portfolio/   # thème : gabarits Jinja2 + CSS
├── pelicanconf.py    # configuration (menu, URL, flux RSS)
└── docs/             # site HTML généré, publié par GitHub Pages
```

Chaque page commence par des **métadonnées** que Pelican lit avant de générer le HTML :

```text
Title: Projets personnels
Slug: projets-personnels
Date: 2026-10-09
```

Extrait de la configuration (`pelicanconf.py`) : dossier de sortie et **flux RSS de la veille** :

```python
OUTPUT_PATH = 'docs'                     # GitHub Pages publie le dossier /docs
ARTICLE_PATHS = ['veille']
PAGE_SAVE_AS = 'pages/{slug}.html'

FEED_ALL_RSS = 'feeds/veille.rss.xml'    # flux RSS des articles de veille
FEED_ALL_ATOM = 'feeds/veille.atom.xml'
```

### Procédure de travail et de publication

```bash
# 1. Activer l'environnement Python
cd ~/Mon-portfolio
source venv/bin/activate

# 2. Prévisualiser en local avec rechargement automatique
pelican -lr                 # http://localhost:8000

# 3. Publier
git add .
git commit -m "docs: mise à jour du rapport de stage"
git push origin master      # GitHub Pages republie le dossier docs/
```

### Difficultés rencontrées

- **Proxy du lycée** : sous Ubuntu au lycée, l'installation des paquets nécessite l'option `pip install --proxy`. À la maison, sur macOS, la connexion est directe.
- **Environnement virtuel** : le dossier `venv/` dépend du système (Linux au lycée, macOS chez moi). Il ne doit pas être versionné : je l'ai ajouté au `.gitignore` et je le recrée sur chaque machine.
- **Liens morts** : les liens du menu doivent correspondre exactement au `slug` de chaque page. J'ai fixé le `Slug` dans les métadonnées de chaque fichier.
