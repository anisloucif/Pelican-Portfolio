Title: Stage de 1re année : découverte de la qualité logicielle sur ButeurIA
Slug: stage-sio1
Date: 2026-10-09
Kicker: Réalisations · Stage SIO1
Lead: Six semaines de stage à distance, du 18 mai au 26 juin 2026 : découverte de la démarche de tests (QA) sur une application SaaS web et mobile, puis observation d'un projet d'orchestration d'agents IA.

<div markdown="1" class="row g-4 mb-2">
<div markdown="1" class="col-md-6">
<dl class="id-card mb-0">
<dt>Dates</dt><dd>Du 18 mai au 26 juin 2026 (6 semaines)</dd>
<dt>Modalité</dt><dd>Stage à distance (télétravail)</dd>
<dt>Structure d'accueil</dt><dd>Éditeur de l'application <strong>ButeurIA</strong> (SaaS)</dd>
</dl>
</div>
<div markdown="1" class="col-md-6">
<dl class="id-card mb-0">
<dt>Tuteur en entreprise</dt><dd>Thomas, développeur web</dd>
<dt>Professeur référent</dt><dd>M. Dutilloy</dd>
<dt>Nature du stage</dt><dd>Stage d'observation et de découverte : qualité logicielle, outils de versioning, projet SaaS d'agents IA</dd>
</dl>
</div>
</div>

<div markdown="1" class="toc-box">
**Sommaire**

