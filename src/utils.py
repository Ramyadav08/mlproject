import os      
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        logging.info("Directory created for the file path")
        pd.to_pickle(obj,file_path)
        logging.info("Object is pickled successfully")
    except Exception as e:
        logging.info("Error occured in saving object")
        raise CustomException(e,sys)