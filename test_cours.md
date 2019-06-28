## Natural Language Processing


## Ce que vous apprendrez dans ce cours

Ce cours est une introduction à l’analyse statistique des textes et du langage. C’est une discipline qui a récemment connu d’énorme progrès scientifique grâce aux développement du deep learning et de la capacité exponentielle des ordinateurs à traiter les calculs qu’on leur demande. Nous commencerons ici par des principes d’analyse élémentaires.


## Natural language processing

Le Natural Language Processing, souvent abrégé par le sigle NLP et traduit en français par traitement automatique du langage naturel, est une discipline au croisement des sciences informatiques et des data science qui consiste à étudier comment interagissent les langages informatiques et celui des humains (langage naturel).



1. Exemples d’applications

Le NLP a connu un très fort essor depuis ses balbutiements dans les années 1950, et aujourd’hui, grâce à l’amélioration rapide des capacités des ordinateurs tant en termes de mémoire, de stockage et de vitesse de calcul et à l’avènement du deep learning, le nombre et la diversité des champs d’application du NLP ne cesse de grandir. Faisons une liste fortement non-exhaustive de quelques applications populaires :



*   Correction orthographique, recherche de mots clés, recherche de synonymes
*   Extraction d’information depuis des sites internets (par exemple, le prix d’un produit, des dates, des noms de personnes, d’entreprises etc…)
*   Classification :
    *   Classer des textes par niveau de difficulté
    *   Classer par sujet traité
    *   Classer en fonction du sentiment général d’un texte (positif/négatif)
*   Traduction automatisée
*   Système commandé par la parole
*   Capacité pour l’ordinateur de répondre à des questions complexes
2. Pourquoi le langage constitue un type de données très particulier ?

La plupart des données sur lesquelles travaillent d’ordinaires les data scientists sont des métriques mesurées dans le monde, comme des cours d’action, des mesures météorologiques, du signal que l’on souhaite transcrire en son. Toutes ces données sur lesquelles nous travaillons, nous espérons leur donner un sens pour en faire quelque chose d’utile, comme aider notre prise de décision quant à l’achat d’une maison, ou d’une action, prédire quel temps il fera demain, si un client serait plutôt une jeune mère ou un homme du troisième âge.

Le langage a cette particularité d’être un système spécifiquement développé par les humains pour véhiculer de l’information et du sens. Le problème n’est plus de donner un sens à des données qui prises hors contexte n’en on pas, il s’agit maintenant pour les data-scientists d’aider la machine à comprendre le sens ou les sens qui existent déjà au sein du langage qu’utilisent les humains. Le système symbolique qu’est le langage humain peut être communiqué de différentes façons, il peut être écrit, exprimé sous forme de sons, de gestes, ce qui entraîne un nouveau niveau de complexité et de richesse pour cette discipline.

Si les données étudiées dans le cadre du Natural Language Processing sont par nature très particulières, elles amènent avec un elle un certains nombre de difficultés elles aussi très particulières.



*   L’expression du langage passe par de nombreux canaux de communications à la fois, lors d’une conversation, par exemple, le langage est exprimé à la fois par les mots, l'intonation et les modulations de la voix, les mouvements du corps qui accompagnent le discours, le regard etc…
*   Le langage est un mode d’expression ambigu. Un même mot, une même phrase ou texte peuvent avoir des interprétations complètement différents, des générations de chercheurs continue de s’intéresser à des oeuvres, des citations, voie même des mots tant la richesse d’interprétation du langage est profonde et dense.
*   L’interprétation du langage dépend d’un contexte situationnel, du monde réel environnant, du sens commun et de normes culturelles et sociales

Toutes ces particularités du langage en font un sujet infiniment intéressant pour les data-scientists qui, malgré les difficultés présentées par ce dernier, ont fait et continue à faire d’immense progrès dans cette discipline.



3. Représentation du langage pour la machine

Afin d’analyser du texte avec python, il est nécessaire de travailler le format des données afin qu’elles puissent facilement être comprises, comptées, analysées par l’ordinateur. Nous allons maintenant présenter rapidement différentes techniques de traitement du texte de manière à ce qu’il puisse être utilisé pour du machine leanring :



*   Lower case (lettres minuscules) :

    Python, comme beaucoup d’autres langages informatiques, fait la distinction entre les majuscules et les minuscules “A”, n’est ainsi pas le même caractère que “a”. Par extension les mots “Apprendre” et “apprendre”, bien que compris de la même manière par nos cerveaux humains ne représentent pas les mêmes chaînes de caractère dans un langage comme python. On va donc généralement remplacer tous les caractères d’un texte par leur équivalent en minuscule avant de commencer des traitements plus avancés.

