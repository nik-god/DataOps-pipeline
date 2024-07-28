# scripts/preprocess_data.py

import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_data():
    dataset = 'nikbond/onlinesales'
    destination = './data'
    if not os.path.exists(destination):
        os.makedirs(destination)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(dataset, 'OnlineSales.csv', path=destination)
    print("Dataset downloaded successfully.")

def preprocess_data():
    file_path = './data/OnlineSales.csv'
    df = pd.read_csv(file_path)

    # Clean up the data
    initial_row_count = len(df)
    df = df[df['Country'].notna()]
    df = df[df['Country'].str.lower() != 'unspecified']
    final_row_count = len(df)

    print(f"Initial number of rows: {initial_row_count}")
    print(f"Number of rows after cleanup: {final_row_count}")

    df.to_csv(file_path, index=False)
    print("Data preprocessed and saved successfully.")

if __name__ == "__main__":
    download_kaggle_data()
    preprocess_data()
