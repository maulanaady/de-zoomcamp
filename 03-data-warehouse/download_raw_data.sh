#!/bin/bash

# Read each URL from raw_data_urls.txt
while IFS= read -r url; do
    # Extract the filename from the URL
    filename=$(basename "$url")
    
    # Use wget to download the file
    wget "$url" -O "$filename"
    
    # Use gsutil to copy the downloaded file to Google Cloud Storage
    gsutil cp "$filename" gs://terraform_zoomcamp_data/ny_taxi_dbt/
    
    # Remove the downloaded file after uploading
    rm "$filename"
done < raw_data_urls.txt
