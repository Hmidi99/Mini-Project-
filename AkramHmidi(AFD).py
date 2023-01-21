# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:56:03 2021

@author: akram
"""

import pandas as pd
df = pd.read_csv('HR_SBA_Software.csv',header=0)
##########print(df['sales'].value_counts(normalize=True))##########
#############print(df['left'])###############

#percentage du Nombre d'employés qui quittent /restent dans l'entreprise par département


print(df.groupby(["left", "sales"]).size().transform(lambda x: x / x.sum()))


#percentage du Nombre d'employés qui quittent/restent dans l'entreprise par niveau de salaire 

print(df.groupby(["left", "salary"]).size().transform(lambda x: x / x.sum()))

#percentage du Nombre d'années passées avant de quitter / continuer à rester

print(df.groupby(["left", "time_spend_company"]).size().transform(lambda x: x / x.sum()))

#percentage des employées qui quittent/restent lors d'un accident pendant le séjour du salarié

print(df.groupby(["left", "Work_accident"]).size().transform(lambda x: x / x.sum()))

#percentage des employées qui quittent/restent lors d'un Nombre de promotions dans son séjour

print(df.groupby(["left", "promotion_last_5years"]).size().transform(lambda x: x / x.sum()))



#percentage des employées qui quittent/restent lors Nombre moyen d'heures par mois, passées par un employé au bureau

df["bins"] = pd.cut(df[ 'average_montly_hours'], [0, 100, 200, 300,400])
print(df.groupby(["bins","left"])[ 'average_montly_hours'].agg(['count']).transform(lambda x: x / x.sum()))



#percentage des employees qui quittent/restent lors l'employe est impliqué dans le projet 

print(df.groupby(["left", "number_project"]).size().transform(lambda x: x / x.sum()))


#percentage des employées qui quittent/restent lors de sa dernière évaluation

df["last_evaluation"] = pd.cut(df[ 'last_evaluation'], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
print(df.groupby(["last_evaluation","left"])[ 'last_evaluation'].agg(['count']).transform(lambda x: x / x.sum()))


#percentage des employées qui quittent/restent au  niveau de satisfaction du travail
df["satisfaction_level"] = pd.cut(df[ 'satisfaction_level'], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
print(df.groupby(["satisfaction_level","left"])[ 'satisfaction_level'].agg(['count']).transform(lambda x: x / x.sum()))


