import requests



url = "https://data.ademe.fr/data-fair/api/v1/datasets/base-carboner/schema"



try:

  response = requests.get(url)

  response.raise_for_status() # Vérifie si la requête a réussi

  schema = response.json() # Convertit la réponse en JSON

  print(schema) # Affiche le schéma récupéré

except requests.exceptions.RequestException as e:

  print(f"Erreur lors de la requête : {e}")

