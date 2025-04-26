import pandas as pd

# Load the data
df = pd.read_csv("U.S._Chronic_Disease_Indicators.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop completely empty rows
df.dropna(how='all', inplace=True)

# Optional: Drop columns with too many nulls
threshold = 0.5  # If more than 50% of values are missing
df = df.loc[:, df.isnull().mean() < threshold]

# Save cleaned version
df.to_csv("U.S._Chronic_Disease_Indicators_Cleaned.csv", index=False)