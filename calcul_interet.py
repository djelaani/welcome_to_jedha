#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gain():
    
    try:
        som_a_placer = float(input("quelle somme voulez-vous placer ? "))
        if som_a_placer < 0:
            print("entrer un montant positif")
        nombre_annee = int(input("combien d'annee souhaitez-vous placez votre argent ? "))
        if nombre_annee < 0:
            print("le nombre d'annee doit etre un entier positif ")
        taux = float(input("quel est le taux d'interet ? "))
        if taux < 0 :
            print("le taux d'interet doit etre un reel positif")

        if som_a_placer < 0 or nombre_annee < 0 or taux < 0 :
            raise ValueError()
        else :
            total_revenu = som_a_placer*(1+taux/100)**nombre_annee
            return print("Vous allez recevoir {:.2f} euros".format(total_revenu))
        
    except: ValueError as erreur:
            print("La valeur inseree n'est pas valide")

gain()


# In[ ]:




