import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Step 1: Download the Dataset from Kaggle
dataset = 'nikbond/onlinesales'
destination = './data/OnlineSales.csv'
os.makedirs('./data', exist_ok=True)

api = KaggleApi()
api.authenticate()
api.dataset_download_file(dataset, file_name='OnlineSales.csv', path='./data')

# Step 2: Load the Data
df = pd.read_csv(destination)

# Step 3: Data Cleanup
df.dropna(subset=['Country'], inplace=True)
df = df[df['Country'].str.lower() != 'unspecified']

# Save the cleaned data
df.to_csv(destination, index=False)

# Print number of rows before and after cleanup
print(f"Number of rows before cleanup: {len(df) + df.isnull().sum().sum()}")
print(f"Number of rows after cleanup: {len(df)}")
