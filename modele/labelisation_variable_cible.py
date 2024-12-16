import pandas as pd


file_path = "data_beez_cleaned.csv"
data = pd.read_csv(file_path)

# Fonction pour attribuer le risque
def assign_risk(row):
    # Critère 1 : Âge
    if row['Age'] < 22 or row['Age'] > 60:
        return 'bad'

    # Critère 2 : Emploi
    if row['Job'] < 2:
        return 'bad'

    # Critère 3 : Logement
    if row['Housing'] != 'own':
        return 'bad'

    # Critère 4 : Montant du crédit
    if row['Credit amount'] >15000:
        return 'bad'

    # Critère 5 : Durée
    if row['Duration'] < 12:
        return 'bad'

    # Si tous les critères sont satisfaits, le risque est "good"
    return 'good'

#la fonction pour créer la colonne "Risk"
data['Risk'] = data.apply(assign_risk, axis=1)

#mises à jour dans du nouveau fichier CSV

output_path = "german_credit_data_risk.csv"
data.to_csv(output_path, index=False)

print(f"Fichier modifié enregistré sous : {output_path}")
