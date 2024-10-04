import pandas as pd

# Function to display basic data structure and info
def dataset_overview(df):
    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])
    print("\nData Types:\n", df.dtypes)
    print("\nMissing values per column:\n", df.isnull().sum())

# Function for summary statistics
def summary_statistics(df):
    print("\nSummary Statistics:\n")
    return df.describe()

# Function to identify missing values
def missing_values(df):
    missing = df.isnull().sum().sort_values(ascending=False)
    print("\nMissing Values in Dataset:\n", missing[missing > 0])

# Main function to call the dataset overview, summary statistics, and missing values check
def run_data_overview(df):
    dataset_overview(df)
    print(summary_statistics(df))
    missing_values(df)
