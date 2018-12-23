# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:31:05 2018

@author: Home
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("liste_aliments.csv", sep='\t', low_memory=False)


df=df.drop(['url','creator','created_t','created_datetime','last_modified_t','last_modified_datetime','generic_name','packaging','packaging_tags','quantity','brands', 'categories','categories_tags','categories_fr','origins_tags','manufacturing_places_tags','labels_tags','emb_codes','emb_codes_tags','first_packaging_code_geo','cities','cities_tags','purchase_places','stores','countries','countries_tags','countries_fr','allergens','traces','traces_tags','traces_fr','no_nutriments','additives_tags','additives_fr','ingredients_from_palm_oil_n','ingredients_from_palm_oil_tags','ingredients_that_may_be_from_palm_oil_n','ingredients_that_may_be_from_palm_oil_tags'], axis=1)

df=df.drop(['states','states_tags','main_category','main_category_fr','image_url','image_small_url'], axis=1)

df=df.drop(['energy-from-fat_100g','butyric-acid_100g','caproic-acid_100g','caprylic-acid_100g','capric-acid_100g','lauric-acid_100g','myristic-acid_100g','palmitic-acid_100g','stearic-acid_100g','arachidic-acid_100g','behenic-acid_100g','lignoceric-acid_100g','cerotic-acid_100g','montanic-acid_100g','melissic-acid_100g','monounsaturated-fat_100g','polyunsaturated-fat_100g','omega-3-fat_100g','alpha-linolenic-acid_100g','eicosapentaenoic-acid_100g','docosahexaenoic-acid_100g','omega-6-fat_100g','linoleic-acid_100g','arachidonic-acid_100g'], axis=1)

df=df.drop(['gamma-linolenic-acid_100g','dihomo-gamma-linolenic-acid_100g','omega-9-fat_100g','oleic-acid_100g','elaidic-acid_100g','gondoic-acid_100g','mead-acid_100g','erucic-acid_100g','nervonic-acid_100g','sucrose_100g','glucose_100g','fructose_100g','lactose_100g','maltose_100g','maltodextrins_100g','starch_100g','polyols_100g','casein_100g','serum-proteins_100g','nucleotides_100g','alcohol_100g','beta-carotene_100g','vitamin-d_100g','vitamin-e_100g','vitamin-k_100g','vitamin-b1_100g','vitamin-b2_100g','vitamin-pp_100g','vitamin-b6_100g','vitamin-b9_100g','folates_100g','vitamin-b12_100g','biotin_100g'], axis=1)

df=df.drop(['pantothenic-acid_100g','silica_100g','bicarbonate_100g','potassium_100g','chloride_100g','phosphorus_100g','magnesium_100g','zinc_100g','copper_100g','manganese_100g','fluoride_100g','selenium_100g','chromium_100g','molybdenum_100g','iodine_100g','caffeine_100g','taurine_100g','ph_100g','fruits-vegetables-nuts_100g','collagen-meat-protein-ratio_100g','cocoa_100g','chlorophyl_100g','carbon-footprint_100g','glycemic-index_100g','water-hardness_100g'], axis=1)


#df.to_csv("liste_allegee.csv", sep='\t')

'''
# on va chercher à obtenir une base de données remplies, avec qqs milliers de lignes, pour effectuer le training et les tests

df_training=df.dropna(thresh=27)

df_training.to_csv("liste_training.csv",sep='\t')'''


df_base=df.dropna(thresh=27)


df_base.to_csv("liste_base.csv",sep='\t')


print(df_base.head(5))

'''
# les colonnes des apports sont transformés en type float

for x in len(df):
    for y in range(62,162):
        df[x][y]=float(df[x][y])
'''




#& test sur les lignes avec données manquantes


#fichier_nettoye=df_net.dropna(thresh=22)

#fichier_nettoye.to_csv("c:\projet1\essai_fichier.csv",sep='\t')

#print(len(fichier_nettoye))
















