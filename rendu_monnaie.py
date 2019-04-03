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
customerSomme = input("Insérez votre billet : ")
somme = int(customerSomme)
# Got 100
nbBillet100 = somme / 100
left100 = somme % 100

# Just KISS (Keep It Simple and Stupid)
print ("Il y a ", nbBillet100, " billets de 100 et il reste ", left100)

