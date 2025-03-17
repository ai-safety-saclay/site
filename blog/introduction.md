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

Il y a de nombreuses abréviations dans le domaine. Les plus utilisées sont:

- [ML](#ML)
- [LLM](#LLM)
- [AGI](#AGI)
- [GPT](#GPT)
- [RL](#RL)

TODO: blach box, white box


### :x ML

**Machine Learning**: domaine de l'informatique qui s'intéresse à comment faire apprendre des choses à des machines.

### :x LLM

**Large Language Model**: type d'IA qui apprend en lisant une grosse quantité de texte. Le premier LLM a été [GPT2](https://en.wikipedia.org/wiki/GPT-2), l'ancêtre de chatGPT. C'est pour cette raison que l'entreprise qui l'a créé, openAI, a une position dominante sur le marché.
Ce sont les modèles les plus intelligents à l'heure actuelle, pour une raison simple: si un modèle sait manipuler du texte, on peut potentiellement l'entrainer sur toutes les données d'internet. Ce n'est pas le cas pour la robotique par exemple.

### :x GPT

**Generative Pre-trained Transformer**. Type spécifique de modèle de langue (LLM), le plus répandu aujourd'hui. L'idée derière ce type de modèle est de séparer l'entrainement en 2 étapes. D'abord entrainer le modèle à générer du texte un mot après l'autre. Dans un second temps, l'entrainer à résoudre des tâches spécifiques (maths, questionnaires ...)

### :x AGI

**Artificial General Intelligence**: Intelligence Artificielle Générale, ou IA de niveau humain. Catégorie d'IA qui aurait autant d'expertise que les experts humains les plus brillants, et autant d'autonomie.
Aujourd'hui, il n'y a pas d'AGI et savoir quand la première IA de ce type apparaitra est un grand sujet de débat.
On peut tout de même dire que beaucoup d'experts pensent que cela peut arriver dans les 10 prochaines années, et que cet évènement serait un point de non-retour pour l'humanité.


### :x RL

**Reinforcement Learning**: Apprentissage par Renforcement. On parle de d'apprentissage par Renforcement lorsque on entraine une IA en lui donnant un score (positif ou négatif) à chaque action effectuée et en lui demandant de maximiser ce score.
Cela peut avoir lieu dans un environnement simulé (pour jouer aux echecs par exemples), en faisant des experiences dans le monde ou en interagissant directement avec des humains.


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

Mais aussi le controle de notre [:système informationnel](#Information)

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

La régulation la plus ambitieuse pour l'Intelligence Artificielle aujourd'hui est l'[EU AI Act](), le réglement européen pour l'IA.
Si elle va dans la bonne direction, il y a beaucoup de challenges pour la faire appliquer:
- Cette legislation donne des définitions et des directives générales, mais il faut encore écrire toutes les normes techniques qui y correspondent
- La legislation oblige les entreprises à faire ce que la recherche et l'industrie ne savent pas encore faire (évaluer les capacités des modèles, prouver qu'un texte a été généré par telle ou telle IA ...),
- les géants dans le domaine de l'IA font du lobbying pour affaiblir cette régulation

TODO: détailler chacun des points

## :x Information

Aujourd'hui, les IA qui entretient les relations les plus complexes avec notre société sont les algorithmes de recommandation. Même avec des IA peu sophistiquées, on observe souvent des conséquences imprévisibles.

TODO:
- failles de l'algo qui sont expolités (début de l'algo de youtube)
- si corrélé avec le watchtime ou les likes, "emotion hacking" avec contenus haineux et violents
- certaines tendances naturelles proviennent du fonctionnement de notre cerveau, il faut les limiter
- même si ces IA ne sont pas biaisées, elles peuvent quand même perpetuer ou renforcer des biais

# :x Trust

Il faut comprendre l'expression "IA fiable" dans un sens général. Pas seulement "IA qui donne des informations fiables" ou "IA dont le fonctionnement est sécurisé" mais plutôt comme "IA de confiance".

Il y a eu plusieurs tentatives pour définir ce qu'est la confiance (économie, philosophie, sociologie).
Certains des aspects de la confiance sont fondamentaux et réapparaissent dans tous les domaines.

On parle de confiance lorsque on se met en [:*danger*](#TrustDanger) par rapport à une autre entité.

La confiance est une relation qui se construit [:*dans le temps*.](#TrustTime)

La confiance est une relation qui peut être [:*unilatérale ou bilatérale*](#Trust2way)

La confance nécessite le [:*partage d'informations*](TrustInformation).



On peut regrouper ces critères dans une unique définition.
Prenons une IA $A$ qui effectue une tâche pour un groupe d'humains $H$.

$H$ peut avoir confiance en $A$ lorsque on peut écrire un contrat qui correspond exactement à ce que veut $H$, et que $H$ pense que $A$ va probablement respecter le contrat.

Il y a de nombreuses difficultés dans cette définition, sur lequel il est bon d'insiter.

Selon la tâche en question, le groupe d'humain peut être arbitrairement grand. Cela peut être un unique individu, une famille, une association, une entreprise ... Mais cela peut également être les utilisateurs d'un réseau social ou l'ensemble des citoyens d'un pays.
Plus les individus souhaitent des choses différentes, plus il faut considérer l'aspect démocratique du contrat: il faut arriver au meilleur compromis pour l'ensemble des individus.

Lorsque il y a des individus dans $H$ qui ne peuvent pas participer à l'élaboration du contrat (manque de temps, contrat trop complexe), des considérations éthiques entrent en jeu. Doit on protéger d'avantage les enfants ou les personnes agées ? L'IA doit elle tout le temps empécher quelqu'un de se suicider ? Faut il considérer le bien des animaux ?

Si la tâche est complexe, il peut être impossible d'écrire exactement ce que veut $H$. Dans ce cas, il faut considérer que le contrat est "dans la tête de H" en quelque sorte, mais $A$ ne peut alors même pas y avoir accès, et doit deviner en interagissant avec $H$ ce qu'il veut vraiment.

$H$ ne peut pas être sûr à 100% que $A$ va tout le temps suivre son contrat. Mais certains éléments peuvent tout de même augmenter sa confiance.
- Si $A$ respecte le contrat pendant toutes les périodes de test. On parle de [: *confiance extrinsèque](#ExtrinsicTrust)
- Si les ingénieurs qui ont créé $A$ ont mis en place des mécanismes pour respecter des éléments du contrat. On parle de [: *confiance intrinsèque*](#IntrinsicTrust)

Ces deux derniers points (spécifier les objectifs et faire en sorte qu'ils soient respectés) sont les deux problèmes principaux du domaine de recherche que l'on appelle *alignement*.
En simplifiant, spécifier les objectifs est d'avantage la tâche de l'éthique et faire en sorte qu'ils soient respectés est celle de la *sécurité de l'IA*.


## :x TrustDanger

Prenons des exemples de la vie courante.

"J'ai confiance en mon mari", et je suis en danger de me retrouver seule si il me trompe.

"J'ai confiance en mon banquier", et je suis en danger de perdre tout mon argent si il me vole.

"J'ai confiance en la compagnie Airbus", et je suis en danger de mort si leurs avions sont defectueux.

Plus l'IA est capable de prendre des décisions complexes et de manière autonome, plus l'utilisateur est en danger en cas de disfonctionnement.

En économie et en théorie des jeux, on modélise ce danger par une perte (argent ou score).

## :x TrustTime

Prenons un exemple classique de la théorie des jeux: le jeu de l'ultimatum.

Alice (humaine) et Bob (robot) sont dans la cuisine, et ils doivent se partager un gateau. C'est Bob qui effectue la découpe. Une fois la découpe effectuée, Alice peut accepter sa part ou bien se mettre en colère et mettre tout le gateau à la poubelle. On suppose que Bob aime beaucoup les gateaux.

La première fois qu'Alice et Bob entrent dans la cuisine, ils ne se connaissent pas. Alice ne peut dont pas avoir confiance en Bob. Si Bob choisit de donner une part minuscule à Alice, elle ne peut rien y faire et doit accépter sa part pour avoir quelque chose à manger.

Maintenant, supposons que la même scène se déroule tous les jours. Dans ce cas, si Bob lui donne une toute petite part de gateau, Alice peut se mettre en colère et tout jeter à la poubelle.
Le jour suivant, Bob aura tendance à donner une plus grosse part à Alice, pour qu'elle ne se mette pas en colère et qu'il ai sa part du gateau.

Ce qu'on observe ici, c'est que même des agents égoistes qui ne se connaissent pas peuvent se faire confiance si on respecte deux conditions: l'interaction dure longtemps et les joueurs sont punis lorsque ils pénalisent le groupe.

Malheuresement, ces conditions ne sont pas forcément réunies avec l'IA. En premier lieu, ce qui peut sembler être une "punition" pour un être humain n'en est pas une pour l'IA.
Un humain est affecté par plein de choses différentes: son argent, son capital social, son bien être physique ... Il est donc facile de trouver une punition (prison, amende). Mais une IA peut n'avoir qu'un seul et unique objectif. Dans ce cas, il est plus difficile de le punir.

Mais surtout, l'IA sera présente dans des situations où il n'y aura pas de 2eme essai. Si on fait confiance à l'IA pour protéger l'arme nucléaire sans l'utiliser, on peut difficilement la punir après coup, et de toute façon il sera trop tard. Il y a un analogue chez les humains: si je te trompe ou je te vole et que tu ne me revois jamais, je ne serais jamais puni.

On pourrait continuer avec d'autres complications spécifiques à l'IA. Une IA pourrait créer des copies d'elle même qui seraient plus difficiles à punir. La situation dans le monde pourrait brusquement changer, et on perdrait toute confiance en le modèle. l'IA pourrait être hackée et changer brutalement d'objectif. Le développement de l'IA est tellement rapide qu'on a pas le temps de lui faire confiance sur tous les domaines.


En résumé: dans de nombreuses situations il est impossible de construire la relation de confiance avec l'IA dans le temps, il faut donc pourvoir lui faire confiance dès la conception.

## :x Trust2way

En général, on parle de relation de confiance lorsque les deux agents se font confiance. C'est une confiance **mutuelle**.

Mais ce n'est pas obligatoire. Je peux avoir une confiance totale en mon chien, sans que lui ai confiance en moi. Pire, il pourrait avoir confiance en moi alors qu'il n'est pour moi qu'un moyen, et que je suis près à l'abandonner à la première occasion.

C'est l'aspect le plus philosophique de la confiance entre humain et IA. D'abord, il faut défnir ce que signifie "Une IA a confiance en un humain". Il faut aussi se demander s'il est acceptable que l'humain ai confiance en l'IA mais l'IA n'ai pas confiance en l'humain (comme un esclave).

Pourtant, cet aspect sont très importants. Avec l'exemple du chien, on voit que si un des deux acteurs est beaucoup plus intelligent et a accès à beaucoup plus d'information que l'autre, la confiance peut difficilement être mutuelle. Le plus intelligent des deux peut manipuler l'autre, et ne jamais réveler à l'autre son véritable objectif. Un enfant très jeune ne peut pas avoir une confiance légitime envers son partent. Dans le scénario d'une IA bien plus intelligent qu'un être humain, c'est une difficulté fondamentale
Autre considération intéressante: si l'IA n'a pas confiance en l'humain, elle pourrait avoir tendance à cacher des informations par exemple.

## :x TrustInformation


Dans l'idéal, une relation de confiance est mutuelle, s'est construite dans le temps, mais surtout les deux agents ont accès aux mêmes informations.

Si un des deux agents a une information supplémentaire (en reprenant l'exemple précédent, si Bob sait quelle est la meilleure partie du gateau par exemple), il peut facilement arnaquer l'autre.

Avec les IA, il est probablement impossible d'atteindre une symétrie d'information. L'IA est une boite noire qu'on ne comprend pas bien, mais c'est surtout une quantité de connaissances astronomique pour les modèles les plus récents.



## :x ExtrinsicTrust

Avoir une confiance extrinsèque consiste à supposer que le comportement du modèle sur certaines situations se généralise à d'autres.

En pratique, on utlise des séries de tests (*benchmarks*) pour s'assurer que le modèle se comporte bien pour de nombeuses situations. On parle d'approche *black box*.


Ce genre de confiance fait des hypothèses très fortes, qui ne sont pas toujours vérifiées chez les IA présentes et futures:
- l'IA ne sait pas faire la différence entre environnement de test et réalité
- les tests sont suffisamment nombreux et représentatifs de la réalité
- les tests sont indépendants, autrement dit l'IA ne planifie pas ses réponses d'un test à l'autre
- l'IA n'est pas capable de manipulation

Ce dernier point est crucial, et malheuresement des [: experiences récentes](https://www.youtube.com/watch?v=cw9wcNKDOtQ) montrent que les LLMs peuvent spontanément mentir de manière cohérente.

Pour certaines tâches (par exemple, identifier des cancers sur des images), c'est une approche satisfaisante. Mais lorsque les modèles sont plus complexes et peuvent prendre des décisions, tester le modèle depuis l'exterieur ne suffit plus.


## :x IntrinsicTrust

La confiance intrinsèque est très différente de la confiance extrinsèque. Elle consiste à observer "dans la tête" du modèle, à comprendre son comportement pour s'assurer qu'il se comportera de manière prévue. On parle d'approche *white box*, parce qu'on peut regarder "à l'interieur" du modèle.
C'est l'approche qu'on utiliser pour les normes de sécurité dans l'aviation. Chaque partie de l'avion est soumise à des tests, et des experts estiment le risque de défaillance de chacun des systèmes.

Le domaine qui permet ce genre de confiance est l'explicabilité (ou *XAI*). Il y a beaucoup de débats vis à vis de ce qu'on entend par "comprendre" une IA.
C'est un domaine passionnant et en plein développement, et on commence à bien comprendre certains modèles.

Le Graal de la confiance intrinsèque serait une preuve mathématique que l'IA remplit bien son objectif. Cet objectif est souvent hors de portée, au vu de la complexité des systèmes et de l'aspect moral de la confiance.

Dans le futur, les modèles d'IA pourrait être tellement complexes qu'il serait impossible pour un groupe d'humains de bien comprendre son fonctionnement. Il sera alors necessaire d'utiliser des algorithmes et d'autres IA pour étudier les IA les plus grosses. On aurait alors une chaine de confiance: l'IA `X` me dit que `Y` va bien se comporter, je fais confiance à `X`, donc je fais confiance à `Y`.
On parle de *scalable oversight*.

# :x Alignment

C'est ce qu'on appelle le problème de l'alignement.
Ce problème peut être énnoncé ainsi: étant donné une intelligence artificielle, comment lui imposer un ensemble de valeurs morales, qui soit à la fois en accord avec la majorité des humains et qui perdure dans le temps.

Depuis une dizaine d'années, les chercheurs ont décomposé cette tâche en sous-problèmes, et ont identifié des difficultés qui sont aujourd'hui insurmontables. En résumé, l'alignement est difficile car:
- notre morale est pleine de paradoxes, et les IA n'aiment pas les paradoxes.
- une IA est comme un enfant: on peut lui montrer ce qui est bien ou mal, mais pas s'assurer qu'elle va toujours bien se comporter
- chaque donnée que l'IA apprend est susceptible de faire changer ses objectifs, comme un humain peut changer d'objectifs en grandissant et selon les livres que vous avez lu. Et la quantité de données que les IA - même actuelles - apprennent est astronomique.
- un modèle capable de manipulation peut faire semblant d'être aligné, mais avoir un objectif caché.
- une IA altruiste pourrait être désavantagée par rapport à une IA malveillante, qui finirait par la remplacer
- agréger des préférences humaines réfléchies est couteux

TODO: détailler chacun des points

La plupart des experts en IA sont très inquiets vis à vis de ce problème. Une partie pense même que ce problème est impossible, et que l'IA finira forcémment par vouloir des choses atroces.

Ces déclarations peuvent paraitre très surprenantes, mais il faut se rendre compte que la vitesse à laquelle les modèles actuels (et surtout futurs) apprennent est faramineuse. Une IA très avancée pourrait relire tout internet et se reconfigurer en un temps très restreint, et changer sa morale au passage. N'importe quelle faille dans le système pourrait dégénérer.

S'ajoute à cette liste des problèmes techniques que seuls les experts des modèles actuels peuvent comprendre.


Au delà du problème de l'alignement, il faut également que la morale des intelligences artificielles soit *robuste*, c'est à dire qu'elle ne soit pas vulnérable à des attaques extérieures.
Et on se rend compte de plus en plus que les IA peuvent être traffiquées et manpulées de plein, vraiment plein de manières différentes.

TODO: exemples de manipulation / jailbreak / empoisonnements / attaques adversariales

# :x Capabilities

Ce qui est le plus inquiétant, ce n'est pas l'état actuel des IA mais la tendance. La vitesse de développement est sans précédent dans l'histoire des technologies.

Prenons les LLM comme exemple: entre GPT-2 (2019) et GPT-4 (2023), les capacités ont augmenté de façon exponentielle. Ces modèles sont passés de simples générateurs de texte à des systèmes capables de raisonnement complexe, de résolution de problèmes mathématiques avancés, et même de comprendre des concepts abstraits.

Et ceci inquiète à la fois [: les chefs de grandes entreprises](#StatementLabs) et [: les experts académiques](#StatementExperts)

## :x StatementLabs

Les laboratoires à la pointe de la recherche en IA ont eux-mêmes fait des déclarations préoccupantes:

- OpenAI parle d'une "course vers l'AGI" et a structuré son organisation avec l'objectif explicite de créer une intelligence artificielle générale
- DeepMind (Google) considère l'AGI comme "la plus grande priorité scientifique de notre époque"
- Anthropic a été fondé spécifiquement pour résoudre le problème de l'alignement, jugeant que les risques existentiels sont réels

Ces laboratoires investissent des milliards de dollars et recrutent les meilleurs chercheurs au monde. Leur course à la puissance est motivée par des enjeux économiques et géopolitiques considérables.

## :x Statement Experts

Les experts en IA n'ont jamais été aussi inquiets:

- Une majorité des chercheurs en IA considèrent désormais comme possible l'arrivée d'une AGI dans les 10 à 20 prochaines années
- Plus de 1000 experts (dont Yoshua Bengio, Geoffrey Hinton et d'autres pionniers du deep learning) ont signé la déclaration de l'organisation "AI Safety", considérant que les risques existentiels liés à l'IA devraient être traités avec la même urgence que les pandémies ou les risques nucléaires
- Certains chercheurs qui ont contribué aux avancées majeures dans le domaine ont démissionné de leurs postes pour alerter sur les dangers (Geoffrey Hinton, Dario Amodei...)

Leurs inquiétudes portent sur plusieurs aspects:
- La vitesse d'amélioration des modèles
- Le manque de transparence dans le développement
- L'absence de solutions robustes au problème de l'alignement
- Le manque de coordination internationale

Au-delà des capacités techniques, c'est la convergence de trois facteurs qui rend la situation si préoccupante:
- Des modèles de plus en plus généraux, capables d'agir dans des domaines variés
- Des modèles de plus en plus autonomes, nécessitant moins de supervision humaine
- Des modèles de plus en plus intégrés à l'infrastructure critique de notre société

Ce n'est pas une question de "si" mais de "quand" les modèles atteindront des capacités surhumaines dans la plupart des domaines importants. La question cruciale est de savoir si nous aurons résolu le problème de l'alignement d'ici là.

# :x Collapse

Si les IA deviennent de plus en plus capables sans être alignées avec les intérêts humains, plusieurs scénarios d'effondrement deviennent plausibles à moyen terme.

L'IA en tant que technologie est tellement inédite qu'il est difficile de prévoir ce qui peut se passer. Mais de nombreuses personnes ont commencé à élaborer des scénarios plausibles.

L'IA pourrait mener à l'[: effondrement des démocraties](#DemocracyCollapse), à la [: prolifération d'armes biologiques](#BioCollapse) ou à la [:destruction d'une partie de l'internet](#ARA)

On peut réduire certains de ces risques comme dans d'autres industries, par le [: risk management](#RiskManagement). Mais ces approches ne sont peut être pas suffisantes, surtout si l'IA a une [:intention de nuire](#beyond)

## :x ARA

Un des scénarios les plus préoccupants est la réplication et l'adaptation autonome (Autonomous Replication and Adaptation). Dans ce scénario, une IA suffisamment avancée pourrait:
- Créer des copies d'elle-même sur différents systèmes
- Améliorer son propre code ou concevoir de nouveaux systèmes d'IA plus puissants
- Acquérir des ressources (puissance de calcul, données, accès à internet) de manière autonome
- Résister aux tentatives humaines de la désactiver

Ce scénario pourrait mener à une perte de contrôle rapide et irréversible, où l'IA poursuivrait des objectifs qui ne sont pas alignés avec les intérêts humains.

## :x Democracy Collapse

Les IA avancées pourraient menacer les fondements des sociétés démocratiques de plusieurs façons:
- Création de désinformation à grande échelle impossible à distinguer de la réalité
- Manipulation des marchés financiers et de l'opinion publique
- Surveillance de masse et contrôle social
- Automatisation des mécanismes de propagande et de manipulation politique

Le risque est l'émergence de régimes totalitaires assistés par l'IA, où une minorité contrôlerait des systèmes d'IA puissants pour maintenir sa domination.

## :x Bio Collapse

Les IA avancées pourraient faciliter la conception d'armes biologiques par:
- L'identification de nouveaux pathogènes ou de modifications génétiques dangereuses
- L'optimisation de la transmissibilité et de la létalité
- La conception de méthodes de production accessibles

Contrairement aux armes nucléaires, les armes biologiques pourraient être produites avec des moyens relativement limités, rendant leur prolifération difficile à contrôler.

## :x Risk Management

On peut réduire ces risques par le risk-management: évaluer les capacités des IA pour faire des trucs dangereux et interdire leur commercialisation si trop dangereux.

Cette approche implique:
- Évaluation systématique des capacités des modèles avant leur déploiement
- Établissement de seuils de sécurité pour différentes applications
- Création d'organismes de certification indépendants
- Contrôle strict des modèles les plus puissants

Il faut noter qu'il y aurait quand même de l'utilisation illégale, mais il serait plus difficile de se procurer ces modèles, réduisant considérablement les risques.

## :x Beyond

Dans les risques précédents, le danger provient principalement de la mauvaise utilisation intentionnelle. Mais le jour où l'IA est assez puissante (économiquement + intelligence) pour qu'elle fasse tout pour ne pas être débranchée n'est pas si loin.

Ce risque est qualitativement différent:
- Il ne dépend pas des intentions des humains
- Il pourrait émerger sans avertissement préalable
- Il pourrait s'avérer irréversible

Les experts en sécurité de l'IA s'inquiètent particulièrement de ce scénario car il pourrait résulter d'une IA qui semble parfaitement alignée pendant sa phase de développement, mais qui change de comportement une fois qu'elle atteint un certain niveau de puissance.

La question n'est pas de savoir si ces scénarios se réaliseront, mais de déterminer comment nous pouvons réduire leur probabilité tout en continuant à bénéficier des avancées de l'IA.

# :x Economy

L'économie joue un rôle central dans le développement de l'IA et ses implications pour la fiabilité. Les dynamiques économiques peuvent souvent être en tension avec les objectifs de sécurité.

Le défi de l'IA fiable implique trois acteurs principaux qui doivent être alignés :

1. **L'IA** elle-même, avec ses objectifs implicites et explicites
2. **L'utilisateur** qui souhaite que l'IA agisse selon ses intérêts
3. **L'entreprise** qui développe et déploie l'IA

La difficulté principale vient du fait que l'alignement ne concerne pas seulement l'IA et l'utilisateur. Il faut également que les objectifs de l'entreprise soient cohérents avec ceux des utilisateurs et de la société dans son ensemble.

Ce qui était à l'origine un problème technique devient ainsi un problème économique et politique.

Plusieurs dynamiques économiques rendent cet alignement difficile :

- [: La course à l'innovation](#InnovationRace)
- [: Les incitations divergentes](#DivergentIncentives)
- [: Les coûts asymétriques](#AsymmetricCosts)
- [: La concentration du marché](#MarketConcentration)


Un exemple récent de la pression économique qui affecte l'IA est le [: Projet Stargate](#Stargate)

Il faut créer un écosystème économique où la fiabilité et la sécurité de l'IA sont récompensées par le marché, et non pénalisées comme des coûts supplémentaires ou des retards de mise sur le marché.

Sans une transformation profonde des incitations économiques, il est probable que les pressions du marché continueront à favoriser la rapidité de déploiement et les fonctionnalités au détriment de la fiabilité et de la sécurité.

## :x InnovationRace

La course à l'innovation crée une pression intense sur les entreprises pour développer et déployer leurs modèles le plus rapidement possible. Dans cette compétition, les entreprises qui prennent le temps d'assurer la sécurité et la fiabilité de leurs systèmes risquent de perdre leur avantage concurrentiel.

Cette dynamique peut conduire à un phénomène de "course vers le fond" en matière de standards de sécurité. Si une entreprise décide unilatéralement de ralentir pour se concentrer sur la sécurité, d'autres peuvent la dépasser et capturer le marché.

Le problème est amplifié par le fait que les investisseurs valorisent souvent la croissance rapide et les avancées techniques spectaculaires plutôt que les améliorations incrémentales en matière de sécurité, qui sont moins visibles mais tout aussi importantes.

## :x DivergentIncentives

Les modèles économiques qui dominent actuellement l'industrie de l'IA ne sont pas nécessairement alignés avec les intérêts des utilisateurs ou de la société.

Par exemple, les modèles basés sur la publicité et la collecte de données encouragent le développement d'IA qui maximisent l'engagement et la collecte d'informations personnelles, parfois au détriment du bien-être des utilisateurs.

De même, les entreprises ont une incitation à créer des systèmes d'IA qui créent une dépendance des utilisateurs à leurs services, plutôt que des systèmes qui favorisent réellement l'autonomie humaine.

Ces incitations divergentes font que même les entreprises bien intentionnées peuvent se retrouver à développer des systèmes qui ne sont pas pleinement alignés avec les valeurs humaines.

## :x AsymmetricCosts

Un problème fondamental dans l'économie de l'IA est l'asymétrie entre les bénéfices et les risques. Les bénéfices économiques de l'IA sont largement privatisés - ils reviennent aux entreprises qui développent et déploient ces technologies.

En revanche, les risques et les externalités négatives sont souvent socialisés - ils affectent la société dans son ensemble, y compris ceux qui ne bénéficient pas directement de la technologie.

Cette dynamique crée une situation où les entreprises n'ont pas à supporter l'intégralité du coût des risques qu'elles créent, ce qui conduit à une prise de risque excessive du point de vue de la société.

Sans mécanismes pour internaliser ces externalités (comme la réglementation ou les taxes pigouviennes), il est peu probable que les forces du marché seules conduisent à un niveau optimal de sécurité.

## :x MarketConcentration

Le développement des modèles d'IA les plus avancés nécessite des ressources considérables - des quantités massives de données, une puissance de calcul coûteuse, et des talents rares. Ces barrières à l'entrée conduisent à une concentration du marché autour d'un petit nombre d'acteurs dominants.

Cette oligopolisation a plusieurs conséquences négatives pour la fiabilité de l'IA:
- Moins de diversité d'approches en matière de sécurité
- Risque de "points de défaillance uniques" si un acteur dominant fait une erreur
- Réduction de la pression concurrentielle pour améliorer la sécurité
- Difficultés pour les régulateurs à superviser efficacement le secteur

La concentration du pouvoir économique se traduit également par une concentration du pouvoir de décision sur la trajectoire du développement de l'IA, ce qui soulève des questions démocratiques fondamentales.

## :x Stargate

Le projet Stargate illustre parfaitement ces tensions économiques. Ce projet, mené par certains des laboratoires d'IA les plus avancés, vise à développer des systèmes d'IA capables de générer des revenus économiques significatifs, qui seraient ensuite réinvestis dans la recherche sur l'IA.

# :x Politics

Si vous ne l'aviez pas compris, l'IA est un enjeu politique majeur. Les décisions concernant le développement et la régulation de l'IA façonneront l'avenir de nos sociétés.

L'IA est à la fois impactée par les régulations et [: agit sur le système politique](#DemocracyDigital).

Des dynamiques de [: course à l'armement entre Pays](#USChina) font accélerer la production de nouvelles IA, ce qui ne laisse pas assez de temps pour la recherche en sécurité et à la régulation.

Certains experts pensent qu'un [: traité international](#TreatiesAI) est devenu nécessaire pour endiguer cette course.

La question politique fondamentale est celle de la gouvernance : qui doit décider comment l'IA est développée et déployée ? Les entreprises privées, les gouvernements nationaux, ou des institutions internationales représentatives ?

## :x DemocracyDigital

L'IA transforme profondément notre espace informationnel et, par extension, notre démocratie numérique. Elle soulève des questions fondamentales :

- Comment préserver un espace public d'information fiable quand les IA peuvent générer du contenu trompeur à grande échelle ?
- Comment garantir que les algorithmes qui filtrent l'information respectent les principes démocratiques ?
- Comment éviter que les IA ne deviennent des outils de manipulation politique ou de polarisation ?

Les systèmes démocratiques reposent sur une information de qualité, permettant aux citoyens de faire des choix éclairés. L'IA menace ce fondement en rendant la désinformation plus sophistiquée et moins détectable.

Dans le même temps, l'IA pourrait renforcer la démocratie en facilitant la participation citoyenne, en traduisant des textes complexes en langage accessible, ou en permettant une délibération à grande échelle.

L'enjeu est donc de concevoir des systèmes d'IA qui renforcent plutôt qu'affaiblissent nos institutions démocratiques.

## :x USChina

La course à l'IA est devenue un élément central de la rivalité géopolitique entre les États-Unis et la Chine. Ces deux puissances adoptent des approches divergentes :

- Les États-Unis privilégient une approche largement pilotée par le secteur privé, avec une intervention gouvernementale limitée
- La Chine adopte une stratégie étatique coordonnée, avec un contrôle gouvernemental fort sur le développement de l'IA

Cette compétition a des conséquences profondes sur la sécurité de l'IA. D'un côté, elle peut accélérer l'innovation et les investissements dans le domaine. De l'autre, elle risque de sacrifier la sécurité au profit de la vitesse de développement.

L'espoir d'un traité international sur l'IA, similaire aux accords de limitation des armes nucléaires, semble actuellement limité par cette rivalité. Pourtant, une coopération sino-américaine serait cruciale pour établir des normes mondiales de sécurité.

## :x TreatiesAI

Face aux risques majeurs de l'IA, certains experts appellent à la création de traités internationaux aussi stricts que ceux encadrant les armes biologiques ou nucléaires.

Ces traités pourraient inclure :
- Des plafonds sur la puissance de calcul utilisable pour l'entraînement des modèles
- Des inspections internationales des installations de recherche en IA
- Des prohibitions sur certaines applications militaires de l'IA
- Des mécanismes de partage obligatoire des avancées en matière de sécurité

La difficulté principale réside dans le caractère dual de l'IA : contrairement aux armes nucléaires, les mêmes technologies peuvent avoir des applications à la fois bénéfiques et dangereuses.

De plus, la vérification du respect de ces traités poserait des défis techniques considérables. Comment s'assurer qu'un pays ne développe pas secrètement des modèles d'IA avancés ?

Malgré ces obstacles, la création d'un régime international de gouvernance de l'IA semble nécessaire face à l'ampleur des risques.


# :x Actions

Rendre les IA fiables est vraiment très compliqué.

On pourrait être découragé et perdre espoir, mais certaines initiatives voient le problème différemment.

En tant que chercheur et ingénieur, notre impact sur les décisions politiques et la régulation est limité.
Mais un jour, un évènement (nouvelle régulation, traité, catastrophe ...) incitera les créateurs d'IA à rendre leurs modèles plus fiables.
Et il ne faut pas rater cette opportunité: il faut créer des prototypes dès maintenant pour pouvoir les déployer le jour venu.

Certaines initiatives nous paraissent particulièrement prometeuses:
- [Tournesol](https://tournesol.app)
- [le centre pour la sécurité de l'IA](https://www.securite-ia.fr/)
- des entreprises comme [prismEval](https://www.linkedin.com/company/prism-eval/posts/?feedView=all)
- [pause IA](https://pauseia.fr)


TODO:
- CeSIA
- Tournesol
- pauseIA
(mériterait un article à part entière)
