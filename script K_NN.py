# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:38:22 2018

@author: Jérôme
"""


import numpy as np
import pandas as pd



''' Le programme ci-dessous se décompose en deux parties : la définition
des fonctions utilisées par la suite, puis la partie principale qui consiste à effectuer le calcul du test
des k plus proches voisins afin de déterminer le k optimal. On aura au préalable effectuer une segmentation de
la base de données en base entrainement et base test'''




''' définition des fonctions utilisées dans la suite du programme'''

#☻ fonctions de soustraction d'un vecteur sur les lignes d'une matrice

def soustrac_array(vecteur_test, vecteur_moyenne):
    vecteur_test=np.array(vecteur_test)
    
    soustraction=vecteur_moyenne-vecteur_test
    
    return (soustraction)

# fonction de soustraction de deux vecteurs ensemble

def soustrac_vecteur(vecteur_test,dataset_entrainement):
    
    vecteur=np.array(vecteur_test)
    soustrac=dataset_entrainement.sub(vecteur, axis=1)

    return (soustrac)


# mise au carré de chaque élément d'une matrice
        
def mise_au_carre(matrice):
    carre=matrice**2
    
    return (carre)

# calcul de la somme par colonne de chaque élément d'une matrice

def somme_elements(matrice):
    somme=matrice.sum(axis=1)
    
    return (somme)

# calcul de la somme des éléments d'un vecteur

def somme_vecteur(vecteur):
    somme=vecteur.sum()
    return(somme)

# calcul de la distance euclidienne

def distance_euclidienne(matrice):
    dist=np.sqrt(matrice)
    
    return (dist)

# fonction qui récupère les k plus petites distances euclidiennes

def kppv(dist_euclid,k):
    liste_dist=dist_euclid.sort_values()
    kppv=liste_dist[0:k]
        
    return (kppv)

# fonction qui récupère les k plus proches voisins d'un vecteur donné

def recup_lignes_kppv(kppv,dataset):
    
    indices=np.array(kppv.index)
    proches_voisins=[]
    for i in indices:
        if i !=0:
            proches_voisins.append(dataset.loc[i])
    voisins=np.array(proches_voisins)
    voisins=voisins.T
    moyenne=np.mean(voisins,axis=1)
    
    return (moyenne)






''' nettoyage de la base de donnée initiale.Plusieurs colonnes ne présentent aucun intérêt dans l'étude
demandée. '''


df=pd.read_csv("liste_aliments.csv", sep='\t', low_memory=False)


''' description du fichier'''
#df.describe()

'''visualisation des premières et dernières lignes'''

# print(df.head(10))
# print(df.tail(10))




df=df.drop(['url','creator','created_t','created_datetime','last_modified_t','last_modified_datetime','generic_name','packaging','packaging_tags','quantity','brands', 'categories','categories_tags','categories_fr','origins_tags','manufacturing_places_tags','labels_tags','emb_codes','emb_codes_tags','first_packaging_code_geo','cities','cities_tags','purchase_places','stores','countries','countries_tags','countries_fr','allergens','traces','traces_tags','traces_fr','no_nutriments','additives_tags','additives_fr','ingredients_from_palm_oil_n','ingredients_from_palm_oil_tags','ingredients_that_may_be_from_palm_oil_n','ingredients_that_may_be_from_palm_oil_tags'], axis=1)

df=df.drop(['states','states_tags','main_category','main_category_fr','image_url','image_small_url'], axis=1)

df=df.drop(['energy-from-fat_100g','butyric-acid_100g','caproic-acid_100g','caprylic-acid_100g','capric-acid_100g','lauric-acid_100g','myristic-acid_100g','palmitic-acid_100g','stearic-acid_100g','arachidic-acid_100g','behenic-acid_100g','lignoceric-acid_100g','cerotic-acid_100g','montanic-acid_100g','melissic-acid_100g','monounsaturated-fat_100g','polyunsaturated-fat_100g','omega-3-fat_100g','alpha-linolenic-acid_100g','eicosapentaenoic-acid_100g','docosahexaenoic-acid_100g','omega-6-fat_100g','linoleic-acid_100g','arachidonic-acid_100g'], axis=1)

df=df.drop(['gamma-linolenic-acid_100g','dihomo-gamma-linolenic-acid_100g','omega-9-fat_100g','oleic-acid_100g','elaidic-acid_100g','gondoic-acid_100g','mead-acid_100g','erucic-acid_100g','nervonic-acid_100g','sucrose_100g','glucose_100g','fructose_100g','lactose_100g','maltose_100g','maltodextrins_100g','starch_100g','polyols_100g','casein_100g','serum-proteins_100g','nucleotides_100g','alcohol_100g','beta-carotene_100g','vitamin-d_100g','vitamin-e_100g','vitamin-k_100g','vitamin-b1_100g','vitamin-b2_100g','vitamin-pp_100g','vitamin-b6_100g','vitamin-b9_100g','folates_100g','vitamin-b12_100g','biotin_100g'], axis=1)

df=df.drop(['pantothenic-acid_100g','silica_100g','bicarbonate_100g','potassium_100g','chloride_100g','phosphorus_100g','magnesium_100g','zinc_100g','copper_100g','manganese_100g','fluoride_100g','selenium_100g','chromium_100g','molybdenum_100g','iodine_100g','caffeine_100g','taurine_100g','ph_100g','fruits-vegetables-nuts_100g','collagen-meat-protein-ratio_100g','cocoa_100g','chlorophyl_100g','carbon-footprint_100g','glycemic-index_100g','water-hardness_100g'], axis=1)



'''segmentation de la base de données: les calculs visent à remplacer à terme les éléments numériques qui
font défaut dans les colonnes des apports nutritionnels'''

df_segmente=df.iloc[:,19:]
dataset=df_segmente.dropna()


''' on scinde la base de données en plusieurs parties : une base de données complète
qui servira de référence pour les calculs de distances, une base de données sur laquelle on
effectuera les calculs et qui permettront de calculer les erreurs. Cette base est scindée elle-même
en deux : une base d'entrainement, l'autre de test. 
La base est issue de permutation aléatoire du jeu de données complet initial. En relançant le processus à plusieurs
reprises, on obtient donc des résultats différents ce qui permet de faire des évaluations différentes
'''

sample=np.random.permutation(len(dataset))
dataset_base=dataset.take(sample)


# la longueur indiqué ci-dessous est à titre indicative. Les tests ont été effectués sur
# des échantillons de tailles variables.


longueur=2000
base_donnee=dataset_base.iloc[0:longueur]
base_entrainement=dataset_base.iloc[longueur:longueur+150]
base_test=dataset_base.iloc[longueur+151:longueur+201]



# lancement des phases de calculs
''' Pour chaque valeur de k entre 2 et 10 compris, on cherche les plus proches voisins de la base
entrainement '''



liste_emq=[]

for k in range(2,11):
    for i in range(len(base_entrainement)):
       
        
        vecteur_entrainement=base_entrainement.iloc[i]
        soustraction=soustrac_vecteur(vecteur_entrainement,base_donnee)
        carre=mise_au_carre(soustraction)
        somme=somme_elements(carre)
        dist=distance_euclidienne(somme)
        
        voisins=kppv(dist,k)

        prochesvoisin=recup_lignes_kppv(voisins, base_donnee)



# on calcule un emq pour évaluer les différences entre les différentes données
# obtenues pour les lignes de la base de test

        difference=soustrac_array(vecteur_entrainement,prochesvoisin)
        car=mise_au_carre(difference)
        som=somme_vecteur(car)
        emq=distance_euclidienne(som)/17
        
        liste_emq.append(emq)
        liste=np.array(liste_emq)
        moy_emq=np.mean(liste)
        
    print("l'erreur moyenne quadratique pour k=",k,"est de",float(moy_emq))
 



#  on recommence les calculs en prenant cette fois-ci la base test. 
       
        
for k in range(2,11):
    for i in range(len(base_test)):
       
        
        vecteur_test=base_test.iloc[i]
        soustraction=soustrac_vecteur(vecteur_test,base_donnee)
        carre=mise_au_carre(soustraction)
        somme=somme_elements(carre)
        dist=distance_euclidienne(somme)
        
        voisins=kppv(dist,k)

        prochesvoisin=recup_lignes_kppv(voisins, base_donnee)





        difference=soustrac_array(vecteur_test,prochesvoisin)
        car=mise_au_carre(difference)
        som=somme_vecteur(car)
        emq=distance_euclidienne(som)/17
        
        liste_emq.append(emq)
        liste=np.array(liste_emq)
        moy_emq=np.mean(liste)
        
    print("l'erreur moyenne quadratique de la base test pour k=",k,"est de",float(moy_emq))



