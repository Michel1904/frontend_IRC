import streamlit as st
import requests

st.title("Prédiction du Stade de l'IRC")

# Dictionnaire de mappage pour remplacer les noms des champs booléens
field_mapping = {
    "motif_asthenie": "Motif(s) d'Admission/Asthénie",
    "motif_alt_fonction": "Motif(s) d'Admission/Altération de la fonction rénale",
    "motif_hta": "Motif(s) d'Admission/HTA",
    "motif_oedeme": "Motif(s) d'Admission/Œdème",
    "motif_diabete": "Motif(s) d'Admission/Diabète",
    "pm_hta": 'Personnels Médicaux/HTA',
    "pm_diabete1": 'Personnels Médicaux/Diabète 1',
    "pm_diabete2": 'Personnels Médicaux/Diabète 2',
    "pm_cardiovasculaire": 'Personnels Médicaux/Maladies Cardiovasculaire(Cardiopathie, AVC, preeclampsie)',
    "symptome_anemie": 'Symptômes/Anémie',
    "symptome_hta": 'Symptômes/HTA',
    "symptome_asthenie": 'Symptômes/Asthénie',
    "symptome_insomnie": 'Symptômes/Insomnie',
    "symptome_perte_poids": 'Symptômes/Perte de poids',
    "anemie": 'Anémie'
}

# Liste des champs booléens
bool_fields = [
    "motif_asthenie", "motif_alt_fonction", "motif_hta", "motif_oedeme", "motif_diabete",
    "pm_hta", "pm_diabete1", "pm_diabete2", "pm_cardiovasculaire",
    "symptome_anemie", "symptome_hta", "symptome_asthenie",
    "symptome_insomnie", "symptome_perte_poids", "anemie"
]

# Dictionnaire pour stocker les entrées de l'utilisateur
input_data = {}
input_data['age'] = st.number_input("Age", 0, 120, 50)

# Affichage des champs booléens avec leurs intitulés
for field in bool_fields:
    label = field_mapping[field]  # Récupérer l'intitulé réel
    input_data[field] = 1 if st.radio(label, ["Non", "Oui"]) == "Oui" else 0

# Sélection de l'état général à l'admission
etat = st.selectbox("Etat Général à l'Admission", ["Bon", "Acceptable", "Altéré"])
etat_map = {"Bon": 1, "Acceptable": 2, "Altéré": 3}
input_data['etat_general'] = etat_map[etat]

# Entrées supplémentaires pour les résultats médicaux
input_data['uree'] = st.number_input("Urée (g/L)", 0.0, 5.0, 0.5)
input_data['creatinine'] = st.number_input("Créatinine (mg/L)", 0.0, 50.0, 1.0)

# Bouton pour faire la prédiction
if st.button("Prédire"):
    response = requests.post("https://backend-irc.onrender.com/predict", json=input_data)
    st.success(response.json()['result'])
