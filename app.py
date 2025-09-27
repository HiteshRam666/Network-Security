import os
import sys 
# import certifi 
# ca = certifi.where() 
from mlflow.entities import Expectation
import pymongo 
import pandas as pd 
from network_security.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME, DATA_INGESTION_DATABASE_NAME
from network_security.logging.logger import logging 
from network_security.exception.exception import NetworkSecurityException 
from network_security.pipeline.training_pipeline import TrainingPipeline
from network_security.utils.main_utils.utils import load_object

from fastapi import FastAPI, File, UploadFile, Request 
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run
from dotenv import load_dotenv

from network_security.utils.ml_utils.model.estimator import NetworkModel 
load_dotenv() 

mongodb_url = os.getenv("MONGODB_URL_KEY")

client = pymongo.MongoClient(mongodb_url)

database = client[DATA_INGESTION_DATABASE_NAME] 
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI() 
origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials= True, 
    allow_methods = ["*"], 
    allow_headers = ["*"]
)

templates = Jinja2Templates(directory="./templates") 

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url = "/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is Successful") 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.post("/predict")
async def predict_route(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        preprocessor = load_object("final_models/preprocessor.pkl")
        final_model = load_object("final_models/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model = final_model)
        print(df.iloc[0])
        y_pred = network_model.predict(df)
        print(y_pred)
        df["predicted_column"] = y_pred 
        print(df["predicted_column"])

        os.makedirs("predicted_data", exist_ok=True)
        output_file = f"predicted_data/output_{file.filename}"
        df.to_csv(output_file, index = False)

        return FileResponse(output_file, filename=f"predictions_{file.filename}")
    except Expectation as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    app_run(app, host="localhost", port = 8000)