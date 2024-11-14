---
alias: "GPT4 Minecraft"
title: "Voyager: comment GPT4 joue à Minecraft"
---

# Description

GPT4 a été créé pour compléter du texte, répondre à des questions et plus tardivement expliquer comment résoudre des tâches spécifiques.

Mais des chercheurs ont réussi à le faire jouer à minecraft, ce qui est assez incroyable: on ne s'attend pas du tout à ce qu'un modèle de ce genre soit capable de naviguer dans un monde de jeux vidéos.

Cette prouesse s'appelle "Voyager".

# Article

<https://arxiv.org/pdf/2305.16291>

# Fonctionnement

L'idée générale, c'est de demander en boucle à chatGPT quelque chose de ce genre:

> Ton but est de me donner la prochaine tâche à effectuer dans Minecraft.
> Ton dernier objectif était: ...
> Tu as accès à ...
> Ton inventaire contient ...
> (Et plein d'autres informations)
> Réfléchis à tout ça et donne moi le prochain objectif qu'il faut que tu atteignes.

Ensuite, une fois qu'on a la tâche à accomplir, on demande à GPT4 de programmer cette fonctionnalité (en javascript). Donc pour être clair, il ne joue pas au jeu comme un humain (il n'utilise pas de vision), mais il interagit avec le jeu en écrivant des instructions. C'est comme si vous n'aviez pas de claviers et de souris, mais des boutons "avancer", "casser un bloc", "ouvrir son inventaire" ...

Le plus gros du travail de ce papier, c'est de proposer une tuyauterie (*scaffholding* ou échafaudage en anglais) pour qu'une boite noire qui ne peut que répondre à des questions arrive à progresser dans un jeu.

Tous les blocs dans le schéma suivant sont des instances de GPT4 (ou GPT3.5) avec des prompts différents.

![[voyager 2024-05-26 22.34.23.excalidraw.svg]]
%%[[voyager 2024-05-26 22.34.23.excalidraw.md|🖋 Edit in Excalidraw]]%%

Toutes les flèches vertes et rouges sont **uniquement des échanges de texte**

## Mémoire

Un aspect qui n'est pas très détaillé dans le papier est l'utilisation de la mémoire. Et c'est une grande question de recherche: comment faire en sorte qu'une IA puisse utiliser une mémoire à long terme. En particulier, comment faire pour qu'il apprenne des compétences pour s'en servir plus tard.

À chaque fois que Voyager écrit un programme qui fonctionne, ce programme est ajouté à une bibliothèque.

Elle contient une liste de fonctionnalités, c'est à dire à chaque fois un programme et une description associée.

![](voyager 2024-05-26 23.06.36.excalidraw.svg)
%%[[voyager 2024-05-26 23.06.36.excalidraw.md|🖋 Edit in Excalidraw]]%%


Quand Voyager doit effectuer une nouvelle tâche, on va chercher dans la bibliothèque les fonctionnalités qui pourraient lui être utile. Pour faire cela, on calcule une "distance sémantique" entre le plan actuel et les descriptions des différentes fonctions.


![](voyager 2024-05-26 22.55.13.excalidraw.svg)
%%[[voyager 2024-05-26 22.55.13.excalidraw.md|🖋 Edit in Excalidraw]]%%


Si la distance est faible (=le sens est proche), on va lui rappeler dans son prompt:

> N'oublie pas que tu sais faire les choses suivantes:
> ...

# Bilan

Voyager est assez perturbant: c'est un **bricolage** autour de GPT4, qui lui permet de faire des choses assez folles.

## Puissance

Les idées développées dans Voyager sont assez puissantes:
- on peut faire évoluer et réfléchir un LLM juste en le faisant parler avec lui même, avec la bonne tuyauterie
- La qualité de cette tuyauterie (scaffolding) peut permettre au système de résoudre des tâches très complexes
- en écrivant du code, on peut faire énormément de choses, et avoir un impact sur le monde.
- Voyager est assez facile à comprendre, parce que tout ce qui se passe dans son cerveau est du texte. On ne peut pas savoir pourquoi il a généré ce texte, mais si un jour il prend une décision étrange, on peut suivre un espèce de processus de pensée en lisant tous les messages qui ont été écrits.

## Limitations

Le papier montre aussi des limitations que l'on a a l'heure actuelle:
- Voyager n'arrive pas à atteindre certains objectifs, il continue d'essayer la même chose en boucle alors que cela ne fonctionne pas
- Voyager n'apprend presque pas. Il a déjà une très bonne connaissance du jeu (GPT3.5 a été entraîné sur un grand nombre de site internet et de discussions, et Minecraft est très populaire)
- La mémoire, c'est du bricolage et ça ne marche pas super bien (pour l'instant)
- Cette architecture ne va jamais proposer une solution très innovante, parce que la structure (le scaffholding) est fixée. C'est à la fois une bonne chose (on ne risque pas d'être surpris par [[danger-optimisation-renforcement|specification gaming]]), et une limitation dans ce que peut faire le modèle.