class Film:
    def __init__(self, name):
        self.name= name
    
    def watch(self):
        print("Bon visionnage !")

class FilmCassette(Film):
    """Un film en cassette !"""

    def __init__(self, name):
        """Initialise le nom et la bande magnetique."""
        self.name = name
        self.magnetic_tape = True
    
    def rewind(self):
        """Rembobine le film."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

film = Film("2001: l'odyssée de l'espace")
film_cassette = FilmCassette("Blade Runner")

print(film_cassette.name)
film_cassette.watch()
film_cassette.rewind()

"""
L’héritage multiple est à utiliser avec précaution – pour la plupart des problèmes, il existe généralement des designs plus simples et plus faciles.

Si vous ne spécifiez pas de classe parent, vous dites en fait à Python de faire de la classe une sous-classe d’Object.  
Object  constitue la base de toutes les classes, ce qui peut prêter à confusion.
Vous vous souvenez que toutes les classes possèdent un constructeur sans argument par défaut ? 
C’est parce qu’elles héritent d’Object.
"""

"""
On définit une classe enfant en utilisant  class Enfant(Parent).
Par défaut, toutes les classes héritent d’Objet – un objet Python qui fournit une fonctionnalité basique.
Les classes peuvent hériter de classes parents multiples simultanément – dans le cas de l’héritage multiple.
"""