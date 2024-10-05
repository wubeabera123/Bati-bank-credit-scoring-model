import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Function 1: Create Aggregate Features
def create_aggregate_features(df):
    # Total Transaction Amount per Customer
    df['Total_Transaction_Amount'] = df.groupby('CustomerId')['Amount'].transform('sum')
    
    # Average Transaction Amount per Customer
    df['Average_Transaction_Amount'] = df.groupby('CustomerId')['Amount'].transform('mean')
    
    # Transaction Count per Customer
    df['Transaction_Count'] = df.groupby('CustomerId')['TransactionId'].transform('count')
    
    # Standard Deviation of Transaction Amounts per Customer
    df['Transaction_Amount_Std'] = df.groupby('CustomerId')['Amount'].transform('std')
    
    return df

# Function 2: Extract Features
def extract_time_features(df):
    # Convert TransactionStartTime to datetime
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])
    
    # Extract hour, day, month, and year from the transaction timestamp
    df['Transaction_Hour'] = df['TransactionStartTime'].dt.hour
    df['Transaction_Day'] = df['TransactionStartTime'].dt.day
    df['Transaction_Month'] = df['TransactionStartTime'].dt.month
    df['Transaction_Year'] = df['TransactionStartTime'].dt.year
    
    return df

# Function 3: Encode Categorical Variables
def encode_categorical_features(df):
    # Label Encoding for categorical columns
    label_cols = ['CustomerId', 'ProviderId', 'ProductId', 'ChannelId', 'CurrencyCode']
    for col in label_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
    
    # One-Hot Encoding
    df = pd.get_dummies(df, columns=['ProductCategory'], drop_first=True)
    
    return df

# Function 4: Handle Missing Values
def handle_missing_values(df):
    # Imputation for missing values in numerical columns
    df['Amount'].fillna(df['Amount'].mean(), inplace=True)
    df['Transaction_Amount_Std'].fillna(df['Transaction_Amount_Std'].mean(), inplace=True)
    
    # Removal of rows with missing categorical data
    df.dropna(subset=['ProviderId', 'ProductId', 'CountryCode'], inplace=True)
    
    return df

# Function 5: Normalize/Standardize Numerical Features
def scale_numerical_features(df, method='standardization'):
    scaler = None
    num_cols = ['Amount', 'Total_Transaction_Amount', 'Average_Transaction_Amount', 'Transaction_Amount_Std']
    
    if method == 'standardization':
        scaler = StandardScaler()
    elif method == 'normalization':
        scaler = MinMaxScaler()
    
    if scaler:
        df[num_cols] = scaler.fit_transform(df[num_cols])
    
    return df

# Main Function: Run All Feature Engineering Steps
def run_feature_engineering(df):
    df = create_aggregate_features(df)
    df = extract_time_features(df)
    df = encode_categorical_features(df)
    df = handle_missing_values(df)
    df = scale_numerical_features(df, method='standardization')
    
    return df
