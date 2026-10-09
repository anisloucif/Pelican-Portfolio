Title: Stage de 1re année : tests et qualité logicielle sur ButeurIA
Slug: stage-sio1
Date: 2026-10-09
Kicker: Réalisations · Stage SIO1
Lead: Six semaines de stage à distance, du 18 mai au 26 juin 2026 : campagnes de tests (QA) sur une application SaaS web et mobile, puis observation d'un projet d'orchestration d'agents IA.

<div markdown="1" class="row g-4 mb-2">
<div markdown="1" class="col-md-6">
<dl class="id-card mb-0">
<dt>Dates</dt><dd>Du 18 mai au 26 juin 2026 (6 semaines)</dd>
<dt>Modalité</dt><dd>Stage à distance (télétravail), point quotidien le matin et débriefing le soir</dd>
<dt>Structure d'accueil</dt><dd>Éditeur de l'application <strong>ButeurIA</strong> (SaaS)</dd>
</dl>
</div>
<div markdown="1" class="col-md-6">
<dl class="id-card mb-0">
<dt>Tuteur en entreprise</dt><dd>Thomas, développeur web</dd>
<dt>Professeur référent</dt><dd>M. Dutilloy</dd>
<dt>Missions</dt><dd>Phase 1 : tests fonctionnels et qualité logicielle<br>Phase 2 : observation et veille sur un projet SaaS d'agents IA</dd>
</dl>
</div>
</div>

<div markdown="1" class="toc-box" >
**Sommaire**

