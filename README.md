# Network Security & Phishing Detection System

A comprehensive end-to-end machine learning system for network security threat detection and phishing URL classification. This production-ready ML pipeline automates data ingestion, validation, transformation, and model training with RESTful API endpoints for batch predictions.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [ML Pipeline Components](#ml-pipeline-components)
- [Technologies Used](#technologies-used)
- [Docker Deployment](#docker-deployment)

## 🎯 Overview

This system analyzes 30+ URL features (IP address patterns, SSL states, domain characteristics, etc.) to classify malicious websites and phishing URLs. It implements a complete MLOps pipeline with automated data processing, model training, versioning, and deployment capabilities.

**Impact:** Automated phishing detection system that reduces manual security analysis time and improves threat detection accuracy.

## Demo


https://github.com/user-attachments/assets/25a76842-7648-4490-8f51-750de20e75bf


https://github.com/user-attachments/assets/a1e02b93-3607-447c-a16d-a9f7faacce05




## ✨ Features

- **RESTful API**: FastAPI-based endpoints for batch prediction and model training
- **Comprehensive ML Pipeline**: Automated data ingestion, validation, transformation, and model training
- **Model Evaluation**: Tests 7+ machine learning models with GridSearchCV hyperparameter tuning
- **MLflow Integration**: Experiment tracking, model versioning, and performance monitoring
- **MongoDB Integration**: Scalable data storage and management system
- **Data Validation**: Schema validation and drift detection mechanisms
- **Batch Prediction**: Process CSV files and return predictions with preprocessed data
- **Docker Support**: Containerized application for easy deployment
- **S3 Integration**: Cloud storage for artifacts and models

## 🏗️ Architecture

The system follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Application                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  /train      │  │  /predict    │  │  /docs       │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Training Pipeline                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Data         │→ │ Data         │→ │ Data         │       │
│  │ Ingestion    │  │ Validation   │  │ Transform    │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                          │                                  │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────┐           │
│  │         Model Trainer                         │          │
│  │  (7+ Models with GridSearchCV)                │          │
│  └──────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
┌──────────────┐                    ┌──────────────┐
│   AWS S3     │                    │   MLflow     │
│ (Data Store) │                    │ (Tracking)   │
└──────────────┘                    └──────────────┘
```

## 📁 Project Structure

```
Network Security/
│
├── app.py                          # FastAPI application entry point
├── main.py                         # Training pipeline entry point
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup configuration
├── Dockerfile                      # Docker container configuration
├── .env                           # Environment variables (create this)
│
├── network_security/               # Main package
│   ├── __init__.py
│   ├── components/                 # ML pipeline components
│   │   ├── data_ingestion.py       # MongoDB data ingestion
│   │   ├── data_validation.py      # Schema validation & drift detection
│   │   ├── data_transformation.py  # Data preprocessing & transformation
│   │   └── model_trainer.py        # Model training & evaluation
│   │
│   ├── pipeline/                   # Pipeline orchestration
│   │   └── training_pipeline.py    # Main training pipeline
│   │
│   ├── entity/                     # Configuration & artifact entities
│   │   ├── config_entity.py        # Configuration classes
│   │   └── artifact_entity.py      # Artifact data classes
│   │
│   ├── constants/                  # Constants and configuration
│   │   └── training_pipeline/      # Pipeline constants
│   │
│   ├── utils/                      # Utility functions
│   │   ├── main_utils/             # General utilities
│   │   └── ml_utils/               # ML-specific utilities
│   │       ├── model/              # Model estimators
│   │       └── metric/             # Evaluation metrics
│   │
│   ├── cloud/                      # Cloud integration
│   │   └── s3_syncer.py           # AWS S3 synchronization
│   │
│   ├── logging/                    # Logging configuration
│   │   └── logger.py
│   │
│   └── exception/                  # Custom exceptions
│       └── exception.py
│
├── data_schema/                    # Data schema definitions
│   └── schema.yaml                 # Feature schema (30+ features)
│
├── Artifacts/                      # Generated artifacts (timestamped)
│   └── [timestamp]/
│       ├── data_ingestion/
│       ├── data_validation/
│       ├── data_transformation/
│       └── model_trainer/
│
├── final_models/                   # Trained models
│   ├── model.pkl                  # Best model
│   ├── preprocessor.pkl           # Preprocessing pipeline
│   ├── random_forest.pkl
│   └── xgboost.pkl
│
├── Network_data/                   # Raw data
│   └── phisingData.csv
│
├── logs/                          # Application logs
├── mlruns/                        # MLflow experiment runs
└── predicted_data/                # Prediction outputs
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+
- MongoDB (local or cloud instance)
- AWS Account (for S3, optional)
- Docker (optional, for containerized deployment)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "Network Security"
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the root directory:

```env
MONGODB_URL_KEY=mongodb+srv://username:password@cluster.mongodb.net/
```

### Step 5: Setup MongoDB

1. Create a MongoDB database (default: `HITESH`)
2. Create a collection (default: `NetworkData`)
3. Upload your phishing dataset to MongoDB using `push_data.py`:

```bash
python push_data.py
```

### Step 6: Verify Installation

```bash
python test_mongodb.py
```

## ⚙️ Configuration

### Data Schema

The system expects 30+ features defined in `data_schema/schema.yaml`:

- **URL Features**: `URL_Length`, `Shortining_Service`, `having_At_Symbol`, etc.
- **Domain Features**: `having_IP_Address`, `having_Sub_Domain`, `Domain_registeration_length`, etc.
- **Security Features**: `SSLfinal_State`, `HTTPS_token`, `port`, etc.
- **Content Features**: `Favicon`, `Request_URL`, `URL_of_Anchor`, etc.
- **Behavioral Features**: `on_mouseover`, `RightClick`, `popUpWidnow`, etc.
- **Reputation Features**: `Page_Rank`, `Google_Index`, `web_traffic`, etc.
- **Target**: `Result` (0 = legitimate, 1 = phishing)

### Pipeline Constants

Key constants are defined in `network_security/constants/training_pipeline/__init__.py`:

- `TRAIN_TEST_SPLIT_RATIO`: 0.2 (80/20 split)
- `MODEL_TRAINER_EXPECTED_SCORE`: 0.6 (minimum acceptable score)
- `DATA_INGESTION_DATABASE_NAME`: "HITESH"
- `DATA_INGESTION_COLLECTION_NAME`: "NetworkData"

## 📖 Usage

### Training the Model

#### Option 1: Using FastAPI Endpoint

```bash
# Start the FastAPI server
python app.py

# Trigger training via API
curl http://localhost:8080/train
```

#### Option 2: Using Main Script

```bash
python main.py
```

#### Option 3: Using Training Pipeline Class

```python
from network_security.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()
```

### Making Predictions

#### Using FastAPI Endpoint

```bash
# Start the server
python app.py

# Make batch prediction
curl -X POST "http://localhost:8080/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@validation_data/test.csv"
```

The API returns a CSV file with predictions added as a `predicted_column`.

#### Using Python Code

```python
from network_security.utils.main_utils.utils import load_object
from network_security.utils.ml_utils.model.estimator import NetworkModel
import pandas as pd

# Load preprocessor and model
preprocessor = load_object("final_models/preprocessor.pkl")
model = load_object("final_models/model.pkl")

# Create model wrapper
network_model = NetworkModel(preprocessor=preprocessor, model=model)

# Load and predict
df = pd.read_csv("validation_data/test.csv")
predictions = network_model.predict(df)
df["predicted_column"] = predictions
```

## 🌐 API Endpoints

### Base URL

```
http://localhost:8080
```

### Endpoints

#### 1. **GET /** 
- **Description**: Redirects to Swagger documentation
- **Response**: Redirect to `/docs`

#### 2. **GET /train**
- **Description**: Triggers the complete ML training pipeline
- **Response**: 
  ```json
  "Training is Successful"
  ```
- **Process**: 
  - Data ingestion from MongoDB
  - Data validation
  - Data transformation
  - Model training (7+ models)
  - Artifact and model saving

#### 3. **POST /predict**
- **Description**: Batch prediction on uploaded CSV file
- **Request**: 
  - `file`: CSV file (multipart/form-data)
- **Response**: 
  - CSV file with predictions in `predicted_column`
- **Example**:
  ```bash
  curl -X POST "http://localhost:8080/predict" \
       -F "file=@test.csv"
  ```

#### 4. **GET /docs**
- **Description**: Interactive API documentation (Swagger UI)
- **Access**: Open in browser at `http://localhost:8080/docs`

## 🔄 ML Pipeline Components

The training pipeline consists of four main stages:

### 1. Data Ingestion (`data_ingestion.py`)

**Purpose**: Extract data from MongoDB and prepare it for processing.

**Steps**:
1. **Connect to MongoDB**: Establishes connection using environment variables
2. **Export Collection**: Reads data from MongoDB collection into pandas DataFrame
3. **Data Cleaning**: Removes MongoDB `_id` column and replaces "na" with NaN
4. **Feature Store**: Saves raw data to feature store directory
5. **Train-Test Split**: Splits data (80/20) and saves to ingested directory
6. **Artifact Creation**: Returns `DataIngestionArtifact` with file paths

**Output**:
- `feature_store/phisingData.csv` - Raw data
- `ingested/train.csv` - Training set
- `ingested/test.csv` - Test set

### 2. Data Validation (`data_validation.py`)

**Purpose**: Validate data schema and detect data drift.

**Steps**:
1. **Schema Validation**: 
   - Checks column count matches schema
   - Validates data types for each column
   - Ensures target column exists
2. **Data Drift Detection**:
   - Compares current data statistics with reference data
   - Generates drift report (YAML format)
   - Identifies columns with significant drift
3. **Data Validation**:
   - Separates valid and invalid data
   - Logs validation results
4. **Artifact Creation**: Returns `DataValidationArtifact` with validation status

**Output**:
- `validated/train.csv` - Validated training data
- `validated/test.csv` - Validated test data
- `drift_report/report.yaml` - Drift analysis report

### 3. Data Transformation (`data_transformation.py`)

**Purpose**: Preprocess and transform data for model training.

**Steps**:
1. **Load Data**: Reads validated train and test datasets
2. **Feature-Target Separation**: Separates features (X) and target (y)
3. **Preprocessing Pipeline**:
   - **KNN Imputation**: Handles missing values using K-Nearest Neighbors
     - Parameters: `n_neighbors=3`, `weights="uniform"`
   - **Standardization**: Normalizes features (optional, based on model needs)
4. **Save Preprocessor**: Serializes preprocessing pipeline for inference
5. **Convert to NumPy**: Converts DataFrames to NumPy arrays for model training
6. **Artifact Creation**: Returns `DataTransformationArtifact` with transformed data paths

**Output**:
- `transformed/train.npy` - Transformed training features
- `transformed/test.npy` - Transformed test features
- `transformed_object/preprocessing.pkl` - Preprocessing pipeline

### 4. Model Trainer (`model_trainer.py`)

**Purpose**: Train, evaluate, and select the best model.

**Steps**:
1. **Load Transformed Data**: Reads NumPy arrays for training
2. **Model Initialization**: Initializes 7+ models:
   - Random Forest Classifier
   - XGBoost Classifier
   - Gradient Boosting Classifier
   - Decision Tree Classifier
   - AdaBoost Classifier
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
3. **Hyperparameter Tuning**: Uses GridSearchCV for each model
4. **Model Evaluation**:
   - Trains each model on training set
   - Evaluates on test set
   - Calculates metrics: F1-score, Precision, Recall, Accuracy
5. **Model Selection**:
   - Compares all models
   - Selects best model based on F1-score
   - Checks for overfitting/underfitting (threshold: 0.05)
6. **MLflow Tracking**:
   - Logs metrics for each model
   - Tracks experiments
   - Versions models
7. **Model Saving**: Saves best model and preprocessor
8. **Artifact Creation**: Returns `ModelTrainerArtifact` with model paths

**Output**:
- `trained_model/model.pkl` - Best trained model
- MLflow experiment runs with metrics

**Models Evaluated**:
- **Random Forest**: Ensemble of decision trees
- **XGBoost**: Gradient boosting with regularization
- **Gradient Boosting**: Sequential ensemble learning
- **Decision Tree**: Rule-based classification
- **AdaBoost**: Adaptive boosting
- **Logistic Regression**: Linear classification
- **KNN**: Instance-based learning

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.10+**: Programming language
- **FastAPI**: Modern, fast web framework for building APIs
- **MongoDB**: NoSQL database for data storage
- **MLflow**: ML lifecycle management and experiment tracking
- **scikit-learn**: Machine learning library
- **XGBoost**: Gradient boosting framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

### Additional Libraries
- **pymongo**: MongoDB Python driver
- **uvicorn**: ASGI server for FastAPI
- **python-dotenv**: Environment variable management
- **pyaml**: YAML file parsing
- **dagshub**: MLflow integration with DagsHub

### DevOps
- **Docker**: Containerization
- **AWS S3**: Cloud storage 

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t network-security:latest .
```

### Run Container

```bash
docker run -p 8080:8080 \
  -e MONGODB_URL_KEY="your_mongodb_url" \
  network-security:latest
```

### Docker Compose (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  network-security:
    build: .
    ports:
      - "8080:8080"
    environment:
      - MONGODB_URL_KEY=${MONGODB_URL_KEY}
    volumes:
      - ./Artifacts:/app/Artifacts
      - ./final_models:/app/final_models
```

Run with:
```bash
docker-compose up
```

## 📊 Model Performance

The system evaluates models using multiple metrics:

- **F1-Score**: Harmonic mean of precision and recall
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **Accuracy**: Correct predictions / Total predictions

Models are selected based on F1-score, with a minimum expected score of 0.6.

## 🔍 Monitoring & Logging

- **Logs**: Stored in `logs/` directory with timestamped files
- **MLflow**: Track experiments at `http://localhost:5000` (if running locally)
- **Artifacts**: All pipeline artifacts stored in timestamped directories

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Hitesh Ram**
- Email: hiteshram321@gmail.com

