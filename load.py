import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from sqlalchemy import create_engine  

def save_to_csv(df, filename='products_clean.csv'):
    try:
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan ke CSV: {e}")

def save_to_google_sheets(df, creds_json='google-sheets-api.json', sheet_name='Products'):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(creds_json, scopes=scopes)
        client = gspread.authorize(creds)

        spreadsheet = client.open(sheet_name)
        sheet = spreadsheet.sheet1
        sheet.clear()

        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Data berhasil disimpan ke Google Sheets.")
    except Exception as e:
        print(f"Gagal menyimpan ke Google Sheets: {e}")