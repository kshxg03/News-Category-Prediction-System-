from fastapi import FastAPI
import joblib
from src.schemas.response import ModelOutput
from src.utils.utility import preprocess_text
from src.schemas.request import ModelInput

app = FastAPI()

label_encoder = joblib.load(
    r"C:\ML_Final_Project\backend\src\models\label_encoder.pkl"
)

pipeline = joblib.load(
    r"C:\ML_Final_Project\backend\src\models\knn_model.pkl"
)

@app.get("/")
async def root():
    return {"status": "Healthy"}

@app.post("/predict")
async def predict(data: ModelInput):
    cleaned_text = preprocess_text(data.text)
    prediction_output = pipeline.predict([cleaned_text])[0]
    prediciton = label_encoder.inverse_transform([prediction_output])[0]
    return ModelOutput(category = prediciton)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)