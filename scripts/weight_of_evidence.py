import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np

def woe_binning(df, target_column, variable, n_bins=5):
    # Convert target_column and variable to numeric (if not already)
    df[target_column] = pd.to_numeric(df[target_column], errors='coerce')
    df[variable] = pd.to_numeric(df[variable], errors='coerce')

    # Drop rows where conversion failed (NaN values)
    df.dropna(subset=[target_column, variable], inplace=True)

    # Check if any rows are left after cleaning
    if df.empty:
        raise ValueError(f"No valid data available after cleaning '{variable}' and '{target_column}' columns.")

    # Use KBinsDiscretizer to create bins for the variable
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='uniform')
    
    # Check if there are enough samples to apply binning
    if df[[variable]].shape[0] < n_bins:
        raise ValueError(f"Not enough valid samples for binning. Found {df[[variable]].shape[0]}, but need at least {n_bins}.")
    
    df[f'{variable}_bin'] = discretizer.fit_transform(df[[variable]])

    # Calculate WoE
    binned_data = df.groupby(f'{variable}_bin')[target_column].agg(['count', 'sum'])
    binned_data['good'] = binned_data['count'] - binned_data['sum']  # Number of good cases
    binned_data['bad'] = binned_data['sum']  # Number of bad cases
    
    # Avoid division by zero by adding a small constant to 'good' and 'bad'
    binned_data['good_dist'] = binned_data['good'] / (binned_data['good'].sum() + 1e-10)
    binned_data['bad_dist'] = binned_data['bad'] / (binned_data['bad'].sum() + 1e-10)
    
    # Calculate WoE values
    binned_data['WoE'] = np.log(binned_data['good_dist'] / binned_data['bad_dist'])
    
    # Merge WoE values back to the original dataframe
    woe_mapping = binned_data['WoE'].to_dict()
    df[f'{variable}_WoE'] = df[f'{variable}_bin'].map(woe_mapping)
    
    return df
