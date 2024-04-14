"""
Les attributs d’instance sont des variables définies à l’aide de self. 
Elles sont relatives à l’instance, et ne peuvent être accédées sans instanciation. 
Dans le cadre des méthodes, ce sont les méthodes classiques d'une classe, qui possèdent  self  en premier paramètre.
"""

class Bird:
    """Un oiseau. 🐦"""

    def __init__(self):
        """Les attributs définis ici sont des attributs d'instance."""
        self.wings = 2

    def fly(self):
        """Cette méthode est une méthode d'instance."""
        print("Je vole !")

 

bird = Bird()  # obligation d'instancier un oiseau pour utiliser ses attributs
bird.wings
bird.fly()

# Les attributs d'instance permettent d'utiliser la programmation orientée objet à son plein potentiel