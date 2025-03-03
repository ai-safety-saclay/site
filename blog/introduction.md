---
title: Rendre l'IA fiable
---

L'[:IA](#IA) n'est pas une technologie comme les autres. Elle pose des [:risques comparables](#Risks) aux technologies nuléaires ou de modification génétique.
Mais ses capacités d'apprentissage plus rapide que l'humain la rend particulièrement [:difficile à controler](#Control).

Il est urgent de [:rendre l'IA fiable](#Trust), c'est à dire éthique mais surtout sûre.
La recherche montre que c'est un [:problème très difficile](#Alignment), d'autant plus que les IA sont [:intelligentes et générales](#Capabilities).
Si la trajectoire actuelle continue, on court probablement à [:la catastrophe](#Collapse).

L'IA ne se résume pas à une question technique ou même éthique, car elle subit des pressions [:économiques](#Economy) et [:politiques](#Politics) intenses.
Vous serez probablement confronté au problème de la confiance en l'IA dans votre métier, et n'importe quel pas [:dans la bonne direction](#Actions) peut être décisif.


# :x IA

L'Intelligence Artificielle désigne n'importe quel système de traitement de l'information qui peut traiter des données complexes du monde réel, pour atteindre un objectif spécifique. Cela peut prendre en compte:
- les algorithmes de recommandation des réseaux sociaux
- les chatbots
- les logiciels de reconnaissance d'image
- les algorithmes de trading
...

On ne programme pas directement l'IA. On lui fait extrapoler des données, s'entrainer à des jeux contre elle même ou s'améliorer pour maximiser un score. Dans tous les cas, l'IA *apprend*, on parle de *Machine Learning*.
C'est ça la grande différence avec l'informatique "classique".

Les systèmes d'IA peuvent être plus ou moins "intelligents".
L'intelligence est difficile à définir, mais nul besoin d'avoir une définition parfaite pour réfléchir à l'IA.

En général, on considère que quaque IA a un *spectre d'intelligence*. Elle correspond à la capacité à raisonner et à atteindre des objectifs dans différents domaines.

Lorsque l'IA est très efficace pour des taches précises, on parle d'*IA experte*.
Lorsque l'IA peut résoudre un grand nombre de tâches différentes, on parle d'*IA générale*.

Et il y a beaucoup d'autre [: vocabulaire spécifique](#Voc) aux différentes IA.


Dans cette définition de l'intelligence, il n'y a absolument pas besoin de corps, de conscience ou de toute autre caractéristique humaine.

## :x Voc

TODO:
- AGI
- LLM
- GPT
- apprentissage supervisé, non supervisé, par renforcement

# :x Risks

Dans le débat public, on a l'impression qu'il existe 2 types de risque liés à l'IA: Des risques sociétaux et environnementaux à court terme, et des risques de guerre à long terme, qui peuvent ressembler à des scénarios de Science-fiction.

En réalité, les risques sont bien plus divers et certains risques actuels sont déjà très préoccupants.
On peut classer ces risques en 3 grandes familles: la [: mauvaise utilisation](#Misuse), les [: risques systémiques](#Systemic) et les risques de [: dysfonctionnement](#Malfunction)

La plupart des risques évoqués ici sont tirés de [ce document](https://www.securite-ia.fr/panorama#Classification-des-risques-li-s-l-IA) du centre français pour la sécurité de l'IA (CeSIA).

## :x Misuse

Les IA peuvent être utilisés par des individus ou des organisations malveillantes, souvent dans des buts illégaux.

Un exemple actuel est celui des cyber-arnaques. Depuis que chatGPT est apparu, elles sont de plus en plus nombreuses et surtout de plus en plus réalistes.

Certains risques sont à plus haute échelle: l'IA sert de plus en plus à générer des deepfakes et autres contenus trompeurs pour la manipulation de masse et ainsi influer sur les elections.

À l'avenir, l'IA pourra également être utilisée pour fabriquer des drones tueurs, pour faciliter les attaques cybercriminelles et pour designer des armes biologiques.

## :x Systemic

Même lorsque aucun acteur n'a de but spécialement malveillant, l'IA peut tout de même avoir des impacts très négatifs. L'IA est utilisée là où elle n'a pas été anticipée.

Les exemples les plus évidents sont les systèmes de recommandation des réseaux sociaux et l'utilisation de chatGPT chez les élèves.

Mais ce ne sont pas les seuls. Un type de modèle actuel déjà très répandu, le LLM (type chatGPT), modifie la manière dont on recherche l'information et raisonne.
- L'utilisation par les jeunes enfants impact le développement de leur cerveau.
- Beaucoup de contenu sur internet est écrit partiellement ou entièrement par ces IA, donc de plus en plus le style et l'idéologie du contenu s'uniformise
- Les biais (racisme, sexisme) sont reproduits et même amplifiés par les IA

Et bien sûr, toutes les conséquences sur l'environnement entrent dans cette catégorie. (TODO: impact écologique du datacenter de musk)

## :x Malfunction

Et si l'IA est utilisée par des acteurs bien intentionnés, qui ont réfléchi à l'impact sur la société au préalable ?

Malheuresement, cela ne suffit pas. Car l'IA peut ne pas se comporter comme on l'avait imaginé.

Même après des années de recherche, il y a encore des accidents de voitures autonomes qu'on arrive pas à expliquer. Et pourtant, les IA des voitures autonomes sont probablement les plus fiables qui existent à l'heure actuelle.

Plus les IA sont complexes et apprennent longtemp, sur des grosses quantités de données, plus ils est difficile de prévoir leur comportement. Les incidents où les IA se comportent de manière inattendue se multiplient. (TODO: faire un article sur l'exemple de Bing Chat ou autre)


Ce type de risque peut paraitre mineur par rapport aux deux autres, mais c'est peut être le risque principal. Les IA ne se *programment pas*, elles apprennent. Cela rend les risques de dysfonctionnement bien plus importants, et toute tentative de contrôle plus difficile.
C'est tout l'enjeu de rendre les IA fiables, que l'on explore dans la suite.


# :x Control

Imaginez: on vous donne la mission de surveiller un programme informatique pour l'empécher de faire certaines actions dangereuses. Vous acceptez.
Ce programme informatique est utilisé par de nombreux utilisateurs (potentiellement malveillants), il est capable d'apprendre cetains sujets plus vite que vous, il communique avec tout internet, il peut être dupliqué facilement, et il change de forme tous les 5 ans.

C'est l'état actuel du problème avec les IA.

Selon le niveau auquel on se place, on observe des difficultés différentes:
- lors de la [: creation](#Creation) du modèle
- lors de son [: deploiement](#Deploy)
- au niveau de la [:legislation](#Legislation)

## :x Creation

Il faut savoir qu'à l'heure actuelle, l'entrainement d'une IA type chatGPT dure plusieurs mois, fait tourner des millions de cartes graphiques en continu et s'entraine sur une bonne proportion d'internet.

La taille et la complexité de ces IA font qu'elles sont en grande partie inexplicables. On parle de *boite noire*.

Il y a différents enjeux dans la recherche actuelle pour mieux controler les IA:
- mieux comprendre les IA pour identifier ce qu'elle est susceptible de faire ou pas dans différents scénarios (*explicabilité*)
- prouver mathématiquement certaines propriétés des IA
- avoir des moyens fiables de spécifier des objectifs à l'IA, lui faire apprendre ces règles et surtout lui faire respecter (*alignement*)

Ce dernier point, le problème de l'alignement, est central dans le domaine. Nous y reviendrons.


## :x Deploy

Lorsque le modèle est déployé, il peut échapper aux contrôle de ceux qui l'ont créé pour plusieurs raisons:
- il peut être utilisé dans des scénarios qu'on avait pas imaginé
- des attaquants peuvent modifier le comportement du modèle par de nombreuses techniques (TODO: resource)

Il est également possible que l'IA se comporte très différemment en phase de test et en phase de déploiement.

Il est également probable que l'IA intergisse avec d'autres IA créées par d'autres acteurs. Et controler les interactions entre différents types d'IA est encore plus compliqué.

## :x Legislation

Une legilsation met des années à se mettre en place, et est très souvent réactive plutôt que préventive.

En comparaison, les modèles d'IA peuvent changer du tout au tout en quelques années.


## :x Information

TODO

# :x Trust

TODO:
- IA fiable = IA de confiance
- définition de la confiance à base de contrats
- confiance intrinseque / extrinseque
- montrer les difficultés fondamentales:
  - asymétrie d'information
  - explicabilité


# :x Alignment

TODO:
- prérequis:
  - bonne cybersécurité
- definition alignement

# :x Capabilities

TODO:
- ce qui est le plus inquietant, ce n'est pas l'état actuel mais la tendance
- Top labs et leurs déclarations
- déclarations des experts

# :x Collapse

TODO:
- scénarios principaux à moyen terme:
  - ARA (https://www.alignmentforum.org/posts/vERGLBpDE8m5mpT6t/autonomous-replication-and-adaptation-an-attempt-at-a)
  - effondrement des démocraties et totalitarisme via IA
  - armes biologiques
- on peut réduire ces risques par le risk-management: évaluer les capacités des IA pour faire des trucs dangereux et interdire leur commercialisation si trop dangereux.
  - note: il y aurait qd même de l'utilisation illégale, mais plus difficile à se procurer ces modèles
- dans les risques précédents, provient de la mauvaise utilisation. Mais le jour où l'IA est assez puissante (économiquement + intelligence) pour qu'elle fasse tout pour ne pas être débranchée n'est pas si loin.

# :x Economy

TODO:
- 3 acteurs dans le problème de l'IA fiable: IA, utilisateur et entreprise
  - plus difficile que d'aligner IA et utilisateur
  - devient un pb economique
- projet stargate

# :x Politics

TODO:
- démocratie numérique
- US / Chine, espoirs d'un traité
- pourrait nécessiter des traités politiques aussi forts que pour les armes biologiques ou nuléaires (https://hyperarme.com/)


# :x Actions

TODO:
- CeSIA
- Tournesol
- pauseIA
(mériterait un article à part entière)
