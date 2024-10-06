import pandas as pd
import numpy as np

def construct_rfms(df):
    # Ensure TransactionStartTime is timezone-naive
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime']).dt.tz_localize(None)
    
    # Recency: Time since the user's last transaction
    current_time = pd.to_datetime('today').tz_localize(None)  # Ensure current time is also timezone-naive
    df['Recency'] = df.groupby('CustomerId')['TransactionStartTime'].transform(lambda x: (current_time - x.max()).days)
    
    # Frequency: Number of transactions per user
    df['Frequency'] = df.groupby('CustomerId')['TransactionId'].transform('count')
    
    # Monetary: Total amount spent per user
    df['Monetary'] = df.groupby('CustomerId')['Amount'].transform('sum')
    
    # Optional Seasonality: Add seasonal behavior based on month, if required
    df['TransactionMonth'] = pd.to_datetime(df['TransactionStartTime']).dt.month
    df['Seasonality'] = df.groupby('CustomerId')['TransactionMonth'].transform(lambda x: x.mode()[0])
    
    # Normalize features to build RFMS score
    df['RFMS_Score'] = (df['Recency'] + df['Frequency'] + df['Monetary']) / 3
    return df
def classify_users(df, threshold=50):
    df['UserCategory'] = np.where(df['RFMS_Score'] > threshold, 'Good', 'Bad')
    return df


   