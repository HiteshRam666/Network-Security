from network_security.components.data_ingestion import DataIngestion 
from network_security.components.data_ingestion import DataIngestion 
from network_security.exception.exception import NetworkSecurityException 
import sys 
from network_security.entity.config_entity import DataIngestionConfig 
from network_security.entity.config_entity import TrainingPipelineConfig
from network_security.logging.logger import logging 
from datetime import datetime

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig(timestamp = datetime.now())
        dataingestionconfig = DataIngestionConfig(training_pipeline_config)          
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion") 
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact) 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

