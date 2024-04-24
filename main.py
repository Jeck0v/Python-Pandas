import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download
from sqlalchemy import create_engine

#--------------------- IMPORT -------------------#
df = pd.DataFrame(
    {
        "Name": [
            "Brand, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "Louis, Louis Donkey",
            "Max, Maxime Biden",
            "Alex, Alexis Frontier",
        ],
        "Age": [22, 35, 58, 19, 27, 24],
        "Sex": ["male", "male", "female", "male", "male", "male"],
    }
)
#--------------------- DataFrame1 -------------------#

nb = 2

print("================================================================")
print(" .head permet de voir le", nb ,"premières lignes sélectionner ")
print("================================================================")
print(df.head(nb))
print("================================================================")
print(" .tail permet de voir les", nb ,"dernières lignes sélectionner ")
print("================================================================")
print(df.tail(nb))
print("================================================================")
#data = pd.read_json('data.json') #prend les infos du json => transforme en DataFrame de Pandas


#engine = create_engine('sqlite:///mydatabase.db', echo=True)
#df.to_sql('mytable', engine, if_exists='replace')   #récupère le dataframe et le transforme en SQL via .to_sql
# créer une table myttable et si elle existe déjà, il l'a remplace

#--------------------- Sous-Ensemble -------------------#
# On utilise les crochets []
# Selec Ligne / colonne spé avec .loc en utilisant leur nom
# Selec ligne / colonne spé avec .iloc en utilisant leur positions dans le tableau

ages = df["Age"]
print("================================================================")
print(ages)
print("================================================================")
print("Permet de sélectionner une seule colonne de la DataFrame 1 ")
print("================================================================")
AgeDiff = df["Age"] >= 35
print(AgeDiff)
print("================================================================")
print("Permet de sélectionner une seule colonne Age, supérieur à 35 ans")
print("================================================================")


ad_name = df.loc[df["Age"] >=35 , "Name"]
print(ad_name)
print("================================================================")
print("Permet de sélectionner des lignes et des colonnes spécifiques")
print("On sélectionne les noms des personnes d'au moins 35 ans ")
# opérateur .loc => df["Age] >=35 est la lignes souhaitez et "Name" est la colonne souhaiter
print("================================================================")

iloc = df.iloc[0:3, 0:1]    # 0:3 => lignes 0 à 2 (3 => lignes 0, 1, 2)
print(iloc)
print("================================================================")
print("Permet de sélectionner les lignes 0 à 2 et les colonnes 0 à 1")
print("================================================================")
