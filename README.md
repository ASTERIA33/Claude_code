# ✦ Elope & Away — Notes de projet

> Site éditorial et affiliate sur le mariage intime / elopement en Europe.  
> Stack : HTML/CSS/JS statique · Hébergement : [à définir] · Domaine : [à définir]

---

## 1. Vision & Positionnement

### Concept
Site éditorial francophone sur l'elopement en Europe — destinations, guide légal, budget, photographes.  
Modèle économique mixte : **contenu SEO longue traîne + monétisation affiliate** (hébergement, prestataires, guides PDF).

### Proposition de valeur
> *"Vous voulez que votre mariage ressemble à votre vie — pas à un catalogue."*

Se différencier des blogs mariage généralistes en adoptant un ton éditorial fort, une DA haut de gamme (ivoire / terracotta / grain film), et un positionnement destinations Europe plutôt que France uniquement.

### Cible
- Couples 28–38 ans, CSP+, sensibles à l'esthétique
- Recherches type : "elopement Portugal", "mariage intime Écosse", "comment se marier en Toscane"
- Canal d'acquisition principal : **Google (SEO)** + Pinterest secondaire

### Destinations prioritaires
| Destination | Priorité | Statut contenu |
|---|---|---|
| Portugal (Sintra, Douro) | 🔴 P1 | À écrire |
| Écosse (Highlands, Skye) | 🔴 P1 | À écrire |
| Toscane (Val d'Orcia) | 🟠 P2 | À écrire |
| Provence | 🟠 P2 | À écrire |
| Açores | 🟡 P3 | Idée |

---

## 2. Direction Artistique

### Palette
```
Ivoire chaud    #F5EFE0   — fond principal
Terre de Sienne #C4845A   — accent CTA / liens
Brun encre      #2D1F14   — texte
Or pâle         #D4AF7A   — highlights, séparateurs
Ivoire secondaire #EDE5D2 — sections alternées
```

### Typographie
| Rôle | Police | Style |
|---|---|---|
| Titres | Playfair Display | Italic, 300–700 |
| Corps / UI | Karla | Light 300, Regular 400 |

### Règles DA
- Grain film sur toutes les images (SVG noise, opacity 12–18%)
- Jamais de blanc pur — toujours ivoire cassé
- Accent terracotta utilisé avec parcimonie (CTA, numéros, tags)
- Illustrations botaniques SVG en fil fin, opacity 0.08–0.15

---

## 3. Architecture Technique

### Structure des fichiers
```
/
├── index.html              ← Page d'accueil
├── /destinations/
│   ├── portugal.html
│   ├── ecosse.html
│   └── toscane.html
├── /guides/
│   ├── budget-elopement.html
│   ├── demarches-legales.html
│   └── choisir-photographe.html
├── /blog/                  ← Articles SEO longue traîne
├── /assets/
│   ├── /css/
│   ├── /js/
│   └── /img/               ← WebP uniquement, max 200kb
└── sitemap.xml
```

### Règles techniques
- **Mobile-first** obligatoire — breakpoint principal à 700px
- Images en **WebP**, ratio cohérent par section
- LCP < 2.5s — pas de vidéo autoplay, pas de Google Fonts bloquant
- Pas de framework JS pour le site vitrine (HTML/CSS/JS vanilla)
- Structured data : `Article` + `BreadcrumbList` + `FAQPage` sur les guides

### Performance cibles
| Métrique | Cible |
|---|---|
| LCP | < 2.5s |
| CLS | < 0.1 |
| FID / INP | < 200ms |
| PageSpeed mobile | > 85 |

---

## 4. Stratégie SEO & Affiliate

### Architecture sémantique
```
Piliers (pages destinations)
  └── Clusters (articles supports)
        └── Longue traîne (questions spécifiques)
```

**Exemple pour Portugal :**
- Pilier : `elopement Portugal — guide complet`
- Clusters : `mariage Sintra`, `budget elopement Portugal`, `photographes Portugal`
- Longue traîne : `peut-on se marier légalement à Sintra en tant que français ?`

### Mots-clés prioritaires (FR)
| Mot-clé | Volume est. | Intention | Priorité |
|---|---|---|---|
| elopement portugal | 500/mois | Informationnel | 🔴 P1 |
| mariage intime écosse | 200/mois | Informationnel | 🔴 P1 |
| elopement toscane | 300/mois | Informationnel | 🔴 P1 |
| comment organiser un elopement | 400/mois | Navigationnel | 🔴 P1 |
| photographe elopement europe | 150/mois | Transactionnel | 🟠 P2 |
| budget mariage intime | 350/mois | Informationnel | 🟠 P2 |

### Modèle affiliate
| Type | Plateforme / Programme | Commission est. |
|---|---|---|
| Hébergements | Booking.com Affiliate | 25–40% commission |
| Hôtels boutique | HotelBeds / Mr & Mrs Smith | Variable |
| Photographes | Annuaire avec referral | À négocier |
| Guides PDF | Vente directe (Gumroad / Lemon Squeezy) | 100% |
| Assurance voyage | AXA / Chapka affilié | ~15% |

### Maillage interne — règles
- Chaque article de blog → lien vers 1 page destination + 1 guide pratique
- Chaque page destination → lien vers 2–3 articles supports
- Footer : liens vers toutes les destinations + guides principaux

### Netlinking
- Cible : annuaires mariage FR (Zankyou, Mariages.net) + blogs voyage
- Format : guest posts sur blogs lifestyle / voyage CSP+
- Pinterest : 1 épingle par article, format vertical 2:3, texte overlay

---

## 5. Roadmap

### Phase 1 — MVP (J+0 à J+60)
- [ ] Finaliser DA et système de design
- [ ] Coder la homepage
- [ ] Écrire 3 pages destinations (Portugal, Écosse, Toscane)
- [ ] Écrire 2 guides piliers (budget, démarches légales)
- [ ] Mettre en ligne + Google Search Console

### Phase 2 — Contenu & SEO (J+60 à J+120)
- [ ] 10 articles longue traîne (2 par destination)
- [ ] Guide PDF "Organiser son elopement en Europe" (lead magnet)
- [ ] Formulaire capture email + séquence Klaviyo ou Brevo
- [ ] Intégration affiliate Booking.com
- [ ] Pinterest : 20 épingles initiales

### Phase 3 — Monétisation (J+120+)
- [ ] Annuaire photographes (modèle freemium ou referral)
- [ ] Pack PDF premium
- [ ] Partenariats hébergements boutique (Portugal, Toscane)
- [ ] Envisager version EN pour Portugal / Écosse

---

## 6. Notes & Ressources

### Outils utilisés
- **Design** : Fichier DA en `/docs/DA_elopement_site.md`
- **SEO** : DataForSEO pour les volumes · Ahrefs pour le netlinking
- **Affiliate** : Affilae (si programme FR) · Booking Partner Hub
- **Emails** : Brevo ou Klaviyo
- **Hébergement** : OVH / Netlify / GitHub Pages à décider

### Références concurrentes
| Site | Ce qu'il fait bien | Ce qu'on fait mieux |
|---|---|---|
| [À compléter] | | |

### Lectures utiles
- [ ] Guide légal mariage à l'étranger (service-public.fr)
- [ ] Étude marché mariage intime Europe 2024
- [ ] Programmes affiliate voyage comparatif

---

*Dernière mise à jour : [date] — Florian*
