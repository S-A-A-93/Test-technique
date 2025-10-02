import requests
import pandas as pd
import duckdb
from google.colab import files

# --- Étape 1 : Extraction des données de l'API Ameli ---
params = {
    'q': 'patho_niv1:Cancers AND region:11',
    'rows': 100,
    'dataset': 'effectifs'
}
url = "https://data.ameli.fr/api/records/1.0/search/"
response = requests.get(url, params=params)
data = response.json()

if 'records' not in data or len(data['records']) == 0:
    raise ValueError("Aucune donnée récupérée pour votre requête.")

records = [record['fields'] for record in data['records']]
df = pd.DataFrame(records)

if df.empty or df.shape[1] == 0:
    raise ValueError("Le DataFrame est vide : vérifiez la requête API.")

# --- Étape 2 : Sauvegarde et téléchargement du CSV ---
csv_name = "recup_cancers_idf.csv"
df.to_csv(csv_name, index=False)
files.download(csv_name)        # Permet de télécharger le fichier sur votre PC

# --- Étape 3 : Création base DuckDB et sauvegarde ---
db_name = "cancers_idf.duckdb"
con = duckdb.connect(db_name)
con.execute("CREATE TABLE IF NOT EXISTS cancers AS SELECT * FROM df")
con.close()
files.download(db_name)         # Permet de télécharger la base DuckDB

# --- Étape 4 : Génération du rapport HTML ---
con = duckdb.connect(db_name, read_only=True)
rapport = con.execute("SELECT * FROM cancers LIMIT 100").df()
html_name = "rapport_cancers.html"
with open(html_name, "w", encoding="utf-8") as f:
    f.write("<h2>Rapport : Exemples de cancers en Île-de-France</h2>")
    f.write(rapport.to_html(index=False))
con.close()
files.download(html_name)       # Permet de télécharger le rapport HTML

print("Tous les fichiers sont créés avec succès.")
