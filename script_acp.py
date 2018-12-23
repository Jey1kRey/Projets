# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:20:21 2018

@author: Home
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import preprocessing




df=pd.read_csv("c:/projet1/echantillon_indexe.csv",sep='\t')



data=df.iloc[:,18:33]


std_scale=preprocessing.StandardScaler().fit(data)
donnees=std_scale.transform(data)



acp=PCA(n_components=6)
acp.fit(donnees)

'''test pour déterminer la variance cumulée et en déduire le nombre
de dimensions nécessaires ( règle du coude)'''

#somme_variance=np.cumsum(acp.explained_variance_ratio_)
#plt.plot(somme_variance)



acp_projete=acp.transform(donnees)

plt.scatter(acp_projete[:,0],acp_projete[:,1],c=df.get('nutrition_grade'))

plt.xlim(-10,10)
plt.ylim(-10,10)


composants=acp.components_

for i,(x,y) in enumerate(zip(composants[0,:],composants[1,:])):
    plt.plot([0,x],[0,y],color='k')
    plt.text(x,y,data.columns[i],fontsize='14')
    
plt.plot([-0.5,0.5],[0,0],color='grey',ls='--')

plt.plot([0,0],[-0.5,0.5],color='grey',ls='--')

plt.xlim([-0.5,0.5])
plt.ylim([-0.5,0.5])
plt.savefig("graphe_dim12.png",dpi=400)