1. [Présentation de l'entreprise et du produit](#entreprise)
2. [Organisation du travail et outils](#organisation)
3. [Phase 1 : campagnes de tests sur ButeurIA](#phase1)
4. [Procédures et tutoriels rédigés](#procedures)
5. [Propositions d'amélioration](#ameliorations)
6. [Phase 2 : observation d'un projet d'orchestration d'agents IA](#phase2)
7. [Compétences du référentiel mobilisées](#competences)
8. [Bilan du stage](#bilan)
</div>

<h2 id="entreprise">1. Présentation de l'entreprise et du produit</h2>

La structure qui m'a accueilli développe et exploite **ButeurIA**, un **SaaS de prédictions sportives propulsé par l'intelligence artificielle**. L'application propose chaque jour des prédictions de buteurs pour les matchs de football, avec une offre gratuite et un abonnement **Premium** payé par carte via **Stripe**.

ButeurIA est disponible sur **trois plateformes** :

| Plateforme | Accès | Points à tester |
|---|---|---|
| Web | Navigateur (Chrome, Firefox, Safari) | Inscription, connexion, tableau de bord, prédictions, paiement |
| Android | Application mobile (Play Store) | Lancement, notifications push, navigation native, mode hors-ligne |
| iOS | Application mobile (App Store) | Inscription, clavier, partage natif, permissions |

En parallèle, l'équipe prépare un **second produit SaaS**, encore en phase de pré-lancement : une **plateforme d'orchestration d'agents IA** destinée aux TPE et PME, qui connecte plusieurs intelligences artificielles aux outils du quotidien pour améliorer la productivité des collaborateurs (voir [phase 2](#phase2)).

<h2 id="organisation">2. Organisation du travail et outils</h2>

Le stage s'est déroulé **entièrement à distance**. La journée était rythmée par :

- un **point du matin** avec le tuteur, pour fixer les parcours à tester ;
- une **journée de tests**, avec la saisie de chaque anomalie dans le tableau de suivi ;
- un **débriefing du soir**, pour relire les anomalies, les prioriser et noter dans le journal de bord ce que j'avais appris et ce qui m'avait bloqué.

| Outil | Usage pendant le stage |
|---|---|
| Chrome DevTools / Firefox DevTools | Lire les erreurs JavaScript (onglet *Console*) et les codes HTTP (onglet *Network*), simuler une connexion lente |
| Lighthouse | Auditer les performances et l'accessibilité de la page d'accueil |
| Android Studio (Logcat) | Lire les journaux de l'application Android lors d'un crash |
| Tableur (Excel) | Tableau de suivi QA : anomalies, idées d'amélioration, journal de bord, synthèse automatique |
| Loom / Notion | Enregistrement vidéo des bugs, prise de notes |
| Git / GitHub | Découverte du versioning : clés SSH, branches, messages de commit |

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : vue d'ensemble du tableau de suivi QA (onglet « Bugs & QA »)</div>

<h2 id="phase1">3. Phase 1 : campagnes de tests sur ButeurIA (18 mai - 5 juin)</h2>

### 3.1 Démarche

J'ai testé l'application **parcours par parcours** : inscription, connexion et mot de passe oublié, consultation des prédictions (filtres, tri, recherche), compte utilisateur, paiement Premium, puis les spécificités mobiles. Pour chaque parcours, je testais d'abord le cas normal, puis les **cas limites** : champ vide, espaces avant ou après un email, mot de passe de 3 caractères, accents (« Mbappé »), noms d'équipe très longs, connexion coupée, etc.

Chaque anomalie est classée par **type** et par **gravité** :

| Gravité | Définition retenue | Exemple |
|---|---|---|
| <span class="sev-b">Bloquant</span> | Empêche un parcours essentiel ou fait perdre de l'argent | Le bouton « Souscrire Premium » renvoie une page 404 |
| <span class="sev-m">Majeur</span> | Le parcours fonctionne mal ou induit l'utilisateur en erreur | Aucun message si l'email est déjà utilisé |
| Mineur | Gêne l'utilisateur sans bloquer | Pas d'indicateur de chargement |
| Cosmétique | Défaut visuel ou de texte | Avatar carré au lieu de rond sur Firefox |

### 3.2 Résultats chiffrés

<div markdown="1" class="row g-3 text-center my-3">
<div markdown="1" class="col-6 col-md-3"><div markdown="1" class="stat"><span class="stat-num">48</span><span class="stat-lbl">retours QA documentés</span></div></div>
<div markdown="1" class="col-6 col-md-3"><div markdown="1" class="stat"><span class="stat-num">6</span><span class="stat-lbl">anomalies bloquantes</span></div></div>
<div markdown="1" class="col-6 col-md-3"><div markdown="1" class="stat"><span class="stat-num">15</span><span class="stat-lbl">anomalies majeures</span></div></div>
<div markdown="1" class="col-6 col-md-3"><div markdown="1" class="stat"><span class="stat-num">14</span><span class="stat-lbl">corrigées pendant le stage</span></div></div>
</div>

| Répartition par type | Nombre | | Répartition par plateforme | Nombre |
|---|---|---|---|---|
| Bugs | 32 | | Web (Chrome) | 31 |
| Améliorations UX | 11 | | Android | 9 |
| Performance | 4 | | iOS | 5 |
| Faute d'orthographe | 1 | | Web (Firefox / Safari) | 3 |

À la fin de la phase 1 : **14 anomalies corrigées** par l'équipe, **8 en cours de correction** et **26 nouvelles** transmises pour la suite.

### 3.3 Les 6 anomalies bloquantes

| N° | Plateforme | Anomalie | Statut |
|---|---|---|---|
| 3 | iOS | Le bouton « S'inscrire » reste figé, sans réaction visuelle | <span class="sev-ok">Corrigé</span> |
| 7 | Web Firefox | « Mot de passe oublié » mène à une page blanche (erreur 500) | <span class="sev-ok">Corrigé</span> |
| 15 | Web | « Souscrire Premium » renvoie une 404 (`/checkout/premium` inexistant) | <span class="sev-ok">Corrigé</span> |
| 18 | Android | Notifications push reçues à 4 h du matin | En cours |
| 26 | Android | Crash au lancement après la mise à jour 1.4.2 (Android 11 et 12) | En cours |
| 34 | Web | Page de paiement Stripe affichant les prix en dollars au lieu d'euros | En cours |

### 3.4 Trois anomalies analysées en détail

#### Anomalie n°3 : bouton « S'inscrire » figé sur iOS (bloquant)

| Rubrique | Contenu |
|---|---|
| Environnement | iPhone, iOS 17.4, application mobile |
| Étapes | 1. Ouvrir l'app &rarr; 2. « Créer un compte » &rarr; 3. Remplir tous les champs &rarr; 4. Appuyer sur « S'inscrire » |
| Attendu | Création du compte puis redirection vers l'accueil |
| Obtenu | Rien ne se passe, aucun retour visuel |

**Difficulté :** le bug était **intermittent** (environ une fois sur trois).
**Méthode :** j'ai refait le test **10 fois** en notant à chaque essai les valeurs saisies. Le bug n'apparaissait qu'avec un **mot de passe contenant un caractère spécial**. Cette précision a permis au développeur de cibler rapidement la cause. Statut : corrigé.

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : fiche de l'anomalie n°3 dans le tableau de suivi</div>

#### Anomalie n°13 : accents cassés (« Vin?cius J?nior ») (majeur)

Sur la page Prédictions, certains noms de joueurs s'affichaient avec des `?` à la place des lettres accentuées. En comparant les noms cassés et les noms corrects, et en m'appuyant sur la documentation MDN sur les jeux de caractères (*charset*), j'ai compris qu'il s'agissait d'un **problème d'encodage côté serveur** (données non transmises en UTF-8) et non d'un problème d'affichage. Extrait de ce que j'ai vérifié dans l'onglet *Network* :

```http
# En-tête attendu dans la réponse de l'API
Content-Type: application/json; charset=utf-8
```

Statut : corrigé par l'équipe.

#### Anomalie n°34 : prix en USD sur la page de paiement Stripe (bloquant)

En cliquant sur « Souscrire Premium », la page de paiement affichait les prix en **dollars** pour un utilisateur français. Pour vérifier que cela ne dépendait pas de ma localisation, j'ai **refait le test avec un VPN réglé sur la France puis sur les États-Unis**, et consulté la documentation Stripe sur la gestion des devises. Conclusion transmise au tuteur : la devise dépend de la **configuration du compte / des prix côté Stripe**, pas du navigateur. Statut : correction en cours.

<h2 id="procedures">4. Procédures et tutoriels rédigés</h2>

### 4.1 Modèle de rapport d'anomalie

C'est le modèle que j'ai utilisé pour chaque ligne du tableau de suivi :

```text
N°            : 13
Date          : 26/05/2026
Titre         : Nom de joueur 'Vinícius Júnior' affiché avec ??? au lieu des accents
Type          : Bug              Gravité : Majeur
Plateforme    : Web Chrome       Écran    : Page Prédictions
Étapes        : 1. Filtrer par Real Madrid
                2. Regarder la carte de Vinícius
Attendu       : Accents corrects (Vinícius Júnior)
Obtenu        : Encodage cassé : 'Vin?cius J?nior'
Statut        : Nouveau -> En cours fix -> Corrigé
```

Règles que j'ai appliquées : **un seul problème par fiche**, des étapes **reproductibles par quelqu'un d'autre**, l'**environnement exact** (navigateur, version d'iOS ou d'Android) et une capture ou une vidéo Loom.

### 4.2 Auditer une page avec Lighthouse

1. Ouvrir la page dans Chrome, puis `F12` &rarr; onglet **Lighthouse**.
2. Choisir le mode **Navigation**, l'appareil **Mobile** et les catégories *Performance* et *Accessibility*.
3. Dans les réglages, garder la **limitation réseau simulée** (connexion mobile lente).
4. Cliquer sur **Analyze page load** et relever les scores et les métriques Web Vitals (LCP, CLS…).

Résultats obtenus sur ButeurIA : **Performance 38/100** sur la page d'accueil (images non optimisées, JavaScript bloquant, anomalie n°21) et **contraste de 2,3:1** sur les boutons secondaires, sous le minimum WCAG AA de 4,5:1 (anomalie n°47).

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : rapport Lighthouse de la page d'accueil</div>

### 4.3 Simuler une connexion 3G avec les DevTools

1. `F12` &rarr; onglet **Network**.
2. Dans la liste déroulante de limitation (*No throttling*), choisir **3G**.
3. Cocher **Disable cache**, puis recharger avec `Ctrl + Maj + R` (`Cmd + Maj + R` sur Mac).
4. Lire le temps de chargement complet en bas de l'onglet (*Load*).

Résultat : **8,3 secondes** pour charger l'accueil, contre un objectif de moins de 5 secondes (anomalie n°36).

### 4.4 Lire les journaux d'un crash Android (Logcat)

1. Activer les **options pour les développeurs** sur le téléphone, puis le **débogage USB**.
2. Brancher le téléphone, ouvrir **Android Studio** &rarr; onglet **Logcat**.
3. Sélectionner l'appareil, puis filtrer les erreurs de l'application :

```text
package:mine level:error
```

4. Lancer l'application et relever la pile d'erreur (*stack trace*) affichée au moment du crash pour la joindre à la fiche (anomalie n°26 : crash après la mise à jour 1.4.2).

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : Logcat au moment du crash</div>

### 4.5 Configurer Git et une clé SSH pour GitHub

Mon tuteur a cité Git et GitHub comme l'un de mes principaux apprentissages du stage. Voici la configuration que j'ai mise en place :

```bash
# Identité Git
git config --global user.name "Anis LOUCIF"
git config --global user.email "anis.loucif91@gmail.com"

# Création d'une clé SSH et ajout à l'agent
ssh-keygen -t ed25519 -C "anis.loucif91@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copier la clé publique, puis la coller dans GitHub > Settings > SSH and GPG keys
cat ~/.ssh/id_ed25519.pub

# Tester la connexion
ssh -T git@github.com
```

Travail avec les branches :

```bash
git switch -c docs/rapport-stage     # créer une branche dédiée
git add .
git commit -m "docs: ajout du rapport de stage SIO1"
git push -u origin docs/rapport-stage
git switch master && git merge docs/rapport-stage   # fusion une fois validé
```

Un des axes de progrès relevés par mon tuteur était **la rigueur des messages de commit**. J'utilise depuis une convention simple : `type: description courte`, avec `fix`, `feat`, `docs` ou `style` comme type.

<h2 id="ameliorations">5. Propositions d'amélioration</h2>

En plus des anomalies, j'ai proposé **16 idées d'amélioration**, chacune évaluée par son impact estimé et sa difficulté. Ma sélection :

| Idée | Catégorie | Impact | Difficulté |
|---|---|---|---|
| Bouton « Copier le lien » sur les prédictions | UX | Fort | Facile |
| Partage WhatsApp (canal principal pour les pronostics entre amis) | Fonctionnalité | Fort | Facile |
| Onboarding en 3 écrans au premier lancement | UX | Fort | Moyen |
| Page « Comment marche notre IA » (transparence, taux de réussite) | Marketing | Fort | Moyen |
| Mode sombre automatique (`prefers-color-scheme`) | UX | Moyen | Facile |
| FAQ dans le pied de page pour réduire les emails au support | UX | Moyen | Facile |

Mon tuteur a souligné que j'étais **force de proposition**.

<h2 id="phase2">6. Phase 2 : observation d'un projet d'orchestration d'agents IA (6 - 26 juin)</h2>

Pendant la seconde phase, j'ai suivi en **observation** un nouveau projet SaaS de l'équipe : une plateforme qui permet aux **TPE et PME** de connecter plusieurs intelligences artificielles (des « agents ») à leurs outils du quotidien.

Le projet étant **sensible et encore en pré-lancement**, je n'ai pas participé au développement. J'ai pu :

- assister aux phases de **conception** et découvrir l'**architecture technique générale** d'un produit IA ;
- comprendre les **enjeux** d'un produit IA en entreprise : fiabilité des réponses, sécurité des données, coût d'utilisation des modèles ;
- mener une **veille technologique** sur les agents IA et les protocoles qui leur permettent de se connecter aux outils (MCP, A2A).

Cette phase est à l'origine du sujet de [ma veille technologique]({filename}/pages/ma-veille.md).

<h2 id="competences">7. Compétences du référentiel BTS SIO mobilisées</h2>

| Bloc | Compétence | Mise en œuvre pendant le stage |
|---|---|---|
| Bloc 2 SLAM | Assurer la maintenance corrective ou évolutive d'une solution applicative | Recherche, reproduction et documentation de 48 anomalies, suivi de leur correction |
| Bloc 2 SLAM | Élaborer et réaliser les tests des éléments mis à jour | Nouveau test des parcours après correction, mise à jour des statuts (« En cours » &rarr; « Corrigé ») |
| Bloc 2 SLAM | Évaluer la qualité d'une solution applicative | Audits Lighthouse (performance, accessibilité), tests multi-navigateurs et multi-plateformes |
| Bloc 1 | Répondre aux incidents et aux demandes d'assistance et d'évolution | Qualification des incidents (type, gravité), propositions d'évolution |
| Bloc 1 | Travailler en mode projet | Point quotidien, priorisation des anomalies par criticité, synthèse finale avec le tuteur |
| Bloc 1 | Organiser son développement professionnel | Journal de bord quotidien, apprentissage par la documentation (MDN, Chrome DevTools, Stripe), veille sur les agents IA |
| Bloc 1 | Développer la présence en ligne de l'organisation | Remarques SEO (CGU en PDF, page 404, temps de chargement) |

<h2 id="bilan">8. Bilan du stage</h2>

### Appréciation du tuteur

<blockquote markdown="1">
« Anis s'est très bien intégré dès son arrivée. Il est sociable, à l'écoute, et n'hésite pas à poser des questions lorsqu'il rencontre une difficulté. […] Il a montré de réelles capacités d'apprentissage, notamment sur les outils de versioning (Git, GitHub, clés SSH, gestion de branches). Il est également force de proposition. »
</blockquote>

### Ce que j'ai appris

- **Tester méthodiquement** : cas normaux et cas limites, reproduction systématique, une fiche par problème.
- **Écrire pour être compris** : un développeur doit pouvoir reproduire mon bug sans me poser de question.
- **Prioriser** : un bug sur le paiement passe avant un défaut d'affichage.
- **Utiliser les outils du développeur** : DevTools, Lighthouse, Logcat, Git avec SSH et les branches.

### Axes de progrès (identifiés avec mon tuteur)

- Consulter la **documentation officielle** avant de demander de l'aide. Je l'ai appliqué pour Lighthouse, l'encodage et Stripe (voir le journal de bord).
- Être plus rigoureux dans les **messages de commit** et la **documentation**.

### Limites et suite

Ce stage ne m'a pas fait coder sur l'application : le code de ButeurIA est complexe et en production, et une erreur de ma part aurait pu affecter les utilisateurs. En revanche, il m'a montré **l'autre moitié du métier de développeur** : la qualité, les tests et la relation avec l'équipe. Pour mon **stage de 2<sup>e</sup> année** (janvier-février 2027), je cherche une mission orientée **développement**, pour mettre en pratique ce que j'ai appris côté qualité.
