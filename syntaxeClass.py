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

class Rectangle:
    width = 3
    height = 2

    def calculate_area(self):
        return self.width * self.height