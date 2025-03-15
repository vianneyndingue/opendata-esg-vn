import requests

import os



# URL de l'API

url = "https://data.ademe.fr/data-fair/api/v1/datasets/base-carboner/data-files"



# Dossier où sauvegarder les fichiers

output_dir = "base_carbone_files"

os.makedirs(output_dir, exist_ok=True)



try:

  # Requête pour obtenir la liste des fichiers

  response = requests.get(url)

  response.raise_for_status() # Vérifie si la requête a réussi

  files = response.json() # Convertit la réponse en JSON



  # Parcours et téléchargement de chaque fichier

  for file in files:

    file_url = file.get("url") # Récupère l'URL du fichier

    file_name = file.get("title", "unknown_file") # Nom du fichier

     

    if file_url:

      file_path = os.path.join(output_dir, file_name)

      print(f"Téléchargement de {file_name}...")

       

      file_response = requests.get(file_url)

      file_response.raise_for_status() # Vérifie si le téléchargement a réussi



      # Sauvegarde du fichier
      file_path = "base_carbone_files/base_carbone.csv"
      with open(file_path, "wb") as f:

        f.write(file_response.content)

       

      print(f"{file_name} téléchargé avec succès dans {output_dir}/")



except requests.exceptions.RequestException as e:

  print(f"Erreur lors de la requête : {e}")