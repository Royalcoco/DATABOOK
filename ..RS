import datetime

date_str = input("Entrez une date au format JJ/MM/AAAA : ")
date = datetime.datetime.strptime(date_str, "%d/%m/%Y")

print("La date que vous avez entrée est :", date)
# Format the date in three levels
formatted_date = date.strftime("%d %B %Y")
print("Formatted date (Level 1):", formatted_date)

formatted_date = date.strftime("%A, %d %B %Y")
print("Formatted date (Level 2):", formatted_date)

formatted_date = date.strftime("%A, %d %B %Y %H:%M:%S")
print("Formatted date (Level 3):", formatted_date)
# Exchange dates with NFT
nft_date = date.strftime("%Y-%m-%d")
print("NFT date:", nft_date)
# Create another date
another_date_str = input("Entrez une autre date au format JJ/MM/AAAA : ")
another_date = datetime.datetime.strptime(another_date_str, "%d/%m/%Y")

# Compare the dates
if date < another_date:
    print("La première date est antérieure à la deuxième date.")
elif date > another_date:
    print("La première date est postérieure à la deuxième date.")
else:
    print("Les deux dates sont identiques.")
    
# Exchange dates with NFT
another_nft_date = another_date.strftime("%Y-%m-%d")
print("NFT date (another date):", another_nft_date)
# Calculate the difference between the two dates
difference = another_date - date

print("La différence entre les deux dates est de", difference.days, "jours.")

# Calculate the difference between the two dates in years
years = difference.days // 365
print("La différence entre les deux dates est de", years, "ans.")

# Calculate the difference between the two dates in months
months = difference.days // 30
print("La différence entre les deux dates est de", months, "mois.")

# Calculate the weight of the NFT for navigating different URLs
nft_weight = len(nft_date) + len(another_nft_date)
print("The weight of the NFT for navigating different URLs is:", nft_weight)

# Calculate the weight of the NFT for navigating different URLs
nft_weight = len(nft_date) + len(another_nft_date)
print("The weight of the NFT for navigating different URLs is:", nft_weight)

# Define the URLs for the blockchain
blockchain_urls = [
    "https://blockchain1.com",
    "https://blockchain2.com",
    "https://blockchain3.com"
]

# Create a blockchain based on the dates
blockchain = []
for url in blockchain_urls:
    blockchain.append(url + "/" + nft_date)

# Print the blockchain
print("Blockchain:")
for block in blockchain:
    print(block)
    
# Create a blockchain based on the dates
blockchain = []
for url in blockchain_urls:
    blockchain.append(url + "/" + another_nft_date)
    
