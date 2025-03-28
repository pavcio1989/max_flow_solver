import sys
import logging
# Add content root to your path
sys.path.append('C:/Users/pawel/Desktop/Learning/max_flow_solver')

if __name__ == "__main__":
    import os

    from src.config.config import Config
    from src.loggers.mfs_logger import MFSLogger
    from src.pipelines.pipeline import Pipeline

    logger = MFSLogger(__name__, level=logging.INFO)

    config = Config()

    pipeline = Pipeline(config)

    pipeline.run()
