from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from network_security.entity.artifact_entity import ClassificationMetricArtifact 
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
import os 
import sys

def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    try:
        model_f1_score = f1_score(y_true, y_pred) 
        model_recall_score = recall_score(y_true, y_pred) 
        model_precision_score = precision_score(y_true, y_pred)

        classification_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score, 
            precision_score=model_precision_score, 
            recall_score = model_recall_score
        )
        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e, sys)