*   Retirer la ponctuation :

    Il est rare d’analyser la ponctuation en texte mining, on va donc généralement retirer toute la ponctuation afin de n’avoir plus que des mots à analyser.

*   Stop words :

    Les stop words sont tous les mots de liaison, les articles et quantificateurs très utilisés dans une langue mais qui ne sont pas en eux mêmes porteurs de sens, en français il s’agit de : “au” “car” “la” “le” etc… En anglais il s’agit par exemple de : “a” “and” “any” etc…


    On les retire en général car ils sont tellement fréquent dans les textes qu’ils empêchent de manière général les différents modèles qu’on peut utiliser de voir les mots qui caractérisent vraiment un texte.

*   Mots communs :

    Pour certaines analyses, comme lorsque l’on souhaite analyser un vocabulaire très spécifique d’un texte, on va parfois retirer certains mots très communs dans un texte en particulier ou une famille de texte. Si on cherche à classer par thèmes des textes qui décrivent l’italie, on va sans doute retirer de tous ces texte le vocabulaire trop communs afin de pouvoir mettre en valeur les différences entre ces différents textes.

*   Mots rares :

    De la même manière, des mots trop peu fréquents dans des textes peuvent s’avérer inutiles car leur liaison avec d’autres mots dans le texte pourraient s’apparenter à du bruit, on les retire aussi dans certains cas.

*   Correction des fautes de frappes :

    Dans un but d’unifier l’orthographe des mots employés dans les textes que l’on souhaite analyser, on fera souvent appel à des packages python afin de corriger les fautes de frappes et ainsi ramener à l’identiques des mots qui ne l’étaient pas à cause de leur orthographe erroné.

*   Stemming (Racinisation)

    De nombreux mots dans différentes langues sont des variations autour d’une racine commune, le processus de racinisation permet de se débarrasser d’éventuels préfixes et suffixes afin de conserver uniquement les racines communes des mots et ainsi pouvoir faire des analyses jusqu’alors impossibles.

*   Lemmisation

    La lemmisation est un procédé proche de la racinisation mais qui, au lieu de supprimer simplement les suffixes et préfixes courants, possède une connaissance suffisante du vocabulaire d’une langue afin de transformer les mots en leur racine et ainsi ne pas dénaturer le vocabulaire comme peut le faire le stemming. Par exemple, le stemming transformera “president” en “sid” alors que la lemmisation transformera “predident” en “presid”.

    1. N-grams

Souvent on ne représentera pas un texte de manière brut lorsqu’on se lance dans du text mining, ainsi on ne laissera pas l’ordinateur se débrouilla avec une chaîne de caractère de la forme :

“Le chat mange les poissons”

Au lieu de cela on va la plupart du temps représenter le texte sous forme de N-grams. Les N-grams sont une manière de décomposer le texte par groupes de ```N``` mots. Par exemple : les 1-grams ou unigrams du texte précédent sont les suivants :


<table>
  <tr>
   <td>“le”
   </td>
   <td>“chat”
   </td>
   <td>“mange”
   </td>
   <td>“les”
   </td>
   <td>“poissons”
   </td>
  </tr>
</table>


Les 2-grams de ce même texte sont :


<table>
  <tr>
   <td>“le chat”
   </td>
   <td>“chat mange”
   </td>
   <td>“mange les”
   </td>
   <td>“les poissons”
   </td>
  </tr>
</table>


Les N-grams sont des outils très pratiques pour analyser le thème général d’un texte, extraire les mots les plus importants, lier les textes entre eux, les classer.



    2. Parse trees

Les parse trees sont des outils qui permettent de décomposer des phrases simples de manière automatiques comme dans l’exemple suivant :


