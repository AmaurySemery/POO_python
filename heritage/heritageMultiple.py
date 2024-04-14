"""
L’héritage multiple suppose qu’une classe ait de multiples classes parents. 
Dans une hiérarchie d’héritage, il y a plusieurs niveaux d’héritage – une classe a un parent qui a un parent.

L’héritage multiple a mauvaise réputation en programmation orientée objet – les systèmes qui utilisent l’héritage multiple peuvent être difficiles à comprendre. 
De plus, certains langages de programmation proposent des implémentations médiocres d’héritages multiples qui provoquent des problèmes.
"""

class Cat:
    """Un chat."""

    def meow(self):
        """Miaule."""
        print("Meow!")


class Talker:
    """Interface qui définit la méthode "say" (dire)."""
     
    def say(self, to_say):
        """Affiche "to_say" (à dire)."""
        print(to_say)


class TalkingCat(Cat, Talker):
    """Un chat qui parle ??"""
    pass


salem = TalkingCat()
salem.meow()
salem.say("Hello!")

"""
Chaque langage qui utilise l’héritage multiple a sa propre solution – celle de Python s’appelle le MRO, pour Method Resolution Order : l’ordre de résolution de méthode.

Expliqué simplement, le MRO d’une classe constitue l’ordre des emplacements où Python va chercher une définition de méthode. 

De façon générale, néanmoins, Python cherchera dans la classe parent la plus à gauche en premier. 
Donc, dans notre exemple  TalkingCat  ci-dessus, Python cherchera d’abord dans Cat, puis dans Talker.
"""