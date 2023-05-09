import math
import time

while True:

    print("           I \                                       ")
    print("           I   \                                     ")
    print("       3   I     \   1                               ")
    print("           I       \                                 ")
    print("           I_________\                               ")
    print("               2                                     ")

    print("De quel côté veux-tu calculer ?")
    print("1 - hypoténuse")
    print("2 - côté adjacent")
    print("3 - Côté opposé")

    RES = int(input('Saisissez l option souhaitée: '))

    if RES == 1:

        X1 = float(input('Côté opposé: '))
        X2 = float(input('côté adjacent: '))

        P0 = math.sqrt( X2 ** 2 + X1 ** 2)

        print("....................................................")

        print("O valor da hypoténuse é: {}".format(P0))
        time.sleep(5)

    elif RES == 2:

        X1: float = float(input('Côté opposé: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur de l'hypoténuse est: {}".format(P0))
        time.sleep(5)

    elif RES == 3:

        X1: float = float(input('Côté adjacent: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur de l'hypoténuse est: {}".format(P0))
        time.sleep(5)
        
    else:
        print('réponse invalide voulez-vous réessayer')
        print("1 - Oui")
        print("2 - No")

        Souo = int(input(" "))

        if Souo == 1:
                continue

        elif Souo == 2:
                break
                time.sleep(2)
        else:
                print("option invalide!")
                print("Est seulement possible de répondre avec un numéro")
                time.sleep(4)
