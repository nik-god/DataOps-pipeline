# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Ensure the .kaggle directory exists and copy the kaggle.json file
RUN mkdir -p /root/.kaggle
COPY kaggle.json /root/.kaggle/kaggle.json
RUN chmod 600 /root/.kaggle/kaggle.json

# Install curl and any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Run the dataset download and preprocessing script
RUN python scripts/preprocess_data.py

# Expose port 8080 for the Dash app
EXPOSE 8080

# Run the application
CMD ["python", "sales.py"]
