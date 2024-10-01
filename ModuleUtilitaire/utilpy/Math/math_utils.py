import math

# Module contenant des fonctions utilitaires liées aux math :
#    manipulation de nombres
#    nombres premiers
#    autres propriétés des nombres

# Le module contient ses propres tests sous forme d'assertions
# Si le message final s'affiche, c'est que tous les tests ont réussi.
# Si un message d'erreur s'affiche, cliquez sur le lien pour voir quel test échoue.

def bertha(a: float, b: float, c: float) -> (float, float):
    """
    Fonction pour résoudre un polynôme de degré 2 (quadratique) et trouver les zéros.
    Selon alloprof:
        On appelle zéro, ou abscisse à l'origine d'une fonction f, une valeur de x pour laquelle f(x)=0.
        Une fonction peut avoir plusieurs zéros.

    Cette fonction lance une exception si on ne fournit pas une équation quadratique ou
    si la fonction n'a pas de zéro.

    :param a: Le a dans l'équation ax2 + bx + c = 0 (forme générale)
    :param b:
    :param c:
    :return: un tuple contenant les 2 valeurs si deux zéros, ou la même valeur 2 fois s'il y a un seul zéro
    """
    b2m4ac = b ** 2 - 4 * a * c

    if a == 0:
        raise ValueError("a ne peut pas être nul sinon ca ne serait pas une équation quadratique mais plutot linéaire")
    elif b2m4ac < 0:
        raise ValueError("La fonction n'a pas de zéro")

    racine1 = (-b + math.sqrt(b2m4ac)) / (2 * a)
    racine2 = (-b - math.sqrt(b2m4ac)) / (2 * a)

    return racine1, racine2


def est_entier(n: str) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False

def est_carré(n: int) -> bool:
    """
    Vérifie si le nombre reçu est un carré parfait.
    Un carré parfait est un nombre dont la racine carrée est un nombre entier.
    """
    if n < 0:
        return False

    racine = math.sqrt(n)
    return racine.is_integer()


def est_premier(n: int) -> bool:
    """
    Test si le nombre fourni est premier en testant tous les diviseurs potentiels
    de 2 jusqu'à la racine carrée du nombre lui-même.
    :param n:
    :return:
    """
    if n == 1: return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def ln(nb: float) -> float:
    """
    Bonbon syntaxique pour logarithme naturel base e,
    puisque le module math n'en fourni pas.
    """
    return math.log(nb)


def sont_proches(x: float, y: float) -> bool:
    """
    Vérifie si 2 nombres sont égaux en ignorant les erreurs potentielles de précision
    dû à la façon dont les nombres réels sont stockés.
    """
    return math.isclose(x, y, abs_tol=0.00001)


def main():
    print("Les tests du module de mathématique sont sur le point d'être exécutés...")
    assert est_entier("123")
    assert not est_entier("allo")
    assert not est_entier("123.45")
    assert not est_entier("123,45")


    assert est_carré(4)
    assert not est_carré(15)
    assert est_premier(2)
    assert not est_premier(2 ** 27 + 3 * 6)
    assert est_premier(23)
    assert not est_premier(100)

    # Affiche tous les nb premier en bas de la valeur x.
    x = 20
    for i in range(1, x):
        if est_premier(i):
            print(i)


    assert ln(math.e) == math.log(math.e, math.e)
    assert ln(123) == math.log(123, math.e)
    assert ln(123) == math.log(123)


    assert (bertha(-4.9, 10, 50) == (-2.332995250031629, 4.373811576562241))
    assert (bertha(1, 3, 2) == (-1, -2))

    # On sait que la fonction -6x2+2x-3 n'a pas de zéro, on veut tester
    # si bertha() lance bel et bien une exception
    try:
        bertha(-6,2,-3)
    except ValueError:
        pass


    print(bertha(1,2,1))

    print("Si ce message s'affiche, c'est que tous les tests ont réussi.")




if __name__ == '__main__':
    main()
