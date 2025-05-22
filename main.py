from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv  

def main():
    print("Start extracting data...")
    raw_data, timestamp = extract_data()  

    print("Start transforming data...")
    clean_data = transform_data(raw_data)

    print("Start loading data to CSV...")
    save_to_csv(clean_data)

if __name__ == "__main__":
    main()