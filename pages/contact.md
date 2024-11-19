{% extends "md_page.html" %}
{% block md_content %}
{% markdown %}

<h2 id="mail">Par mail</h2>

Vous pouvez contacter l'association à l'adresse [contact@piaf-saclay.org](mailto: contact@piaf-saclay.org).

<h2 id="nous-rejoindre">Nous rejoindre</h2>

Vous pouvez venir discuter avec nous, pour approfondir la sûreté de l'IA et participer à nos [groupes de lecture](/groupe-de-lecture.html).

Nous communiquons principalement sur Discord :

{% set link=DISCORD_SERVER %}
{% set link_icon_class="bi-discord" %}
{% set btn_text="Rejoindre la discussion" %}
{% include "button.html" %}

<br>

Pour faire partie de l'association, envoyez-nous un [mail](/contact.html#mail) ou rejoignez le serveur Discord.

Consultez aussi [cette page](/nous-aider.html) pour d'autres manières de nous aider.

{% endmarkdown %}
{% endblock %}