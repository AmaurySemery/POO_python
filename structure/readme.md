us pouvons prendre en compte certains principes en écrivant notre code :

Principe n°1 : la découvrabilité
La découvrabilité désigne la facilité ou la difficulté à trouver l’emplacement de fonctionnalités précises. La découvrabilité peut aussi faire référence à la difficulté de compréhension du code lui-même : est-ce que l’on comprend clairement ce que fait le code, simplement en le regardant ? Ou faut-il aller chercher ailleurs pour comprendre ?

Nous pouvons garantir une bonne découvrabilité en découpant notre code de façon logique, avec des fichiers et des dossiers qui assurent que les sections de code ayant des fonctionnalités similaires soit regroupées.

Principe n°2 : la simplicité
On peut également garantir que chaque section de code ait aussi peu de responsabilités que possible – de préférence une seule ! Les fonctions et méthodes qui ne font qu’une seule chose sont plus faciles à comprendre et à tester. 

Principe n°3 : le style
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