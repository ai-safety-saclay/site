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
