# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:12:58 2018

@author: Home
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing


''' Le programme ci-dessous se décompose en plusieurs parties. La première
consiste en la définition des fonctions. La seconde est le programme de calcul 
des k plus proches voisins de la base de données, puis le remplissage
des lignes aux données manquantes. Enfin, la dernière partie est le calcul de l'ACP. Il ne 
sera pas poursuivi sous python puisque le reste et la fin du projet ont été effectué sous R'''



''' définition des fonctions'''

def soustrac_array(vecteur_test, vecteur_moyenne):
    vecteur_test=np.array(vecteur_test)
    
    soustraction=vecteur_moyenne-vecteur_test
    
    return (soustraction)

def soustrac_vecteur(vecteur_test,dataset_entrainement):
    
    vecteur=np.array(vecteur_test)
    soustrac=dataset_entrainement.sub(vecteur, axis=1)

    return (soustrac)
        
def mise_au_carre(matrice):
    carre=matrice**2
    
    return (carre)

def somme_elements(matrice):
    somme=matrice.sum(axis=1)
    
    return (somme)

def somme_vecteur(vecteur):
    somme=vecteur.sum()
    return(somme)


def distance_euclidienne(matrice):
    dist=np.sqrt(matrice)
    
    return (dist)

def kppv(dist_euclid,k):
    liste_dist=dist_euclid.sort_values()
    kppv=liste_dist[0:k]
        
    return (kppv)


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

def donnee_moyennee(moyenne_kppv,index_vecteur_a_remplir):
    
    vecteur_moyenne=pd.Series(moyenne_kppv,index=index_vecteur_a_remplir)
    
    return (vecteur_moyenne)


''' récupération du fichier, nettoyage et séparation en deux blocs de données'''


df=pd.read_csv("liste_aliments.csv", sep='\t', low_memory=False,encoding='utf-8')


df=df.drop(['url','creator','created_t','created_datetime','last_modified_t','last_modified_datetime','generic_name','packaging','packaging_tags','quantity','brands', 'categories','categories_tags','categories_fr','origins_tags','manufacturing_places_tags','labels_tags','emb_codes','emb_codes_tags','first_packaging_code_geo','cities','cities_tags','purchase_places','stores','countries','countries_tags','countries_fr','allergens','traces','traces_tags','traces_fr','no_nutriments','additives_tags','additives_fr','ingredients_from_palm_oil_n','ingredients_from_palm_oil_tags','ingredients_that_may_be_from_palm_oil_n','ingredients_that_may_be_from_palm_oil_tags'], axis=1)

df=df.drop(['states','states_tags','main_category','main_category_fr','image_url','image_small_url'], axis=1)

df=df.drop(['energy-from-fat_100g','butyric-acid_100g','caproic-acid_100g','caprylic-acid_100g','capric-acid_100g','lauric-acid_100g','myristic-acid_100g','palmitic-acid_100g','stearic-acid_100g','arachidic-acid_100g','behenic-acid_100g','lignoceric-acid_100g','cerotic-acid_100g','montanic-acid_100g','melissic-acid_100g','monounsaturated-fat_100g','polyunsaturated-fat_100g','omega-3-fat_100g','alpha-linolenic-acid_100g','eicosapentaenoic-acid_100g','docosahexaenoic-acid_100g','omega-6-fat_100g','linoleic-acid_100g','arachidonic-acid_100g'], axis=1)

df=df.drop(['gamma-linolenic-acid_100g','dihomo-gamma-linolenic-acid_100g','omega-9-fat_100g','oleic-acid_100g','elaidic-acid_100g','gondoic-acid_100g','mead-acid_100g','erucic-acid_100g','nervonic-acid_100g','sucrose_100g','glucose_100g','fructose_100g','lactose_100g','maltose_100g','maltodextrins_100g','starch_100g','polyols_100g','casein_100g','serum-proteins_100g','nucleotides_100g','alcohol_100g','beta-carotene_100g','vitamin-d_100g','vitamin-e_100g','vitamin-k_100g','vitamin-b1_100g','vitamin-b2_100g','vitamin-pp_100g','vitamin-b6_100g','vitamin-b9_100g','folates_100g','vitamin-b12_100g','biotin_100g'], axis=1)

