# Importation des modules
from bs4 import BeautifulSoup
import requests
import csv

def scrape_books(url):
    # Envoyer une requête HTTP GET pour récupérer le contenu de la page
    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur :", response.status_code)
        return {}

    # Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Dictionnaire pour stocker les résultats
    books = {}

    # Tous les livres sont contenus dans des <article class="product_pod">
    for article in soup.find_all("article", class_="product_pod"):
        # Récupérer le titre depuis le <a> dans <h3>
        a_tag = article.find("h3").find("a")
        title = a_tag.get("title") if a_tag else None

        # Récupérer le prix depuis <p class="price_color">
        price_tag = article.find("p", class_="price_color")
        price = price_tag.get_text().strip().replace("Â", "") if price_tag else None

        # Ajouter au dictionnaire si titre et prix existent
        if title and price:
            books[title] = price

    return books

# Exemple d'utilisation
url = "https://books.toscrape.com/"
books_data = scrape_books(url)

# Afficher les résultats
for title, price in books_data.items():
    print(f"{title} → {price}")

# Exporter les résultats vers un fichier CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    for title, price in books_data.items():
        writer.writerow([title, price])

print("Les données ont été exportées dans books.csv")