1. [Présentation de l'entreprise et du produit](#entreprise)
2. [Déroulement du stage](#deroulement)
3. [La démarche qualité (QA) que j'ai découverte](#qa)
4. [Ce que j'ai pratiqué : Git, GitHub et SSH](#git)
5. [Observation d'un projet d'orchestration d'agents IA](#agents)
6. [Compétences du référentiel abordées](#competences)
7. [Bilan honnête du stage](#bilan)
</div>

<h2 id="entreprise">1. Présentation de l'entreprise et du produit</h2>

La structure qui m'a accueilli développe et exploite **ButeurIA**, un **SaaS de prédictions sportives propulsé par l'intelligence artificielle**. L'application propose des prédictions de buteurs pour les matchs de football, avec une offre gratuite et un abonnement **Premium** (paiement via **Stripe**).

ButeurIA est disponible sur **trois plateformes** : le **web** (navigateur) et les applications mobiles **Android** et **iOS**.

L'équipe prépare aussi un **second produit SaaS**, encore en pré-lancement : une **plateforme d'orchestration d'agents IA** pour les TPE et PME, qui connecte plusieurs intelligences artificielles aux outils du quotidien (voir [partie 5](#agents)).

<h2 id="deroulement">2. Déroulement du stage</h2>

Le stage s'est déroulé **entièrement à distance**, en deux temps :

| Période | Contenu |
|---|---|
| 18 mai - 5 juin | Découverte de l'application ButeurIA et de la **démarche de tests (QA)** utilisée par l'équipe |
| 6 - 26 juin | **Observation** d'un nouveau projet SaaS d'orchestration d'agents IA, et veille technologique sur le sujet |

Le code de ButeurIA est complexe et l'application est en production : une erreur de manipulation aurait pu affecter de vrais utilisateurs. Je n'ai donc **pas développé** sur l'application. Mon tuteur m'a montré son fonctionnement et la façon dont l'équipe suit sa qualité.

<h2 id="qa">3. La démarche qualité (QA) que j'ai découverte</h2>

### 3.1 Le document de suivi QA de l'équipe

L'équipe suit la qualité de ButeurIA dans un **tableau de suivi**, qui m'a été fourni par mon tuteur. Je l'ai étudié pour comprendre comment on organise des tests. Il comporte quatre onglets :

| Onglet | Rôle |
|---|---|
| Bugs & QA | Une ligne par anomalie : titre, type, gravité, plateforme, écran, étapes pour reproduire, résultat attendu, résultat obtenu, statut |
| Idées & Améliorations | Propositions d'évolution avec leur impact et leur difficulté estimés |
| Journal de bord | Suivi quotidien : ce qui a été fait, appris, ce qui a bloqué et comment |
| Synthèse | Indicateurs calculés automatiquement par formules (`NB.SI`) : nombre d'anomalies par gravité, par statut… |

À la fin de la période étudiée, le tableau recensait **48 retours** (32 bugs, 11 améliorations d'ergonomie, 4 problèmes de performance, 1 faute d'orthographe), dont **6 bloquants**.

### 3.2 Comment on classe une anomalie

| Gravité | Définition | Exemple tiré du tableau |
|---|---|---|
| <span class="sev-b">Bloquant</span> | Empêche un parcours essentiel ou fait perdre de l'argent | Le bouton « Souscrire Premium » renvoie une page 404 |
| <span class="sev-m">Majeur</span> | Le parcours fonctionne mal ou induit en erreur | Aucun message si l'email est déjà utilisé |
| Mineur | Gêne sans bloquer | Pas d'indicateur de chargement |
| Cosmétique | Défaut visuel | Avatar carré au lieu de rond sur Firefox |

Ce que j'en ai retenu : **un bug sur le paiement passe avant un défaut d'affichage**. On priorise selon l'impact sur l'utilisateur et sur l'entreprise.

### 3.3 Comment on rédige un rapport d'anomalie

Exemple de fiche, tirée du tableau :

```text
Titre         : Nom de joueur 'Vinícius Júnior' affiché avec ??? au lieu des accents
Type          : Bug              Gravité : Majeur
Plateforme    : Web Chrome       Écran    : Page Prédictions
Étapes        : 1. Filtrer par Real Madrid
                2. Regarder la carte de Vinícius
Attendu       : Accents corrects (Vinícius Júnior)
Obtenu        : Encodage cassé : 'Vin?cius J?nior'
Statut        : Nouveau -> En cours de correction -> Corrigé
```

Les règles d'une bonne fiche : **un seul problème par fiche**, des étapes **reproductibles par quelqu'un d'autre**, l'**environnement exact** (navigateur, système) et une preuve (capture ou vidéo).

Cet exemple m'a aussi fait découvrir la notion d'**encodage des caractères** : les accents s'affichent mal quand les données ne sont pas transmises en **UTF-8**. Cela se vérifie dans l'en-tête de la réponse du serveur :

```http
Content-Type: application/json; charset=utf-8
```

### 3.4 Les outils présentés

| Outil | À quoi il sert |
|---|---|
| Chrome / Firefox DevTools | Voir les erreurs JavaScript (onglet *Console*) et les codes HTTP comme 404 ou 500 (onglet *Network*) |
| Lighthouse (intégré à Chrome) | Mesurer la performance et l'accessibilité d'une page |
| Tableur | Centraliser les anomalies et calculer des indicateurs |

<h2 id="git">4. Ce que j'ai pratiqué : Git, GitHub et SSH</h2>

Mon tuteur a cité Git et GitHub comme mon principal apprentissage du stage. Voici la configuration de base à mettre en place pour travailler avec GitHub en SSH :

```bash
# Identité Git
git config --global user.name "Anis LOUCIF"
git config --global user.email "anis.loucif91@gmail.com"

# Création d'une clé SSH et ajout à l'agent
ssh-keygen -t ed25519 -C "anis.loucif91@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Afficher la clé publique pour l'ajouter dans GitHub > Settings > SSH and GPG keys
cat ~/.ssh/id_ed25519.pub

# Tester la connexion
ssh -T git@github.com
```

Travailler avec des branches :

```bash
git switch -c docs/rapport-stage     # créer une branche dédiée
git add .
git commit -m "docs: ajout du rapport de stage SIO1"
git push -u origin docs/rapport-stage
git switch main && git merge docs/rapport-stage   # fusion une fois validé
```

Un axe de progrès relevé par mon tuteur était **la rigueur des messages de commit**. J'utilise depuis une convention simple : `type: description courte` (`fix`, `feat`, `docs`, `style`).

<h2 id="agents">5. Observation d'un projet d'orchestration d'agents IA</h2>

Pendant la seconde partie du stage, j'ai suivi en **observation** un nouveau projet de l'équipe : une plateforme qui permet aux **TPE et PME** de connecter plusieurs intelligences artificielles (des « agents ») à leurs outils du quotidien.

Le projet étant **sensible et en pré-lancement**, je n'ai pas participé au développement. Cette observation m'a fait comprendre :

- qu'un produit IA en entreprise pose des questions de **fiabilité des réponses**, de **sécurité des données** et de **coût d'utilisation** des modèles ;
- que les agents ont besoin de **connecteurs standards** pour accéder aux outils.

C'est ce qui m'a donné le sujet de [ma veille technologique]({filename}/pages/ma-veille.md) : les protocoles MCP et A2A.

<h2 id="competences">6. Compétences du référentiel abordées</h2>

| Bloc | Compétence | Comment je l'ai abordée |
|---|---|---|
| Bloc 2 SLAM | Assurer la maintenance corrective ou évolutive d'une solution applicative | Découverte du suivi des anomalies : classement, priorisation, statuts de correction |
| Bloc 2 SLAM | Évaluer la qualité d'une solution applicative | Découverte des critères de gravité et d'outils comme Lighthouse et les DevTools |
| Bloc 1 | Travailler en mode projet | Observation de l'organisation d'une équipe produit et d'un projet en phase de conception |
| Bloc 1 | Organiser son développement professionnel | Apprentissage de Git, GitHub et SSH ; veille technologique sur les agents IA |

<h2 id="bilan">7. Bilan honnête du stage</h2>

### Appréciation du tuteur

<blockquote markdown="1">
« Il a montré de réelles capacités d'apprentissage, notamment sur les outils de versioning (Git, GitHub, clés SSH, gestion de branches). »
</blockquote>

### Ce que j'en retiens

- J'ai découvert **l'envers du décor d'une application en production** : une application n'est pas seulement du code, il faut aussi la tester, suivre les anomalies et les prioriser.
- J'ai appris les **bases de Git, GitHub et SSH**, que j'utilise aujourd'hui pour mes projets et pour ce portfolio.
- J'ai trouvé mon **sujet de veille** : les agents IA en entreprise.

### Ce qui m'a manqué

Ce stage a été surtout un **stage d'observation**. À distance, et sur une application trop sensible pour un stagiaire de première année, j'ai peu pratiqué par moi-même. Je retiens deux axes de progrès, identifiés avec mon tuteur :

- chercher d'abord dans la **documentation officielle** avant de demander de l'aide ;
- être plus rigoureux dans les **messages de commit** et la **documentation**.

C'est pour cette raison que je cherche, pour mon **stage de 2<sup>e</sup> année** (janvier-février 2027), une mission où je **développe réellement**, dans une équipe où je peux coder et être relu.
