"""
 Enfin, les attributs statiques sont des attributs qui n’ont pratiquement aucun lien avec la classe. 
 Seules les méthodes peuvent être statiques, et l’ajout par rapport aux attributs de classe est minime : on n'a plus besoin de spécifier le paramètre  cls. 
 Pour créer un attribut statique, il suffit de faire précéder la méthode par  @staticmethod :
"""

class Bird:
    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )

print(Bird.get_definition())

# Les attributs statiques sont à l'opposé du paradigme orienté objet, ils sont donc à éviter