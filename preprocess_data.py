import kaggle
import pandas as pd
import os

# Step 1: Download the Dataset from Kaggle
dataset = 'nikbond/onlinesales'
destination = './data'

# Ensure the destination directory exists
if not os.path.exists(destination):
    os.makedirs(destination)

# Download and unzip the dataset
kaggle.api.dataset_download_files(dataset, path=destination, unzip=True)

# Load the dataset
file_path = os.path.join(destination, 'OnlineSales.csv')
df = pd.read_csv(file_path)

# Show the number of rows in the original dataset
print(f"Number of rows in the original dataset: {len(df)}")

# Step 2: Preprocess and Clean the Data
df.dropna(subset=['Country'], inplace=True)  # Drop rows with missing country values
df = df[df['Country'].str.lower() != 'unspecified']  # Drop rows where the country is 'Unspecified'

# Clean up the Totalsale column
def clean_totalsale(value):
    if isinstance(value, str):
        return float(value.replace(',', ''))
    return value

df['Totalsale'] = df['Totalsale'].apply(clean_totalsale)

# Show the number of rows after cleaning the data
print(f"Number of rows after cleaning the data: {len(df)}")

# Save the cleaned data
cleaned_data_path = os.path.join(destination, 'cleaned_OnlineSales.csv')
df.to_csv(cleaned_data_path, index=False)

# Analysis: Sales by Country
sales_by_country = df.groupby('Country')['Totalsale'].sum().reset_index()

# Analysis: Maximum Selling Products
max_selling_products = df.groupby('Product')['Totalsale'].sum().reset_index().sort_values(by='Totalsale', ascending=False)

# Save the analysis results
sales_by_country.to_csv(os.path.join(destination, 'sales_by_country.csv'), index=False)
max_selling_products.to_csv(os.path.join(destination, 'max_selling_products.csv'), index=False)
