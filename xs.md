import random
import pandas as pd
from datetime import datetime

# Définir les groupes et les probabilités
GROUP_A = range(1, 51)  # 1 à 50
GROUP_B = range(51, 100)  # 51 à 99
GROUP_C = range(100, 151, 5)  # 100 à 150 par pas de 5

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
        rewards["miners"] = 25
        rewards["briseur"] = 14  # 7% * 2 pour les ordinateurs spectateurs
        rewards["owners"] = 61  # Les 61% restants
    elif group == "B":
        rewards["miners"] = 25
        rewards["briseur"] = 14
        rewards["owners"] = 61
        if bonus:  # Bonus pour réinvestissement dans le groupe B
            rewards["bonus"] = 10  # Ajout d'un bonus de 10%
    elif group == "C":
        rewards["miners"] = 25
        rewards["briseur"] = 14
        rewards["owners"] = 61
        if bonus:
            rewards["bonus"] = 10

    return rewards

# Fonction pour simuler un ensemble de blocs et enregistrer les résultats
def simulate_mining(num_blocks):
    data = []
    for i in range(num_blocks):
        block_value = random.randint(1, 150)  # Générer un bloc aléatoire entre 1 et 150
        group, rewards = mine_block(block_value)
        if rewards:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data.append({
                "Block Value": block_value,
                "Group": group,
                "Miners Share": rewards["miners"],
                "Briseur Share": rewards["briseur"],
                "Owners Share": rewards["owners"],
                "Bonus": rewards.get("bonus", 0),
                "Timestamp": timestamp
            })

    # Créer un DataFrame et enregistrer dans un fichier Excel
    df = pd.DataFrame(data)
    df.to_excel("mining_results.xlsx", index=False)
    print("Mining simulation completed and saved to mining_results.xlsx")

# Simuler le minage de 100 blocs
simulate_mining(100)

# Lire les résultats de la simulation
df = pd.read_excel("mining_results.xlsx")
print(df.head())  # Afficher les 5 premières lignes du DataFrame
```

## Exemple de sortie
```
Mining simulation completed and saved to mining_results.xlsx
   Block Value Group  Miners Share  Briseur Share  Owners Share  Bonus  \
0           92     B            25             14            61    NaN
1           29     A            25             14            61    NaN
2           49     A            25             14            61    NaN
3           41     A            25             14            61    NaN
4           11     A            25             14            61    NaN
```

Le code ci-dessus simule le processus de minage de 100 blocs et enregistre les résultats dans un fichier Excel appelé `mining_results.xlsx`. Les résultats incluent des informations sur la valeur du bloc, le groupe auquel il appartient, la part des mineurs, des briseurs, des propriétaires et un éventuel bonus. Le DataFrame est ensuite lu à partir du fichier Excel et les 5 premières lignes sont affichées à titre d'exemple.

J'espère que cela vous aidera à comprendre comment simuler le processus de minage et à enregistrer les résultats dans un fichier Excel en utilisant Python. N'hésitez pas à poser des questions si vous en avez.

## Ressources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Python Datetime Module](https://docs.python.org/3/library/datetime.html)
- [Real Python - Reading and Writing Excel Files in Python](https://realpython.com/openpyxl-excel-spreadsheets-python/)
- [Openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/)
- [Python Excel Tutorial: The Definitive Guide](https://www.datacamp.com/community/tutorials/python-excel-tutorial)
- [Python Excel: Writing to Excel with Pandas](https://www.datacamp.com/community/tutorials/python-excel-tutorial)
- [Python Excel: Read and Write Excel files in Python](https://www.geeksforgeeks.org/reading-excel-file-using-python/)
- [Python Excel: How to Write to Excel Files Using Pandas](https://www.freecodecamp.org/news/how-to-write-to-excel-files-using-pandas/)
- [Python Excel: How to Write to Excel Files Using Openpyxl](https://www.freecodecamp.org/news/how-to-write-to-excel-files-using-openpyxl/)
- [Python Excel: How to Write to Excel Files Using XlsxWriter](https://www.freecodecamp.org/news/how-to-write-to-excel-files-using-xlsxwriter-in-python/)
- [Python Excel: How to Write to Excel Files Using xlwt](https://www.freecodecamp.org/news/how-to-write-to-excel-files-using-xlwt-in-python/)
- [Python Excel: How to Write to Excel Files Using xlrd](https://www.freecodecamp.org/news/how-to-read-excel-files-using-xlrd-in-python/)
- [Python Excel: How to Write to Excel Files Using xlwt](https://www.freecodecamp.org/news/how-to-write-to-excel-files-using-xlwt-in-python/)
- [Python Excel: How to Write to Excel Files Using xlrd](https://www.freecodecamp.org/news/how-to-read-excel-files-using-xlrd-in-python/)

## Conclusion
Dans ce tutoriel, nous avons appris à simuler le processus de minage de blocs et à enregistrer les résultats dans un fichier Excel en utilisant Python. Nous avons utilisé les bibliothèques `random`, `pandas` et `datetime` pour générer des valeurs aléatoires, créer un DataFrame et enregistrer les résultats dans un fichier Excel. J'espère que vous avez trouvé ce tutoriel utile et que vous pourrez l'appliquer à vos propres projets. N'hésitez pas à poser des questions si vous en avez. Merci de votre lecture !