![](https://drive.google.com/uc?export=view&id=15yqMknQsiaqnubxCQjN4AwnlmcDWRQh1)


En anglais, par exemple, des règles grammaticales existent qui permettent de construire des phrases, par exemple une phrase peut être composée d’un groupe nominal (Noun phrase NP) suivie d’un groupe verbal (Verb phrase). On peut faire la liste de ces règles et il existe une librairie sur python (nltk) qui permet grâce à des algorithme de décomposition d’analyser des phrases simples. C’est grâce à cette technologie que les assistants personnels comme Siri (apple), Alexa (amazon) ou Cortana (microsoft) sont capables de comprendre rapidement des instructions vocales après les avoir converties en texte.

Cependant, lorsque les phrases deviennent trop complexes, ce type d’analyse ne permet d’extraire le sens de manière intelligible pour l’ordinateur, elle est plus adaptée à la compréhension du sens d’instructions courtes, précises et factuelles.



4. Analyses simples

Avant de passer à des méthodes de machine learning avancées pour la compréhension du langage, nous allons commencer par introduire des techniques très fréquemment utilisées en linguistique et en marketing quantitatifs pour extraire de l’information de données textuelles.



    1. Term frequency

La term frequency ou fréquence d’un terme et le ratio du nombre d’occurrences du terme sur le nombre de mots dans la phrase ou le texte. Par exemple dans la phrase suivante : “le chat noir mange les poissons mais ne mange pas les autres chats noirs” la table des fréquences peut s’écrire de la manière suivantes après traitement de lemmisation et suppression des stop words :


<table>
  <tr>
   <td>Term
   </td>
   <td>Occurrences
   </td>
   <td>Term Frequency
   </td>
  </tr>
  <tr>
   <td>“chat”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“noir”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“mange”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“poisson”
   </td>
   <td>1
   </td>
   <td>0.125
   </td>
  </tr>
  <tr>
   <td>“autre”
   </td>
   <td>1
   </td>
   <td>0.125
   </td>
  </tr>
  <tr>
   <td><strong>Total</strong>
   </td>
   <td><strong>8</strong>
   </td>
   <td><strong>1</strong>
   </td>
  </tr>
</table>




    2. Inverse document frequency

L’idée sous-jacente si on pense à un ensemble de documents textuels que l’on souhaite classer, on conclut qu’un terme qui apparaît dans tous les documents du corpus (ou groupe de textes) n’est pas très utile pour différencier ou rapprocher entre eux les documents. La formule général de l’inverse term frequency ou IDF est la suivante :




![](https://drive.google.com/uc?export=view&id=1s5juVZzMugTAE3gcbk-PkpiGG-1eMzUO)



Où ```N``` est le nombre total de documents et ```n``` est le nombre de documents dans lequel le terme apparaît. Par exemple si l’on considère les deux documents suivants : “le chat noir mange les poissons mais ne mange pas les autres chats noirs” et “la girafe mange des feuilles grâce à son long cou, mais ne mange pas de poissons”. Si on calcule l’IDF sur ces exemples on obtient le tableau suivant :


<table>
  <tr>
   <td>Term
   </td>
   <td>Document occurences
   </td>
   <td>Document frequency
   </td>
   <td>IDF
   </td>
  </tr>
  <tr>
   <td>"chat"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>“noir”
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>“mange”
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0</p>

   </td>
  </tr>
  <tr>
   <td>“poisson”
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0</p>

   </td>
  </tr>
  <tr>
   <td>“autre”
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>"giraffe"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>"feuille"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>"long"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
  <tr>
   <td>"cou"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td>LOG(2)
   </td>
  </tr>
</table>


Plus l’IDF d’un mot est élevé, plus le mot est unique et donc représentatif d’une caractéristique particulière du document dans lequel il se trouve par rapport aux autres documents.



    3. Term frequency - Inverse document frequency

La Term frequency - inverse document frequency est la multiplication de TF et IDF, c’est un indicateur très populaire de l’importance d’un mot dans un document relativement à sa présence dans les autres documents. Par exemple si un mot est très fréquent dans un texte mais présent dans tous les autres textes, alors son importance sera moins grande qu’un terme très fréquent dans un seul document et absent des autres. Pour les exemples cités, les tf-idf s’écrivent ainsi.


<table>
  <tr>
   <td>Document
   </td>
   <td>Term
   </td>
   <td>TF
   </td>
   <td>IDF
   </td>
   <td>TF IDF
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>"chat"
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1505149978</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“noir”
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1505149978</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“mange”
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.07525749892</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“poisson”
   </td>
   <td><p style="text-align: right">
0.125</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.03762874946</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“autre”
   </td>
   <td><p style="text-align: right">
0.125</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.07525749892</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"giraffe"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"mange"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.06020599913</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"feuille"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"long"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"cou"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
</table>


Ainsi on comprend que les mots les plus importants du document 1 qui le démarquent des autres documents du corpus sont “chat” et “noir”, dans les document 2 les mots “giraffe” “feuille” “long” et “cou” sont les termes les plus caractéristiques. Inversement les mots “mange” et “poisson” ont un tf-idf faible dans les deux documents. On peut donc conclure que les deux document parlent du fait de manger du poisson, mais que le document 1 se concentre sur les chats, alors que le document 2 porte sur les giraffes.



    4. Sentiment analysis

Il existe des librairies dans python comme textblob qui contiennent des listes de vocabulaire où chaque mot possède un score associé au sentiment qu’il véhicule, si ce sentiment est plutôt positif, le score sera positif, par contre si le sentiment véhiculé par le mot est négatif alors le score sera lui aussi négatif.
