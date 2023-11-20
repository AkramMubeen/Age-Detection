from AgeDetection import logger
from AgeDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from AgeDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline




STAGE_NAME = "Data Ingestion"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare Base Model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e