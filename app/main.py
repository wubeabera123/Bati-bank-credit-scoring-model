# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import numpy as np
import joblib
 
app = FastAPI()
 
# Load your trained model

model_path = os.path.join(os.path.dirname(__file__), '../notebooks/best_model.pkl')
model = joblib.load(model_path)
 
# Define the input data model
class InputFeatures(BaseModel):
    features: list  # Assuming your features are passed as a list
 
@app.post('/predict/')
async def predict(input_data: InputFeatures):
    # Convert the input data into a numpy array
    input_features = np.array(input_data.features).reshape(1, -1)  # Adjust based on your feature set
 
    # Make predictions using the loaded model
    try:
        prediction = model.predict(input_features)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")
 
    return {
        "Prediction": prediction[0].tolist(),
    }
 
# Run the FastAPI application
# To run the app, use: uvicorn app:app --reload