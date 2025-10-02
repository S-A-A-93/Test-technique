# Test-technique
# Projet: Pipeline de Données Automatisé avec l'API Ameli, DuckDB et Rapport HTML
# Introduction
Ce projet est un exemple simple de pipeline de données (mini chaîne de traitement de données) : un ensemble d’étapes automatisées qui permettent de récupérer, stocker et analyser des données. Ici, nous travaillons sur des données de santé liées aux cancers en Île-de-France (100 lignes), issues de l’API publique de l’Assurance Maladie (Ameli), via le url suivant: https://data.ameli.fr/explore/dataset/effectifs/information/

L’intérêt est de montrer comment, à partir d’un script Python, on peut extraire des données en ligne, les transformer, les sauvegarder, puis créer un rapport automatiquement.

# Description détaillée du code
## Étape 1 : Extraction des données via l’API Ameli
Le programme interroge l'API Open Data de l’Assurance Maladie pour récupérer des informations sur les dépenses associées aux cancers dans la région Île-de-France.

La requête est paramétrée pour cibler précisément cette pathologie et cette région.

On vérifie bien que des données sont renvoyées ; sinon le programme s’arrête avec un message d’erreur clair.

## Étape 2 : Sauvegarde au format CSV
Les données récupérées sont mises dans un format tableau (“DataFrame” avec Pandas), puis enregistrées dans un fichier CSV local (nommé recup_cancers_idf.csv).

Ce fichier garde une trace des données brutes avant toute modification.

Le script propose dans Google Colab un bouton pour télécharger ce fichier sur votre ordinateur.

## Étape 3 : Création d’une base de données locale DuckDB
Une base de données locale légère est créée avec DuckDB, et le contenu du fichier CSV est importé dans une table.

L’intérêt ici est de faciliter les requêtes SQL sur nos données et de préparer le projet à une éventuelle montée en charge.

Cette base est stockée ensuite dans un fichier cancers_idf.duckdb sur votre ordinateur.

## Étape 4 : Génération d’un rapport HTML
Le programme interroge la base DuckDB pour extraire un résumé de plusieurs enregistrements (limité ici à 100 résultats) puis crée un document HTML.

Ce rapport présente les données de façon lisible dans un navigateur web (exp: Microsoft Edge), avec une mise en forme.

Il s’appelle rapport_cancers.html et peut être ouvert comme une page web.

# Utilisation
Cette pipeline est entièrement automatisée : lancez simplement le script Python.

Les fichiers CSV, base DuckDB et rapport HTML sont créés automatiquement et peuvent être facilement consultés.

En environnement Google Colab, des liens de téléchargement permettent de récupérer les fichiers générés si besoin.
