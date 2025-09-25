from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_ingestion import DataIngestion 
from network_security.exception.exception import NetworkSecurityException 
import sys 
from network_security.entity.config_entity import DataIngestionConfig, DataValidationConfig
from network_security.entity.config_entity import TrainingPipelineConfig
from network_security.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from network_security.logging.logger import logging 
from datetime import datetime

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig(timestamp = datetime.now())
        dataingestionconfig = DataIngestionConfig(training_pipeline_config = training_pipeline_config)          
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion") 
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact) 

        datavalidationconfig = DataValidationConfig(training_pipeline_config=training_pipeline_config) 
        data_validation = DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info(f"Initiating Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation() 
        logging.info("Data Validation Completed") 

        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

