import requests

import json



url = "https://data.ademe.fr/data-fair/api/v1/datasets/base-carboner/schema"

output_file = "schema_base_carbone.json"



try:

  response = requests.get(url)

  response.raise_for_status() # Vérifie si la requête a réussi

  schema = response.json() # Convertit la réponse en JSON



  # Sauvegarde dans un fichier JSON

  with open(output_file, "w", encoding="utf-8") as f:

    json.dump(schema, f, indent=4, ensure_ascii=False)



  print(f"Schéma sauvegardé dans {output_file}")

except requests.exceptions.RequestException as e:

  print(f"Erreur lors de la requête : {e}")

