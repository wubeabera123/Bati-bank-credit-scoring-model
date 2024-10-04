import seaborn as sns
import matplotlib.pyplot as plt

# Function to visualize distribution of numerical features
def plot_numerical_distributions(df, num_cols=None):
    if num_cols is None:
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns[:3]  # Limiting to 3 columns by default
    if len(num_cols) > 0:
        df[num_cols].sample(frac=0.2).hist(figsize=(10, 8), bins=10)  # Reduce bins & sample 20% of the data for faster plotting
        plt.tight_layout()
        plt.show()
    else:
        print("No numerical columns found for plotting.")

# Function to visualize distribution of categorical features
def plot_categorical_distributions(df, cat_cols=None):
    if cat_cols is None:
        cat_cols = df.select_dtypes(include=['object']).columns[:3]  # Limiting to 3 columns by default
    
    if len(cat_cols) > 0:
        n = len(cat_cols)
        rows = (n // 2) + 1 if n % 2 != 0 else n // 2
        
        plt.figure(figsize=(10, 6))
        for i, col in enumerate(cat_cols, 1):
            top_categories = df[col].value_counts().index[:10]  # Top 10 categories
            sns.countplot(y=df[col], order=top_categories, palette="Set2")  # Plot with 'order' for top 10 categories
            plt.title(f"Top 10 categories of {col}")
        plt.tight_layout()
        plt.show()
    else:
        print("No categorical columns found for plotting.")

# Main function to call both visualizations
def run_data_visualization(df):
    print("Visualizing numerical distributions...")
    plot_numerical_distributions(df)
    print("Visualizing categorical distributions...")
    plot_categorical_distributions(df)
