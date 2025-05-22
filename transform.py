import pandas as pd
import re

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Bersihkan data dengan menghapus duplikat & null
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Hilangkan data invalid
    df = df[~df['title'].str.contains("Unknown", case=False)]

    # Konversi Price dari string USD ke angka Rupiah
    def convert_price(price_str):
        try:
            number = float(re.findall(r"\d+\.?\d*", price_str)[0])
            return number * 16000
        except (IndexError, ValueError):
            return None

    df['price'] = df['price'].apply(convert_price)

    # Hapus baris yang price nya None setelah konversi
    df = df[df['price'].notnull()]

    # Konversi rating dari "4.8 / 5" ke float 4.8, hapus text "Rating: "
    def convert_rating(rating_str):
        try:
            match = re.search(r"(\d+\.?\d*)", rating_str)
            return float(match.group(1)) if match else None
        except Exception:
            return None

    df['rating'] = df['rating'].apply(convert_rating)

    # Konversi Colors dari "3 Colors" jadi angka 3
    df['colors'] = df['colors'].apply(lambda x: int(re.findall(r"\d+", x)[0]) if re.findall(r"\d+", x) else 0)

    # Bersihkan Size dan Gender
    df['size'] = df['size'].str.replace(r"Size:\s*", "", regex=True).astype(str)
    df['gender'] = df['gender'].str.replace(r"Gender:\s*", "", regex=True).astype(str)

    df.dropna(inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df