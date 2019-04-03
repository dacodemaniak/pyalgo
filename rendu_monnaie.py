"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input() function to get a user entry
"""

# Defines some vars
nbBillet100 = 0
nbBillet50 = 0
nbBillet10 = 0
nbPiece = 0
leftCoins = 0

# Accept an amount entry
customerSomme = input("Somme en entrée : ")
somme = int(customerSomme)

# Got 100
nbBillet100 = somme // 100
left100 = somme % 100

if left100 > 0:
    # Next... got 50
    nbBillet50 = left100 // 50
    left50 = left100 % 50


    if left50 > 0: 
        # Next... got 10
        nbBillet10 = left50 // 10
        left10 = left50 % 10
        

        if (left10 > 0):
            nbCoins = left10 // 2
            leftCoins = left10 % 2

# This is the end friends
print("And the result is...\n", nbBillet100, " x 100\n", nbBillet50, " x 50\n", nbBillet10, " x 10\n", nbCoins, " x 2\n", leftCoins, " x units")

