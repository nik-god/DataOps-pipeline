import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_data():
    api = KaggleApi()
    api.authenticate()
    
    # Dataset details
    dataset_name = 'nikbond/onlinesales'
    file_name = 'OnlineSales.csv'
    
    # Directory to save the dataset
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    
    # Download dataset
    api.dataset_download_file(dataset_name, file_name, path=data_dir, force=True)
    
    # Unzip the downloaded file
    file_path = os.path.join(data_dir, file_name + '.zip')
    if os.path.exists(file_path):
        import zipfile
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        os.remove(file_path)
    
    print(f'Dataset downloaded and extracted to {data_dir}/{file_name}')
    return os.path.join(data_dir, file_name)

def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Initial row count
    initial_rows = df.shape[0]
    print(f'Initial row count: {initial_rows}')
    
    # Drop rows where 'Country' is NaN or 'Unspecified'
    df.dropna(subset=['Country'], inplace=True)
    df = df[df['Country'].str.lower() != 'unspecified']
    
    # Final row count
    final_rows = df.shape[0]
    print(f'Final row count after cleaning: {final_rows}')
    
    # Save the cleaned data
    df.to_csv(file_path, index=False)
    print(f'Cleaned data saved to {file_path}')

if __name__ == '__main__':
    file_path = download_kaggle_data()
    preprocess_data(file_path)
