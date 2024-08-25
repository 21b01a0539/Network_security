import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        logging.info("training has started")
        print("Hi")
        model_training=TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        print("hey error")
        raise NetworkSecurityException(e,sys)
    
if __name__=='__main__':
    start_training()