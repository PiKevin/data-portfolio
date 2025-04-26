# This script extracts data from the SpaceX API and saves it to a CSV file.
import requests
import json
import os

# Get the current directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")

# Create the data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Define the URL for the SpaceX API endpoint
url = "https://api.spacexdata.com/v4/launches"

# Make a GET request to the API 
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Save the raw data as a JSON file
    file_path = os.path.join(data_dir, "spacex_launches_raw.json")    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Data extracted and saved to {file_path}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")