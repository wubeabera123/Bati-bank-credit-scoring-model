import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# Function to visualize distribution of numerical features
def plot_numerical_distributions(df, num_cols=None):
    if num_cols is None:
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns[:5]  # Limiting to 5 columns by default
    df[num_cols].hist(figsize=(10, 8), bins=15)  # Reduce bins for faster plotting
    plt.tight_layout()
    plt.show()

# Function to visualize distribution of categorical features
def plot_categorical_distributions(df, cat_cols=None):
    if cat_cols is None:
        cat_cols = df.select_dtypes(include=['object']).columns[:5]  # Limiting to 5 columns by default
    
    n = len(cat_cols)
    rows = (n // 3) + 1 if n % 3 != 0 else n // 3
    
    plt.figure(figsize=(10, 8))
    for i, col in enumerate(cat_cols, 1):
        plt.subplot(rows, 3, i)
        sns.countplot(y=df[col], palette="Set2")
        plt.title(f"Count plot of {col}")
    plt.tight_layout()
    plt.show()

# Function for correlation analysis
def correlation_analysis(df):
    corr_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(8, 6))  # Smaller figure for faster plotting
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', linewidths=0.5)  # Set annot=False to speed up
    plt.title("Correlation Matrix")
    plt.show()

# Function to identify missing values
def missing_values(df):
    missing = df.isnull().sum().sort_values(ascending=False)
    print("\nMissing Values in Dataset:\n", missing[missing > 0])

# Function to detect outliers using box plots
def outlier_detection(df, num_cols=None):
    if num_cols is None:
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns[:5]  # Limiting to 5 columns by default
    
    n = len(num_cols)
    rows = (n // 3) + 1 if n % 3 != 0 else n // 3

    plt.figure(figsize=(10, 8))  # Reduce figure size
    for i, col in enumerate(num_cols, 1):
        plt.subplot(rows, 3, i)
        sns.boxplot(df[col])
        plt.title(f"Box plot of {col}")
    plt.tight_layout()
    plt.show()

# Function to run the full data analysis pipeline
def run_data_analysis_pipeline(df):
    dataset_overview(df)
    print(summary_statistics(df))
    plot_numerical_distributions(df)
    plot_categorical_distributions(df)
    correlation_analysis(df)
    missing_values(df)
    outlier_detection(df)
