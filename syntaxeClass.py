"""
Les noms de classe, par convention, commencent par une majuscule. 
S’il y a plusieurs mots dans le nom d’une classe, on utilise généralement le CapitalizedCase, en mettant une majuscule à la première lettre de chaque mot.

Un « scope » en Python est défini par le niveau d’indentation. 
Vous avez déjà écrit des conditions   if  et utilisé les indentations pour montrer où le code doit se résoudre – c’est la même chose avec les classes.

Note : en programmation orientée objet, il existe trois types d’attributs :
* les attributs d’instance (propres aux instances créées),
* les attributs de classe (propres à la classe, et partagés entre les instances),
* et les attributs statiques (qui sont presque indépendants de la classe).

Si chaque type d’attribut possède une utilité propre, essayez autant que possible de privilégier les attributs d’instance, qui permettent d’utiliser la programmation orientée objet à son plein potentiel.

Note sur le paramètre self : le nom « self » n’est qu’une convention : on pourrait très bien le renommer en « instance_actuelle », ou « this », ou encore « toto ». 
Votre code fonctionnerait aussi bien. 
C’est cependant une convention très forte en Python, donc prenez-la au mot. 🙏
"""

# class Rectangle:
#     width = 3
#     height = 2

#     def calculate_area(self):
#         return self.width * self.height

"""
Il existe une catégorie spéciale de méthode nommée constructeur. 
Chaque classe en a un, et il est utilisé pour créer des objets à partir de cette classe. 
En Python, notre constructeur est une méthode magique nommée  __init__, que l’on peut utiliser un peu comme ceci :
"""

class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
        print("Pour ce rectangle, la taille est " + str(length) + ", la largeur est " + str(width) + " et la couleur est " + str(color))

class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print("Le gâteau est coupé en 4 parts !")

# De cette manière, grâce au constructeur __init__, nous déclarons des variables dynamiques

# Instancions maintenant un objet :
rectangle = Rectangle(5, 3)

"""
Il est important que les paramètres que vous fournissez correspondent aux paramètres du constructeur. 
Ceci inclut les positions des paramètres – dans notre constructeur ci-dessus, la « longueur » (length) est le premier paramètre donné, et la « largeur » (width) est le deuxième paramètre donné.
"""