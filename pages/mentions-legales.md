{% extends "md_page.html" %}
{% block md_content %}
{% markdown %}


## Éditeur du site

Ce site est édité par **Pour une Intelligence Artificielle Fiable - PIAF**.

Au 29 novembre 2024, PIAF n'a pas encore de statut légal, mais sera une association de loi 1901.

[Numéro Siret]: #

## Hébergeur du site

Ce site est hébergé par Github Pages. GitHub B.V. est domicilié à l'adresse suivante :

Prins Bernhardplein 200, Amsterdam 1097JB, Pays-Bas

## Contact

Rendez-vous sur la page dédiée.

{% set link="/contact.html" %}
{% set link_icon_class="bi-envelope-at" %}
{% set btn_text="Contact" %}
{% include "button.html" %}

{% endmarkdown %}
{% endblock %}