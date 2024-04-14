Nous pouvons prendre en compte certains principes en écrivant notre code :

# Principe n°1 : la découvrabilité
La découvrabilité désigne la facilité ou la difficulté à trouver l’emplacement de fonctionnalités précises. La découvrabilité peut aussi faire référence à la difficulté de compréhension du code lui-même : est-ce que l’on comprend clairement ce que fait le code, simplement en le regardant ? Ou faut-il aller chercher ailleurs pour comprendre ?

Nous pouvons garantir une bonne découvrabilité en découpant notre code de façon logique, avec des fichiers et des dossiers qui assurent que les sections de code ayant des fonctionnalités similaires soit regroupées.

# Principe n°2 : la simplicité
On peut également garantir que chaque section de code ait aussi peu de responsabilités que possible – de préférence une seule ! Les fonctions et méthodes qui ne font qu’une seule chose sont plus faciles à comprendre et à tester. 

# Principe n°3 : le style
Un code bien structuré a un style cohérent. Pour un projet professionnel ou open source, vous aurez un guide de style. Suivez-le pour garantir que votre code et celui de vos collègues et collaborateurs soient similaires.

Les outils les plus utiles pour structurer du code sont simplement les fichiers et les dossiers. Le découpage de nos programmes en fichiers et dossiers (bien nommés) aide à la découvrabilité.

De façon générale, il convient de placer chaque classe dans un fichier distinct, et de donner un nom logique ou similaire entre le module et la classe qu’il contient. Si cela n’est pas possible ou pas souhaitable, on peut placer un groupe de classes liées logiquement dans le même fichier, avec un nom approprié.

Il est également important de nommer de façon logique les classes, fonctions/méthodes et variables.

n module, c’est simplement le code exécutable et les définitions de classe/fonction contenus dans un fichier Python unique, alors qu’un paquet (ou package) est une collection de modules regroupés logiquement dans un répertoire et partageant un fichier de configuration (__init__.py).

Cet  __init__.py  peut contenir n’importe quel code d’initialisation, et contient parfois une définition__all__, qui définit tous les modules du paquet, comme ceci :

__all__ = ["contact", "textcontact", "owlcontact"]

En plaçant ainsi les modules dans un paquet, nous obtenons des déclarations import plus logiques – ce qui est particulièrement utile si vous fournissez votre code comme bibliothèque à quelqu’un d’autre.

Voici un schéma courant dans les programmes Python :

if __name__ == "__main__":
    do_something()
    print("Hello, World")

__name__  est une variable automatiquement assignée à chaque module. Par défaut, elle contient le nom du module.

Vous pouvez voir que l’on teste l’égalité entre la variable  __name__  et le nom  __main__.

Le fichier principal de votre code (celui que vous utilisez pour lancer le programme) verra automatiquement son nom changé en __main__  !

Cette condition permet donc d'exécuter du code seulement si le fichier courant est le point d’entrée de l’application. Le code ne s'exécutera donc pas si ce fichier a été importé depuis un autre module.

Il est particulièrement important de noter que vous avez très peu de contrôle sur l’ordre du code dans les différents paquets importés : ne vous reposez dessus que pour l’import de paquets et la configuration, et rien d’autre !

En résumé
Un fichier Python, contenant du code Python, est appelé un module.
Un paquet est un répertoire de modules Python contenant un fichier__init__.py.
Nous pouvons utiliser des déclarations import pour inclure des classes et des fonctions d’autres modules et paquets Python.

## Comment décomposer un problème de programmation

# Les fonctionnalités
Que doit faire votre programme ou fonctionnalité ? De quelles fonctionnalités additionnelles pourrait-on avoir besoin à l’avenir ? Comment vous assurer que votre code soit extensible, de façon à ce que ces modifications soient possibles ?

# Les objets
Quels sont les objets qui existent dans l’espace du programme ? Quelles sont les responsabilités de chacun de ces objets ? À quoi servent-ils ? Quelles sont les relations entre ces objets ?

Nous avons parlé d’héritage pendant ce cours, lorsqu’une classe « is-a » (« est-une ») version plus spécialisée d’une autre classe. Il existe également des relations de composition, que nous avons évoquées sans les nommer, qui désignent des relations « has-a » (« a-un »). Par exemple, une voiture a un volant – le volant pourrait être stocké comme variable à l’intérieur de la voiture. C’est une façon d’imbriquer les objets entre eux, pour éviter d’avoir un seul gros objet qui ferait trop de choses différentes.

# Les interfaces
Dans quelle mesure est-ce que ce code va interagir avec d’autres systèmes et d’autres parties de code ? À quoi ressembleront les interfaces – les méthodes, fonctions et autres fonctionnalités qui relient votre programme aux autres ?

## Les exceptions

Une exception est un message du programme qui signale que quelque chose s’est mal passé.

Les exceptions sont déclenchées – ou levées, ou lancées – par un programme. Les exceptions que vous avez pu voir précédemment – comme  NameError,  ZeroDivisionError, ou  IndexError  – sont toutes des exceptions intégrées qui sont lancées par les éléments internes de Python lui-même.

Toutes les exceptions Python sont des objets, ce qui mérite d’être souligné.Exception est la classe de base des exceptions Python, dont tout hérite. Cela signifie que nous pouvons créer nos propres exceptions – ce que nous couvrirons après une note rapide sur la…

# Gestion des exceptions

Lorsqu’une exception est déclenchée dans notre code – et qu’elle n’est pas gérée – habituellement, notre programme s’arrête.

Nous pouvons gérer une exception en utilisant untry-except (souvent appelé une instruction try-catch dans d’autres langages).

def increase_percent(initial_value, after_value):
    try:
        return (after_value / initial_value) * 100
    except ZeroDivisionError:
        return 0
    except Exception as error:
        print("Uh oh, unexpected error occurred!")
        raise error

Lorsqu’une exception est levée, elle se propage dans le programme. Python ne fait plus les choses dans l’ordre, mais lance plutôt continuellement l’exception en remontant la pile – c’est-à-dire la pile de fonctions/méthodes qui ont appelé d’autres fonctions/méthodes. L’exception va continuer à remonter jusqu’à ce qu’elle soit gérée ou qu’elle n’ait plus nulle part où aller. Dans ce dernier cas, le programme plante.