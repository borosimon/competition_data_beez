#Importation des librairies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Chargements de la données
data_beez = pd.read_csv("german_credit_data.csv", index_col=0)
print("Données chargées!")

#Information générale sur la données
print(data_beez.head()) #L'entete
print(data_beez.tail()) #La queu
print(data_beez.info()) #Les type de variable
print(data_beez.describe()) #Statistique descriptive

#Affichage des valeurs manquantes
print(data_beez.isna().sum())

#Remplissages des valeurs manquantes par Inconnue
data_beez['Saving accounts'] = data_beez['Saving accounts'].fillna('Inconnue')
data_beez['Checking account'] = data_beez['Checking account'].fillna('Inconnue')
data_beez.to_csv("data_beez_cleaned.csv")
#Afficher la données après nettoyage
print(data_beez.isnull().sum())

#Recherche des plus grandes corrélations avec l'octroi  ou non de crédit

# 1.Scatter plot : Montant du crédit et la durée
sns.scatterplot(data=data_beez, x='Duration', y='Credit amount')
plt.title("Le montant du crédit et sa durée")
plt.show()

# 2.Histogrammes des ages
data_beez['Age'].plot(kind='hist', bins=20, edgecolor='black')
plt.title("Distribution des âges")
plt.xlabel("Age")
plt.ylabel("Fréquence")
plt.show()

# 3.Heatmap des corrélations
numeric_columns = data_beez.select_dtypes(include=['number'])
corr_matrix = numeric_columns.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap des corrélations")
plt.show()


