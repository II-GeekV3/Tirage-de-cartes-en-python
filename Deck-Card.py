import random
import pygame
from enum import Enum

#class Card:
 #   def __init__(self, value, Type): 
  #      self.value = value
   #     self.Type = Type 

#Type = ['heart', 'diamond', 'spades', 'clud']  # Type = Coeur, Carreau, Treffle, Pique.

#Deck = [Card(value, Type) for value in range(1, 14) for Type in Type ]

class Carte:
    def __init__(self, value, forme):
        self.valeur = value
        self.forme = forme
    def Nom_Carte(self):
        return self.valeur+" de "+self.forme

class Cartes:
    def __init__(self):
        valeurs =["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "K", "1"]
        formes =["Pique", "Coeur", "Carreau", "Trèfle"]

        self.cartes=[]
        for forme in formes:
            for value in valeurs: 
                self.cartes.append(Carte(value, forme))

    #Mélanger : le jeu de cartes
    def mélanger(self):
        random.shuffle(self.cartes) 

    def Afficher(self):
        for card in self.cartes:
            print(card.Nom_Carte())

    def Tirer(self):
        indice= random.randint(0,len(self.cartes)-1)
        ma_carte=self.cartes[indice]
        del(self.cartes[indice])
        return ma_carte
jeu_carte=Cartes()
input("On mélange les cartes")

jeu_carte.mélanger()
input("On affiche les cartes mélangé")

jeu_carte.Afficher()

input("On tire les cartes une à une")
for i in range(52):
    carte_tirée=jeu_carte.Tirer()
    input("carte tirée est "+carte_tirée.Nom_Carte())