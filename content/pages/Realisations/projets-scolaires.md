Title: Projets scolaires : ateliers professionnels de 1re année
Slug: projets-scolaires
Date: 2026-10-09
Kicker: Réalisations · Ateliers professionnels (AP)
Lead: Comptes rendus des deux ateliers professionnels réalisés en 1re année de BTS SIO : le site de l'Hôtel Chambord (front-end) et l'application Cinéma connectée à l'API TMDB (PHP).

<div markdown="1" class="row g-3 mb-4">
<div markdown="1" class="col-md-6"><div markdown="1" class="info-card">
<p class="kicker mb-1">AP · 1re année (déc. 2025)</p>
<h3 class="h5"><a href="#ap1">Site web de l'Hôtel Chambord</a></h3>
<p class="small mb-2">Site vitrine et espace de gestion d'un hôtel de luxe : 19 pages responsives.</p>
<span class="skill">HTML5</span><span class="skill">CSS3</span><span class="skill">Bootstrap 5</span><span class="skill">JavaScript</span>
</div></div>
<div markdown="1" class="col-md-6"><div markdown="1" class="info-card">
<p class="kicker mb-1">AP · 1re année (avril 2026)</p>
<h3 class="h5"><a href="#ap2">Cinéma : application connectée à l'API TMDB</a></h3>
<p class="small mb-2">Recherche de films et d'acteurs, fiche acteur avec filmographie, via une API REST.</p>
<span class="skill">PHP 8</span><span class="skill">API REST</span><span class="skill">JSON</span><span class="skill">Bootstrap 5</span>
</div></div>
</div>

<h2 id="ap1">AP « Hôtel Chambord » : site web d'un hôtel de luxe</h2>

<p>
<a href="https://anisloucif.github.io/AP3_hotel_chambord_anisloucif.github.io/" target="_blank" rel="noopener" class="btn btn-primary btn-sm"><i class="bi bi-globe"></i> Voir le site en ligne</a>
<a href="https://github.com/anisloucif/AP3_hotel_chambord_anisloucif.github.io" target="_blank" rel="noopener" class="btn btn-outline-dark btn-sm"><i class="bi bi-github"></i> Code source</a>
</p>

### 1. Contexte

