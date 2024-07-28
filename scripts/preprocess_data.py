import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Step 1: Download the Dataset from Kaggle
dataset = 'nikbond/onlinesales'
destination = './data'

# Create the data directory if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset, path=destination, unzip=True)

# Load the dataset
file_path = os.path.join(destination, 'OnlineSales.csv')
data = pd.read_csv(file_path)

# Step 2: Data Cleaning
# Drop rows where the country is not specified or is 'Unspecified'
data = data[data['Country'].notna()]
data = data[data['Country'] != 'Unspecified']

# Step 3: Save the cleaned data
cleaned_file_path = os.path.join(destination, 'CleanedOnlineSales.csv')
data.to_csv(cleaned_file_path, index=False)

print(f"Original rows: {len(data)}")
print(f"Cleaned rows: {len(data)}")
