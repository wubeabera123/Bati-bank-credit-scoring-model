# Bati-bank-credit-scoring-model

Project Overview:

This project aims to build a credit scoring model for Bati Bank using eCommerce transaction data. The goal is to predict customer creditworthiness based on transactional and customer-specific features, enabling the bank to make informed lending decisions. The project follows a comprehensive data pipeline that includes data preprocessing, exploration, feature engineering, model development, and evaluation.

Contents of this Repository:

Dataset Overview
Data Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Development
Model Evaluation
Recommendations
Convergence Warning Fix
Further Model Improvements
1. Dataset Overview:

The dataset contains eCommerce transaction records, which include the following types of data:

Transaction-specific Attributes: TransactionId, BatchId, AccountId, Amount, Value, TransactionStartTime.
Customer-specific Attributes: CustomerId, CountryCode, CurrencyCode.
Product-related Attributes: ProductCategory, ProviderId, ChannelId.

2. Data Preprocessing:

Objective: Clean and prepare the dataset for modeling by addressing missing values, duplicate records, and irrelevant columns.
Key Steps:
Missing Values: Columns like CountryCode and ProviderId contained missing data. These were either imputed or dropped, depending on their importance to the analysis.
Unnamed Columns: Some columns without meaningful names were removed.
Duplicate Records: The dataset was checked for duplicates to ensure consistency.
Data Types: Corrected any discrepancies in data types to ensure compatibility for analysis (e.g., converting string representations of numbers to numeric types).

3. Exploratory Data Analysis (EDA):

Objective: Gain insights into the dataset's structure and feature relationships.
Key Steps:
Summary Statistics: Generated for numerical columns like Amount, Value, showing their central tendencies, spread, and variability.
Visualizations: Histograms, box plots, and count plots for both numerical and categorical variables. These helped to visualize data distribution and identify any skewness, missing values, or outliers.
Correlation Matrix: A correlation analysis was performed to understand relationships between numerical variables, such as Amount and Value.
Outlier Detection: Boxplots were used to identify potential outliers in transaction-related fields, which could influence model performance.

4. Feature Engineering:

Objective: Create new features and transform the dataset to better capture customer behavior and enhance the model's predictive power.
Key Features Created:
RFMS Score: A combination of Recency, Frequency, Monetary Value, and Seasonality (RFMS) was calculated for each customer, capturing their transaction behavior over time.
Categorical Encoding: Categorical features such as ProductCategory, CurrencyCode, and CountryCode were encoded using techniques like One-Hot Encoding or Label Encoding.

5. Model Development:

Objective: Train machine learning models to predict customer creditworthiness (good vs. bad customers).
Models Implemented:
Logistic Regression:
Simple, interpretable model but encountered convergence issues due to the large dataset size.
Achieved accuracy of 97.38% and an AUC score of 0.9945.
Random Forest:
Complex, high-performing model that achieved accuracy of 99.62% and an AUC score of 0.9998.
Outperformed Logistic Regression and did not suffer from convergence issues.

6. Model Evaluation:

Confusion Matrix and Classification Reports were generated for both models:
Logistic Regression:
Precision: 0.97 (Bad), 0.98 (Good).
Recall: 0.98 (Bad), 0.97 (Good).
Random Forest:
Precision: 0.99 (Bad), 1.00 (Good).
Recall: 1.00 (Bad), 0.99 (Good).
Insights:
Random Forest performed exceptionally well but may risk overfitting due to its near-perfect scores.
Logistic Regression encountered convergence issues, and it could benefit from further tuning, such as increasing the number of iterations or adjusting the solver.

7. Recommendations:

Model Selection:

Use Random Forest as the primary model due to its high accuracy and AUC score.
Perform cross-validation to ensure the model generalizes well on unseen data.
Hyperparameter Tuning:

For Logistic Regression, consider increasing the max_iter parameter or using an alternative solver.
For Random Forest, fine-tune hyperparameters such as the number of estimators and tree depth.
Handling Data at Scale:

Apply data scaling methods such as Standardization or MinMax Scaling to improve model performance and avoid convergence warnings.
Outlier Treatment:

Address outliers, especially in monetary columns, by capping or other outlier-handling techniques.
Model Interpretability:

Despite Random Forest’s strong performance, its complexity might make deployment challenging. Consider using simpler models for real-time predictions.

8. Convergence Warning Fix:

Logistic Regression encountered convergence warnings. The warning can be fixed by:
Increasing max_iter: Increase the number of iterations to give the model more time to converge.
Alternative Solver: Consider switching to another solver like 'saga' or 'liblinear', which may be more appropriate for large datasets.

9. Further Model Improvements:

Cross-Validation:
Implement cross-validation to validate model performance across different subsets of the data.
Deployability:
While Random Forest shows exceptional results, ensure that model deployment (memory, speed) is feasible for production use, especially if real-time scoring is required.
Instructions to Run the Project:
Clone the repository:

git clone https://github.com/your-username/bati-bank-credit-scoring-model.git
Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Load and clean the dataset:

Run the data_preprocessing.py script to load, clean, and preprocess the dataset.
Run the Exploratory Data Analysis (EDA):

Use the eda.py script to explore the dataset and generate visualizations.
Train and evaluate the models:

Use the model_training.py script to train and evaluate both Logistic Regression and Random Forest models.
Generate the final report:

The final report summarizing model performance, insights, and recommendations can be found in the report.pdf file.
Dependencies:

Python 3.8+
pandas
numpy
matplotlib
seaborn
scikit-learn
openpyxl
fastapi
