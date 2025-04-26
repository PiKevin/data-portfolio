import pandas as pd
import json
import os

# Locate raw JSON file
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
input_path = os.path.join(data_dir, "spacex_launches_raw.json")
output_path = os.path.join(data_dir, "spacex_launches_cleaned.csv")

# Load the raw JSON data
with open(input_path, "r") as file:
    raw_data = json.load(file)

if isinstance(raw_data, list):
    launches = raw_data
else:
    launches = [raw_data] # Handle the case where the JSON data is not a list

cleaned = []
for launch in launches:
    # Extract relevant fields
    cleaned_launch = {
        "name": launch.get("name"),
        "date_utc": launch.get("date_utc"),
        "success": launch.get("success"),
        "details": launch.get("details"),
        "rocket": launch.get("rocket"),
    }
    cleaned.append(cleaned_launch)

# Convert to DataFrame
df = pd.DataFrame(cleaned)

df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")