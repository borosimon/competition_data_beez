import joblib
import pandas as pd

# Charger le modèle
model = joblib.load('modele/data_beez_modele.pkl')

# Charger les nouvelles données
data = pd.read_csv('german_credit_data.csv')
print("Données chargées :")
print(data.head())

# Prédire
predictions = model.predict(data)

# Ajouter les résultats dans le DataFrame
data['Prediction'] = predictions

# Afficher les résultats
print("Résultats des prédictions :")
print(data)

# Sauvegarder les résultats
data.to_csv('resultats_predictions.csv', index=False)
print("Prédictions sauvegardées dans 'resultats_predictions.csv'")
