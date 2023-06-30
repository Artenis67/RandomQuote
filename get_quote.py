import requests

# Endpoint de l'API
url = "https://quotes.rest/qod"

# Paramètres de requête (incluant la clé d'API)
params = {
    "language": "fr",  # Langue des citations (français)
    "category": "inspire",  # Catégorie des citations (inspirantes)
    "api_key": "jcLYnSzb1FReLe9LM23SVLxbFPMs5KNTX6MvFGQH"  # Remplacez par votre propre clé d'API
}

# Faire la requête à l'API avec les paramètres
response = requests.get(url, params=params)

# Vérifier si la requête a réussi (code 200 signifie succès)
if response.status_code == 200:
    # Extraire les données de la réponse
    data = response.json()

    # Vérifier si la clé 'quotes' est présente dans la réponse
    if "quotes" in data["contents"]:
        # Récupérer la citation aléatoire
        quote = data["contents"]["quotes"][0]["quote"]
        author = data["contents"]["quotes"][0]["author"]

        # Afficher la citation et l'auteur
        print(f"{quote} - {author}")
    else:
        print("La clé 'quotes' n'est pas présente dans la réponse de l'API.")
else:
    print("Erreur lors de la requête à l'API.")
