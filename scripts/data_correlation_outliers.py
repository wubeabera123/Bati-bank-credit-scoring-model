import seaborn as sns
import matplotlib.pyplot as plt

# Function for correlation analysis
def correlation_analysis(df):
    corr_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(8, 6))  # Smaller figure for faster plotting
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', linewidths=0.5)  # Set annot=False to speed up
    plt.title("Correlation Matrix")
    plt.show()

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

# Main function to run correlation analysis and outlier detection
def run_correlation_outliers(df):
    correlation_analysis(df)
    outlier_detection(df)
