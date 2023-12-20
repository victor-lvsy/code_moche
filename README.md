# Le code BARRE!
## Présenté par Victor LEVESY du BDMtS (Bureau du Mec tout Seul)

Afin d'avoir une experience sympathique sur ce code, il est nécéssaire d'adopter quelques bonnes pratiques.

Ce code est un code de génération d'images aléatoires à partir d'un embedding de texte maison. (Ne pouvant pas utiliser ma clé d'API OpenAI, j'ai fait avec les moyens du bord)

Le fichier principal est le fichier moche.py, j'ai laissé son nom intact pour que vous regards encore embrumés par la soirée d'hier puissent le trouver.

Pour le lancer rien de plus simple, après avoir installé l'environnement virtuel avec:
```
pipenv install
```
On peut lancer le code avec:
```
pipenv run python moche.py
```

Le premier texte de génération d'image est localisé dans le fichier en code barre avec l'extention .txt.
À vous de le modifier à votre guise pour faire d'autres oeuvres d'art (moderne...), la seule condition est d'avoir un texte de longueur supérieure à 1200 charactères en entrée. Ayant commencé mon code le 20 décembre à 18h, je n'ai pas eu vraiment le temps d'implémenter du padding.

Dans un second temps, copiez le contenu du fichier 'EN_DERNIER.txt' dans le fichier en code barre avec l'extention .txt (en ayant bien évidemment retiré le contenu de ce dernier au préalable) pour obtenir l'ultime surprise de ce code!

En espérant vous avoir fait passer un agréable moment, 
### Victor

PS. Pour les plus curieux d'entres vous, je suis disposé à expliquer le fonctionnement du code à l'aide des fichiers qui ont servi au développement, notamment le fichier de génération du JSON qui contient les "embeddings".