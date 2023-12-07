from src.mlproejct.logger import logging
from src.mlproejct.exception import CustomException
from src.mlproejct.componenets.data_ingestion import Dataingestion, DataIngestionConfig
 

import sys




if __name__ == "__main__":
    logging.info("The execution has started")


    try:
        data_ingestion = Dataingestion()
        data_ingestion.initiate_data_ingestion()
        #DataIngestionConfig = DataIngestionConfig()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
