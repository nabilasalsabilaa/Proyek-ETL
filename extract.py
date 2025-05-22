import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

def extract_data():
    all_items = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for page in range(1, 51): 
        url = "https://fashion-studio.dicoding.dev/" if page == 1 else f"https://fashion-studio.dicoding.dev/page{page}"
        print(f"Mengakses: {url}")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"Gagal mengakses halaman {page}: {err}")
            continue  

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="collection-card")  

        if not cards:
            print(f"Tidak ada produk ditemukan di halaman {page}")
            continue

        for card in cards:
            title = card.find("h3", class_="product-title")
            price = card.find("div", class_="price-container")
            rating = card.find("p", string=lambda t: t and "Rating" in t)
            colors = card.find("p", string=lambda t: t and "Colors" in t)
            size = card.find("p", string=lambda t: t and "Size" in t)
            gender = card.find("p", string=lambda t: t and "Gender" in t)

            produk = {
                "title": title.text.strip() if title else "Unknown Title",
                "price": price.text.strip() if price else "Price Not Available",
                "rating": rating.text.strip() if rating else "No Rating",
                "colors": colors.text.strip() if colors else "No Color Info",
                "size": size.text.strip() if size else "No Size Info",
                "gender": gender.text.strip() if gender else "No Gender Info",
                "timestamp": timestamp  
            }

            all_items.append(produk)

        print(f"Halaman {page}: {len(cards)} produk ditambahkan.")

    return all_items, timestamp


if __name__ == "__main__":
    data, timestamp = extract_data()
    print(f"\nTotal produk terkumpul: {len(data)}")

    filename = f"products.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "price", "rating", "colors", "size", "gender", "timestamp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data berhasil disimpan ke {filename}")