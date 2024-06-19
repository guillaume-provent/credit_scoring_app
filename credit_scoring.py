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
        result = response.json()
        dossier = result.get('Dossier')
        probabilite = result.get('Probabilite')
        seuil = result.get('Seuil')
        return dossier, probabilite, seuil
    else:
        return 'Erreur: Identifiant client non trouvé', None, None

# Début de l'application Streamlit
st.title('Analyse de dossier crédit')

# Saisie de l'ID client
sk_id_curr = st.number_input('Entrez l\'ID client', format="%.0f")

# Bouton pour effectuer la prédiction
if st.button('Analyse du dossier'):
    dossier, probabilite, seuil = predict(sk_id_curr)
    st.write(dossier)
    st.write(f'Probabilité de défaut : {probabilite} (seuil : {seuil})')
