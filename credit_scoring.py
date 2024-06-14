import streamlit as st
import requests

# URL de l'API Flask :
API_URL = 'https://credit-scoring-api-df2c330f1d06.herokuapp.com/predict'
    
def predict(sk_id_curr):
    """
    Requête de l'API Flask
    """
    response = requests.post(API_URL, json={'SK_ID_CURR': sk_id_curr})
    if response.status_code == 200:
        return response.json()['Dossier']
    else:
        return 'Erreur: Identifiant client non trouvé'

# Début de l'application Streamlit
st.title('Analyse de dossier crédit')

# Saisie de l'ID client
sk_id_curr = st.number_input('Entrez l\'ID client', format="%.0f")

# Bouton pour effectuer la prédiction
if st.button('Analyse du dossier'):
    dossier = predict(sk_id_curr)
    st.write(dossier)
