{% extends "md_page.html" %}
{% block md_content %}
{% markdown %}

## Éditeur du site

Ce site est édité par l'association de loi 1901 **Pour une Intelligence Artificielle Fiable - PIAF**, domiciliée à l'adresse suivante :

19 Place Marguerite Perey, 91120 Palaiseau, France

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