import logging
logging.basicConfig(filename='test5.txt',level = logging.INFO)
logging.info("This is my code in logging")
logging.warning("This is warning")
logging.error("This is an error from logging system")

logging.shutdown()
# It will not log anything after shutdown.