# Network Security (Phishing Attacks) ML System ☢️

A production-ready Network Security ML system that ingests network/phishing data from MongoDB, validates and transforms it, trains a classification model with MLflow tracking, and serves batch predictions via a FastAPI service. The training pipeline orchestrates sequential stages—data ingestion, validation, transformation, and model training—then syncs both artifacts and final models to S3 and a deployed Docker image using ECR to EC2 via GitHub Actions CI/CD. The API exposes endpoints to retrain the model on demand and to generate predictions for uploaded CSVs.

---

## Step-by-Step Pipeline

### 1) Data Ingestion
- **Source**: MongoDB collection (`MONGODB_URL_KEY`, `DATA_INGESTION_DATABASE_NAME`, `DATA_INGESTION_COLLECTION_NAME`)
- **Process**: Read data, perform basic cleaning/splits, persist staged data in `Artifacts/<timestamp>/data_ingestion/`
- **Output (artifact)**: `DataIngestionArtifact` with paths to ingested datasets

### 2) Data Validation
- **Inputs**: `DataIngestionArtifact`, `data_schema/schema.yaml`
- **Checks**: Column presence, datatypes, basic integrity
- **Output (artifact)**: `DataValidationArtifact` referencing valid data and a report under `Artifacts/<timestamp>/data_validation/`

### 3) Data Transformation
- **Inputs**: `DataValidationArtifact`
- **Process**: Fit/transform preprocessing (impute, encode, scale, etc.)
- **Outputs**:
  - Transformed arrays/files in `Artifacts/<timestamp>/data_transformation/`
  - Serialized `preprocessor.pkl` (also copied to `final_models/`)

### 4) Model Training
- **Inputs**: `DataTransformationArtifact`
- **Process**: Train scikit-learn model; log metrics to MLflow (`mlruns/`)
- **Outputs**:
  - Trained estimator `model.pkl` in `final_models/`
  - `ModelTrainerArtifact` with metrics/paths in `Artifacts/<timestamp>/model_trainer/`

### 5) Artifact and Model Sync
- **To S3**:
  - Artifacts: `s3://<TRAINING_BUCKET_NAME>/artifact/<timestamp>`
  - Final models: `s3://<TRAINING_BUCKET_NAME>/final_model/<timestamp>`

### 6) Serving (Batch Inference)
- **Endpoint**: `POST /predict`
- **Input**: CSV file (columns must match schema)
- **Process**: Load `final_models/preprocessor.pkl` + `final_models/model.pkl` via `NetworkModel`
- **Output**: Returns a CSV file with an added `predicted_column`

## Project Directory Structure🗃️
```
.
├─ app.py                     # FastAPI app
├─ main.py                    # Pipeline script
├─ Network_data/              # Example dataset
├─ data_schema/
│  └─ schema.yaml             # Column/type schema
├─ network_security/
│  ├─ components/             # Core components
│  │  ├─ data_ingestion.py
│  │  ├─ data_validation.py
│  │  ├─ data_transformation.py
│  │  └─ model_trainer.py
│  ├─ pipeline/
│  │  └─ training_pipeline.py
│  ├─ utils/
│  │  └─ main_utils/          # Serialization, helpers
│  └─ cloud/
│     └─ s3_syncer.py         # S3 folder sync
├─ final_models/              # preprocessor.pkl, model.pkl
├─ Artifacts/                 # Timestamped run outputs
├─ mlruns/                    # MLflow tracking
├─ requirements.txt
├─ Dockerfile
├─ README.md

```
### Environment Variables
````markdown
Create a `.env` file or set system variables:

```bash
MONGODB_URL_KEY="mongodb+srv://<user>:<pass>@<cluster>/<params>"
TRAINING_BUCKET_NAME="<your_s3_bucket>"
# AWS credentials via standard env or AWS config
````

---

# Running the Project

## Start FastAPI

```bash
python app.py
```

* FastAPI runs on `0.0.0.0:8080`
* Open Swagger docs: [http://localhost:8080/docs](http://localhost:8080/docs)

## Trigger Training

* **Via Swagger**: `GET /train`
* **Or script mode**:

```bash
python main.py
```

**Outputs**:

* Artifacts → `Artifacts/<timestamp>/...`
* Models → `final_models/`
* MLflow runs → `mlruns/`

## Batch Prediction

```bash
curl -X POST "http://localhost:8080/predict" \
  -H "accept: text/csv" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@Network_data/phisingData.csv" \
  --output predictions.csv
```

---

# MLflow and Dagshub Usage

Start MLflow UI to monitor runs:

```bash
mlflow ui --backend-store-uri mlruns --port 5000
```

Visit [http://localhost:5000](http://localhost:5000) to view metrics, parameters, and artifacts.

---

# Docker

```bash
docker build -t network-security:latest .
docker run -p 8080:8080 --env-file .env network-security:latest
```

---

# Logging & Error Handling

* **Logs**: `logs/<timestamp>.log`
* **Customized exception**: `NetworkSecurityException`
* **CORS config**: Ensure proper configuration in `app.py` for production

---
## Demo of Project

### Batch Prediction

