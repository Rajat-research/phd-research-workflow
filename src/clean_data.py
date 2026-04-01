import pandas as pd

# Load dataset
data = pd.read_csv('data/sample_data.csv')

# Display missing values
print("Missing values before cleaning:\n", data.isnull().sum())

# Fill missing numeric values with mean
data.fillna(data.mean(numeric_only=True), inplace=True)

# Save cleaned data
data.to_csv('data/cleaned_data.csv', index=False)

print("Cleaned data saved as data/cleaned_data.csv")