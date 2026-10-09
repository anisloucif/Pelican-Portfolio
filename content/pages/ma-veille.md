Title: Les agents IA et leurs protocoles (MCP, A2A)
Slug: ma-veille
Date: 2026-10-09
Template: veille
Save_as: ma-veille.html
URL: ma-veille.html

<div markdown="1" class="row g-4">
<div markdown="1" class="col-md-8" >

## Sujet de veille

**Comment les agents IA se connectent-ils aux outils et aux données des entreprises ?**

Un **agent IA** est un programme qui s'appuie sur un modèle de langage (LLM) pour **réaliser des actions** à la place de l'utilisateur : chercher un document, créer un ticket, envoyer un email, interroger une base de données. Pour cela, l'agent doit pouvoir se connecter aux applications existantes. Depuis fin 2024, des **protocoles standards** apparaissent pour encadrer ces connexions, en particulier :

- **MCP** (*Model Context Protocol*) : relie un agent à des outils et à des sources de données ;
- **A2A** (*Agent2Agent*) : permet à des agents de communiquer entre eux.

</div>
<div markdown="1" class="col-md-4">
<div markdown="1" class="info-card">
<h3 class="h6"><i class="bi bi-lightbulb"></i> Pourquoi ce sujet ?</h3>
<p class="small mb-0">Pendant la 2<sup>e</sup> phase de mon <a href="{filename}/pages/Realisations/stage-sio1.md">stage de 1<sup>re</sup> année</a>, j'ai observé la conception d'une <strong>plateforme d'orchestration d'agents IA pour les TPE/PME</strong>. Pour un développeur SLAM, savoir intégrer une application à ces agents (par exemple en exposant une API via MCP) devient une compétence recherchée.</p>
</div>
</div>
</div>

## Méthodologie

1. **Collecter** : je suis des sources fiables (blogs officiels des éditeurs, presse tech) via un agrégateur de flux RSS et des alertes par mots-clés.
2. **Trier** : je ne garde que les annonces qui changent concrètement quelque chose pour un développeur (nouveau standard, nouvel outil, nouvelle obligation).
3. **Vérifier** : je remonte toujours à la **source officielle** (annonce de l'éditeur, documentation) avant de rédiger.
4. **Synthétiser** : pour chaque nouveauté, un article court avec un résumé, ce que ça change pour un développeur et la source.
5. **Diffuser** : les articles sont publiés ici et dans le **flux RSS du portfolio**.

## Outils utilisés

| Outil | Rôle | Configuration |
|---|---|---|
| **Feedly** (agrégateur RSS) | Centraliser les flux des sources | Dossier « Agents IA » : blogs Anthropic, OpenAI, Google Cloud, Linux Foundation, Le Monde Informatique, Usine Digitale, Blog du Modérateur |
| **Google Alerts** | Être averti des nouveaux articles | Alertes : `"Model Context Protocol"`, `"agents IA" entreprise`, `"Agent2Agent"`, `"AI Act" développeurs` |
| **GitHub** | Suivre les projets open source | Dépôts suivis (*Watch*) : spécification MCP, SDK officiels |
| **Ce portfolio (Pelican)** | Publier et diffuser | Articles en Markdown, flux RSS généré automatiquement |

<div markdown="1" class="info-card my-3">
<div markdown="1" class="d-flex flex-wrap align-items-center gap-3">
<i class="bi bi-rss-fill" style="font-size:2rem;color:#e67e22"></i>
<div markdown="1" class="flex-grow-1">
<strong>S'abonner à ma veille par flux RSS</strong><br>
<span class="small text-muted">Copiez cette adresse dans votre lecteur de flux (Feedly, Inoreader, Thunderbird…)</span><br>
<code>https://anisloucif.github.io/Pelican-Portfolio/feeds/veille.rss.xml</code>
</div>
<a href="https://anisloucif.github.io/Pelican-Portfolio/feeds/veille.rss.xml" class="btn btn-outline-primary btn-sm"><i class="bi bi-rss"></i> Flux RSS</a>
<a href="https://anisloucif.github.io/Pelican-Portfolio/feeds/veille.atom.xml" class="btn btn-outline-secondary btn-sm">Atom</a>
</div>
</div>

## Synthèse provisoire

En un an, on est passé de connexions « bricolées » au cas par cas à des **standards ouverts** (MCP, A2A), gérés par des fondations neutres (Linux Foundation) et adoptés par les principaux éditeurs, même concurrents. En parallèle, la **réglementation européenne** (AI Act) fixe des obligations aux entreprises qui conçoivent ou déploient de l'IA. Pour un développeur, cela veut dire : **savoir exposer son application à des agents** (API documentée, serveur MCP) tout en gardant le **contrôle des accès et des données**.