df=df.drop(['pantothenic-acid_100g','silica_100g','bicarbonate_100g','potassium_100g','chloride_100g','phosphorus_100g','magnesium_100g','zinc_100g','copper_100g','manganese_100g','fluoride_100g','selenium_100g','chromium_100g','molybdenum_100g','iodine_100g','caffeine_100g','taurine_100g','ph_100g','fruits-vegetables-nuts_100g','collagen-meat-protein-ratio_100g','cocoa_100g','chlorophyl_100g','carbon-footprint_100g','glycemic-index_100g','water-hardness_100g'], axis=1)



df_partiegauche=df.iloc[:,0:19]
df_temp=df.iloc[:,19:]




''' récupération d'un échantillon aux données non manquantes'''



dataset_plein=df_temp.dropna()

''' longueur du fichier de données : pour des tests, pour des échantillons, on entrera
le nombre de lignes désirées'''

longueur=len(df_temp)


base_donnee=[]


''' calcul des k plus proches voisins pour chacune des lignes du fichier aux données manquantes : le 
calcul est effectué par rapport au fichier de données non manquantes'''

  
for i in range(longueur):  
    ligne_a_remplir=df_temp.iloc[i]
    index_ligne_a_remplir=ligne_a_remplir.index




    soustraction=soustrac_vecteur(ligne_a_remplir,dataset_plein)
    carre=mise_au_carre(soustraction)
    somme=somme_elements(carre)
    dist=distance_euclidienne(somme)

    voisins=kppv(dist,3)
    prochesvoisin=recup_lignes_kppv(voisins, dataset_plein)

    ligne_remplie=donnee_moyennee(prochesvoisin,index_ligne_a_remplir)

    ligne_complete=ligne_a_remplir.fillna(ligne_remplie)


    base_donnee.append(ligne_complete)

# récupération du dataset dont les lignes ont été corrigées

dataset_corrige=pd.DataFrame(base_donnee)


# finalisation du fichier

df_final=pd.concat([df_partiegauche,dataset_corrige],axis=1, join='inner')


# réindexation sur le nom des produits 

df_index=df_final.reset_index(drop=True)
df_modif=df_index.set_index(['product_name'])

# vérification du fichier final

#print(df_modif.head(10))


# exportation sous forme de csv du dataset corrigé et complet

df_final.to_csv("echantillon_complet.csv", sep='\t')

df_modif.to_csv("liste_echantillon.csv",sep='\t')



''' calcul de l'ACP : récupération des données quantitatives puis calcul via sklearn'''

data=df_modif.iloc[:,18:33]


std_scale=preprocessing.StandardScaler().fit(data)
donnees=std_scale.transform(data)



acp=PCA(n_components=6)
acp.fit(donnees)

'''test pour déterminer la variance cumulée et en déduire le nombre
de dimensions nécessaires ( règle du coude)'''

somme_variance=np.cumsum(acp.explained_variance_ratio_)
plt.plot(somme_variance)



acp_projete=acp.transform(donnees)


''' test pour les graphes de l'ACP. Le travail ici n'est qu'une ébauche effectuée après que 
l'ACP et les graphes ont été calculés et dessinés sous R'''


composants=acp.components_
comp_cos=np.cos(composants)
compos_cos2=comp_cos**2

''' graphes des dimensions 1 et 2 : cela ne sera pas utilisé pour la suite du projet. On utilisera
R en partant du fichier de données remplis'''

for i,(x,y) in enumerate(zip(composants[0,:],composants[1,:])):
    plt.plot([0,x],[0,y],color='k')
    plt.text(x,y,data.columns[i],fontsize='14')
    
plt.plot([-0.5,0.5],[0,0],color='grey',ls='--')

plt.plot([0,0],[-0.5,0.5],color='grey',ls='--')

plt.xlim([-0.5,0.5])
plt.ylim([-0.5,0.5])
plt.savefig("graphe_dim12.png",dpi=400)



