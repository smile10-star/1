==================== 文件：src/utils/logger.py ====================
import logging
import os

def get_logger(name):
logger = logging.getLogger(name)
level = os.getenv("LOG_LEVEL", "INFO").upper()
logger.setLevel(level)
if not logger.handlers:
ch = logging.StreamHandler()
ch.setLevel(level)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
return logger
