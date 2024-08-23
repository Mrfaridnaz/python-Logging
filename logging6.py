import logging
logging.basicConfig(filename='test6.txt', level = logging.DEBUG, format = '%(asctime)s %(message)s')
logging.info("This is my log with timestamp")