L'**Hôtel Chambord** est un hôtel de luxe fictif, situé au cœur du domaine de Chambord, qui propose des chambres, un restaurant, un spa et des activités (golf, balades à vélo, montgolfière). L'établissement souhaite un **site web** pour présenter son offre, permettre aux clients de **réserver** et de le **contacter**, et disposer d'une **partie d'administration** pour son personnel (utilisateurs, services, offres d'emploi).

### 2. Cahier des charges (besoins traités)

| Besoin | Réponse apportée |
|---|---|
| Présenter l'hôtel et ses services | Pages Accueil, Chambres, Restaurant, Spa, Activités, Avis clients |
| Permettre la réservation | Page Réservation à onglets : chambre, table au restaurant, soin au spa |
| Être contacté | Page Contact avec formulaire (nom, prénom, email, sujet, message) |
| Gérer les comptes clients | Connexion, création de compte, mot de passe oublié, modification du compte |
| Administrer le site | Tableau d'administration, gestion des utilisateurs et des services, gestion du restaurant |
| Recruter | Page Recrutement (postes disponibles, candidature spontanée) et création d'offres d'emploi |
| Être consultable sur mobile | Mise en page responsive avec Bootstrap 5 |
| Gérer les erreurs | Page 404 personnalisée |

### 3. Solutions techniques adoptées

**Arborescence du projet :**

```text
AP3_hotel_chambord/
├── index.html                  # page d'accueil
├── css/
│   ├── bootstrap.css           # framework Bootstrap 5 (local)
│   ├── global.css              # styles communs (bandeaux, couleurs)
│   └── recrutement.css         # styles propres à la page Recrutement
├── js/
│   ├── bootstrap.js            # composants Bootstrap (menu, onglets)
│   └── main.js                 # animation d'apparition des sections
├── img/                        # photos (chambres, spa, restaurant…)
└── pages/                      # 18 pages : chambres, reservation, admin, contact…
```

**Choix techniques :**

- **Bootstrap 5 en local** pour la grille responsive, la barre de navigation repliable (`navbar-expand-lg`), les cartes, les onglets de réservation et les formulaires (`form-control`, `form-select`).
- **Une classe CSS de bandeau par page** (`.bandeau-bg-chambres`, `.bandeau-bg-restaurant`…) : une même structure HTML, une image de fond différente.
- **Formulaires HTML5 avec validation native** (`required`, `type="email"`, `type="date"`) et des étiquettes `<label for>` reliées aux champs pour l'accessibilité.
- **Un peu de JavaScript** pour faire apparaître les sections au défilement.

### 4. Extraits de code

Bandeau de page réutilisable (`css/global.css`) :

```css
.bandeau-bg-chambres {
  background-image: url("../img/chambre-1.jpg");
  background-size: cover;
  background-position: center;
  padding: 1rem 0;
  z-index: 1;
  height: 88vh;
}
```

Formulaire de réservation d'une chambre (`pages/reservation.html`, extrait) :

```html
<form class="row g-3" action="#" method="post">
  <div markdown="1" class="col-md-6">
    <label for="type-chambre" class="form-label">Type de chambre</label>
    <select id="type-chambre" name="type-chambre" class="form-select" required>
      <option value="">Sélectionnez une chambre</option>
      <option>Cosy</option>
      <option>Cosy vue rivière</option>
      <option>De luxe vue château</option>
      <option>Suite vue château</option>
    </select>
  </div>
  <div markdown="1" class="col-md-3">
    <label for="date-arrivee" class="form-label">Date d'arrivée</label>
    <input type="date" id="date-arrivee" name="date-arrivee" class="form-control" required />
  </div>
</form>
```

Apparition des sections au défilement (`js/main.js`) :

```javascript
document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll("section");

  function handleScroll() {
    sections.forEach((section) => {
      const rect = section.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        section.classList.add("fade-in");   // la section devient visible
      }
    });
  }

  window.addEventListener("scroll", handleScroll);
  handleScroll();
});
```

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : page d'accueil de l'Hôtel Chambord (ordinateur et mobile)</div>
<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : page Réservation (onglets chambre / restaurant / spa)</div>

### 5. Bilan

**Ce qui fonctionne :** un site complet de **19 pages**, responsive, cohérent graphiquement et **publié en ligne** sur GitHub Pages.

**Limites que j'ai identifiées :**

- Le site est **uniquement front-end** : les formulaires (réservation, contact, connexion) n'enregistrent rien. Ils pointent vers `action="#"` ou vers un `contact.php` qui n'existe pas encore.
- Les pages d'administration sont des **maquettes** : les tableaux d'utilisateurs et de services sont écrits en dur dans le HTML.
- Le projet a été déposé en **un seul commit**, sans historique Git du travail.

**Améliorations prévues :** ajouter un back-end **PHP / MySQL** (tables `client`, `reservation`, `chambre`, `service`), traiter les formulaires côté serveur avec des **requêtes préparées (PDO)**, protéger l'administration par une **authentification avec sessions** et un **mot de passe haché** (`password_hash`).

**Compétences mobilisées :** concevoir et développer une solution applicative (interfaces web), développer la présence en ligne de l'organisation, mettre à disposition un service (publication sur GitHub Pages).

---

<h2 id="ap2">AP « Cinéma » : application connectée à l'API TMDB</h2>

<p>
<a href="https://github.com/anisloucif/movie_api" target="_blank" rel="noopener" class="btn btn-outline-dark btn-sm"><i class="bi bi-github"></i> Code source</a>
</p>

### 1. Contexte

Il s'agit de développer une **application web de cinéma** qui ne stocke aucune donnée elle-même : elle interroge l'**API REST de The Movie Database (TMDB)** pour afficher les films populaires, rechercher des films et des acteurs, et consulter la fiche d'un acteur. L'application doit fonctionner **au lycée**, derrière le proxy du réseau, **et à la maison**, sans proxy.

### 2. Cahier des charges (besoins traités)

| Besoin | Réponse apportée |
|---|---|
| Afficher les films du moment | Page d'accueil `popular.php` : les 20 films les plus populaires |
| Rechercher un film | Formulaire dans l'en-tête &rarr; `search-films.php?query=…` |
| Rechercher un acteur | Formulaire dans l'en-tête &rarr; `search-acteurs.php?query=…` |
| Consulter un acteur (bonus) | `fiche-acteur.php?id=…` : photo, biographie, 20 films les plus populaires et rôle joué |
| Fonctionner au lycée et à la maison | Fonction `getProxy()` qui essaie la connexion directe puis la connexion par le proxy |
| Sécuriser les saisies | Vérification `isset` / `empty` et échappement `htmlspecialchars` |

### 3. Solutions techniques adoptées

| Fichier | Rôle |
|---|---|
| `get-proxy.php` | Requêtes HTTP vers l'API (connexion directe, sinon via le proxy du lycée) |
| `fonctions.php` | Fonctions d'appel à l'API (`popularMovies`, `searchFilms`, `searchActeurs`, `filmsParActeur`, `imgUrl`) |
| `header.php` / `footer.php` | Barre de navigation avec formulaires de recherche, pied de page (inclus sur toutes les pages) |
| `popular.php`, `search-films.php`, `search-acteurs.php`, `fiche-acteur.php` | Pages d'affichage en grille de cartes Bootstrap |

**Choix de la méthode `GET`** pour les formulaires : c'est une recherche, sans donnée sensible, et l'URL de résultat (`search-acteurs.php?query=tom`) peut être partagée ou mise en favori.

**Parcours d'une recherche :**

```text
[Saisie "batman"] --GET--> search-films.php?query=batman
   ├─ isset($_GET['query']) et !empty(trim(...))
   └─> searchFilms("batman")
         └─> getProxy(URL de l'API TMDB)
               └─> json_decode() -> tableau PHP
                     └─> foreach -> cartes Bootstrap
```

### 4. Extraits de code

Appel à l'API et tri de la filmographie d'un acteur (`fonctions.php`) :

```php
function filmsParActeur(int $personId): array
{
    $url      = API_BASE . '/person/' . $personId . '/movie_credits?api_key=' . API_KEY . '&language=fr-FR';
    $response = getProxy($url);
    $data     = json_decode($response, true);   // JSON -> tableau associatif
    $films    = $data['cast'] ?? [];

    // tri par popularité décroissante (opérateur "spaceship")
    usort($films, fn($a, $b) => ($b['popularity'] ?? 0) <=> ($a['popularity'] ?? 0));

    return array_slice($films, 0, 20);           // 20 films maximum
}
```

Connexion directe ou par le proxy du lycée (`get-proxy.php`, extrait) :

```php
$response = @file_get_contents($url, false, $context);   // 1. connexion directe
if ($response !== false) {
    return $response;
}

$proxyOptions = array_merge($sslOptions, [               // 2. sinon, via le proxy
    'http' => [
        'proxy'           => 'tcp://172.16.0.54:8080',
        'request_fulluri' => true,
    ],
]);
```

Vérification de la saisie avant l'appel à l'API (`search-acteurs.php`) :

```php
if (isset($_GET['query']) && !empty(trim($_GET['query']))) {
    $query     = htmlspecialchars(trim($_GET['query']));
    $resultats = searchActeurs($query);
}
```

<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : page des films populaires</div>
<div markdown="1" class="capture"><i class="bi bi-image"></i>Capture d'écran : fiche acteur avec sa filmographie</div>

### 5. Bilan

**Ce qui fonctionne :** les quatre fonctionnalités demandées et le bonus de la fiche acteur. L'application marche au lycée comme à la maison, et un compte rendu technique figure dans le dépôt (`ref/compte-rendu.md`).

**Limites que j'ai identifiées :**

- Le code est **procédural** (des fonctions, pas de classes). Une version **orientée objet** serait plus propre : une classe `TmdbClient` pour les appels à l'API et des classes `Film` et `Acteur` pour les données.
- La **clé d'API est écrite en clair** dans un dépôt public. Elle devrait être placée dans un fichier de configuration exclu de Git (`.gitignore`) ou dans une variable d'environnement.
- La **vérification SSL est désactivée** (`verify_peer => false`) pour contourner le proxy du lycée. C'est acceptable pour un TP, pas pour une application en production.
- Le projet a été déposé en **un seul commit**.

**Compétences mobilisées :** concevoir et développer une solution applicative (PHP, consommation d'une API REST), gérer les données (format JSON, tableaux associatifs), sécuriser les saisies utilisateur.
