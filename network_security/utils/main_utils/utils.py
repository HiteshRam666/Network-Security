import yaml
from network_security.exception.exception import NetworkSecurityException 
from network_security.logging.logger import logging 
import os, sys 
import numpy as np 
import dill
import pickle 

def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f) 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path) 
        os.makedirs(os.path.dirname(file_path), exist_ok=True) 
        with open(file_path, 'w') as file:
            yaml.dump(content, file) 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file 
    file_path: str location of file to save 
    array: np.array data to save 
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True) 
        with open(file_path, 'wb') as f:
            np.save(f, array) 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils Class") 
        os.makedirs(os.path.dirname(file_path), exist_ok=True) 
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f) 
        logging.info("Exited the save_object method of MainUtils class") 
    except Exception as e:
        raise NetworkSecurityException(e, sys)
