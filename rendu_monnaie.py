"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input() function to get a user entry
"""

# Accept an amount entry
customerSomme = input("Somme en entrée : ")
somme = int(customerSomme)

# Got 100
nbBillet100 = somme // 100
left100 = somme % 100

if left100 > 0:
    # Keep It Simple and Stupid
    print ("Billets de 100 : ", nbBillet100, " Reste : ", left100)
    # Next... got 50
    nbBillet50 = left100 // 50
    left50 = left100 % 50


    if left50 > 0: 
        # Keep It Simple and Stupid
        print ("Billets de 50 : ", nbBillet50, " Reste : ", left50)
        # Next... got 10
        nbBillet10 = left50 // 10
        left10 = left50 % 10
        

        if (left10 > 0):
            # KISS
            print ("Billets de 10 : ", nbBillet10, " Reste : ", left10)
            nbCoins = left10 // 2
            leftCoins = left10 % 2

            if (nbCoins > 0):
                print("et donc... ", nbCoins, " pièces de 2 euros. \nIl reste : ", leftCoins)
            else: 
                print("Il reste : ", leftCoins)
else:
    print("Vous m'avez donné ", nbBillet100, " merci...")

