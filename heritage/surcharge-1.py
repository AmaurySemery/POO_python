"""
Bien que la surcharge nous permette de modifier entièrement des comportements hérités, il peut parfois être utile d’avoir accès au code des méthodes des classes parents, depuis les classes enfants.

L’un des emplacements les plus courants pour cette utilisation se trouve dans les constructeurs. 
Pour cela, nous utilisonssuper()– comme ceci :
"""

class Drink:
    """Une boisson."""

    def __init__(self, price):
        """Initialise un prix."""
        self.price = price

    def drink(self):
        """Boire la boisson."""
        print("Je ne sais pas ce que c'est, mais je le bois.")


class Coffee(Drink):
    """Café."""
    
    prices = {"simple": 1, "serré": 1, "allongé": 1.5}

    def __init__(self, type):
        """Initialise le type du café."""
        self.type = type
        super().__init__(price=self.prices.get(type, 1))


    def drink(self):
        """Boire le café."""
        print("Un bon café pour me réveiller !")

"""
L’approche avec  super()  vous permet de réutiliser le code plutôt que de le copier, et assure le regroupement des fonctionnalités de façon logique – soit deux des plus grands avantages de la programmation orientée objet !
"""

"""
Une classe enfant peut fournir sa propre implémentation d’un élément hérité de sa classe parent.
L’implémentation de la classe enfant est prioritaire sur celle du parent – elle surcharge l’implémentation de la classe parent.
On peut utiliser la méthode super pour accéder à des méthodes dans la classe parent que nous avons surchargée.
Une classe abstraite est une classe qui ne peut pas être instanciée – à la place, il faut en hériter.
"""