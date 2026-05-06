import os      
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


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
    
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)
            
            y_test_pred=model.predict(X_test)
            
            report[list(models.keys())[i]]=r2_score(y_test,y_test_pred)
            
        return report
    except Exception as e:
        logging.info("Error occured in evaluating models")
        raise CustomException(e,sys)