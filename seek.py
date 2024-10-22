import random
import pandas as pd
from datetime import datetime

# Définir les groupes et les probabilités
GROUP_A = range(1, 51)  # 1 à 50
GROUP_B = range(51, 100)  # 51 à 99
GROUP_C = range(100, 151, 5)  # 100 à 150 par pas de 5

TOTAL_UNITS = 100_000_000  # 100 millions d'unités
UNITS_PER_BLOCK = 1000  # Par exemple, chaque bloc distribue 1000 unités
TOTAL_BLOCKS = TOTAL_UNITS // UNITS_PER_BLOCK  # Calculer le nombre total de blocs

# Fonction pour miner un bloc et répartir les gains
def mine_block(block_value):
    # Probabilités de groupe
    group = ""
    if block_value in GROUP_A:
        group = "A"
    elif block_value in GROUP_B:
        group = "B"
    elif block_value in GROUP_C:
        group = "C"

    # Simuler le processus de tirage et de répartition des gains
    chance = random.random()  # Chance aléatoire entre 0 et 1

    if group == "A":
        if chance < 0.8:  # 8 chances sur 10 pour une division
            return "A", distribute_rewards("A")
        else:
            return "A", None  # Pas de récompense

    elif group == "B":
        if chance < (1 / 3):  # 1 sur 3
            return "B", distribute_rewards("B")
        else:
            return "B", None  # Pas de récompense

    elif group == "C":
        if chance < (1 / 3):  # 1 sur 3
            return "C", distribute_rewards("C", bonus=True)
        else:
            return "C", distribute_rewards("C")

# Fonction pour distribuer les gains selon le groupe
def distribute_rewards(group, bonus=False):
    rewards = {}
    if group == "A":
        rewards["miners"] = UNITS_PER_BLOCK * 0.25  # 25% aux mineurs
        rewards["briseur"] = UNITS_PER_BLOCK * 0.07  # 7% * 2 pour les ordinateurs spectateurs
        rewards["owners"] = UNITS_PER_BLOCK * 0.61  # Les 61% restants
    elif group == "B":
        rewards["miners"] = UNITS_PER_BLOCK * 0.25
        rewards["briseur"] = UNITS_PER_BLOCK * 0.07
        rewards["owners"] = UNITS_PER_BLOCK * 0.61
        if bonus:  # Bonus pour réinvestissement dans le groupe B
            rewards["bonus"] = UNITS_PER_BLOCK * 0.10  # Ajout d'un bonus de 10%
    elif group == "C":
        rewards["miners"] = UNITS_PER_BLOCK * 0.25
        rewards["briseur"] = UNITS_PER_BLOCK * 0.07
        rewards["owners"] = UNITS_PER_BLOCK * 0.61
        if bonus:
            rewards["bonus"] = UNITS_PER_BLOCK * 0.10

    return rewards

# Fonction pour simuler un ensemble de blocs et enregistrer les résultats
def simulate_mining(num_blocks):
    data = []
    total_units_mined = 0
    for i in range(num_blocks):
        block_value = random.randint(1, 150)  # Générer un bloc aléatoire entre 1 et 150
        group, rewards = mine_block(block_value)
        if rewards:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data.append({
                "Block Number": i + 1,
                "Block Value": block_value,
                "Group": group,
                "Miners Share": rewards["miners"],
                "Briseur Share": rewards["briseur"],
                "Owners Share": rewards["owners"],
                "Bonus": rewards.get("bonus", 0),
                "Timestamp": timestamp
            })
            total_units_mined += UNITS_PER_BLOCK

    # Créer un DataFrame et enregistrer dans un fichier Excel
    df = pd.DataFrame(data)
    df.to_excel("mining_results_100m.xlsx", index=False)
    print(f"Mining simulation completed. {total_units_mined} units mined and saved to mining_results_100m.xlsx")

# Simuler le minage des blocs pour couvrir 100 millions d'unités
simulate_mining(TOTAL_BLOCKS)

# Exemple de sortie:
# Mining simulation completed. 100000000 units mined and saved to mining_results_100m.xlsx

# Le fichier Excel généré contiendra les détails de chaque bloc miné, y compris les récompenses pour les mineurs, les briseurs, les propriétaires et les bonus.
# Vous pouvez ensuite analyser ces données pour voir comment les récompenses sont réparties entre les différents groupes de blocs.
# Vous pouvez également ajuster les probabilités et les récompenses pour voir comment cela affecte la distribution des gains.

# Pour exécuter ce script, vous aurez besoin d'installer la bibliothèque pandas en utilisant la commande suivante:

# pip install
# pandas
# Vous pouvez également personnaliser davantage ce script en ajoutant des fonctionnalités supplémentaires, telles que le calcul des rendements pour les mineurs, les briseurs et les propriétaires en fonction des récompenses reçues.
# Vous pouvez également ajouter des graphiques pour visualiser les données générées par la simulation.
# J'espère que cela vous aidera à simuler le processus de minage de blocs et à comprendre comment les récompenses sont réparties entre les différents groupes de blocs.
# N'hésitez pas à poser des questions si vous avez besoin d'aide supplémentaire ou si vous avez des commentaires sur ce script.

# Merci pour votre attention!
# Cordialement,
# L'équipe de support technique
# The Python Company

# Source:
# https://www.programiz.com/python-programming/examples/generate-random-number
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
# https://www.geeksforgeeks.org/python-pandas-dataframe/
# https://www.w3schools.com/python/python_datetime.asp
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.programiz.com/python-programming/methods/built-in/getattr
# https://www.programiz.com/python-programming/methods/built-in/setattr
# https://www.programiz.com/python-programming/methods/built-in/hasattr
# https://www.programiz.com/python-programming/methods/built-in/delattr
# https://www.programiz.com/python-programming/methods/built-in/vars

# Exemple de sortie:
# Mining simulation completed. 100000000 units mined and saved to mining_results_100
# m.xlsx
# Le fichier Excel généré contiendra les détails de chaque bloc miné, y compris les récompenses pour les mineurs, les briseurs, les propriétaires et les bonus.
# Vous pouvez ensuite analyser ces données pour voir comment les récompenses sont réparties entre les différents groupes de blocs.
# Vous pouvez également ajuster les probabilités et les récompenses pour voir comment cela affecte la distribution des gains.
# Pour exécuter ce script, vous aurez besoin d'installer la bibliothèque pandas en utilisant la commande suivante:

# pip install pandas
# Vous pouvez également personnaliser davantage ce script en ajoutant des fonctionnalités supplémentaires, telles que le calcul des rendements pour les mineurs, les briseurs et les propriétaires en fonction des récompenses reçues.

# Vous pouvez également ajouter des graphiques pour visualiser les données générées par la simulation.
# J'espère que cela vous aidera à simuler le processus de minage de blocs et à comprendre comment les récompenses sont réparties entre les différents groupes de blocs.
# N'hésitez pas à poser des questions si vous avez besoin d'aide supplémentaire ou si vous avez des commentaires sur ce script.
# Merci pour votre attention!
# Cordialement,
# L'équipe de support technique
# The Python Company

# Source:
# https://www.programiz.com/python-programming/examples/generate-random-number
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
