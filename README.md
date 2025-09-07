# piaf-saclay.org

## Description

Le site de l'association PIAF, écrit en Bootstrap + SCSS généré statiquement via Markdown et Jinja

## Développement local

### Environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Dépendances Python

```bash
python -m pip install .
```


### Déploiement

```bash
python3 __main__.py
cd ./build
python3 -m http.server 8080
```

Le site est disponible sur http://localhost:8080.


## TODO

- relire `presentation_piaf.md` et comparer avec l'objet de l'asso défini dans les statuts
- achever les `mentions_legales.md` et `confidentialite.md`
- relire la page `groupe_de_lecture.md`
- relire la page `nous_aider.md`
- section "À la une" :
  - récupérer le RSS depuis https://blog.piaf-saclay.org/index.xml
  - créer un carousel
- Créer un carousel pour les événements passés et à venir (pages Asimov, Jeud'IA)
- écrire la liste des exposés sur le blog
- boutons :
  - faut-il utiliser les boutons officiels de YouTube et de Discord ?
- régler les bugs de `style.scss`
- définir le thème du site
  - fixer une gamme de couleurs, une police d'écriture
  - adapter le logo
- réorganiser les pages si nécessaire
- ajouter la liste des pages, générée automatiquement
- indiquer comment faire un don ou soutenir l'association en tant que sponsor par ex.