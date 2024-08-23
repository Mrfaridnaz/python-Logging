import logging
logging.basicConfig(filename = 'test7.txt',
                    level = logging.DEBUG,
                    format='%(asctime)s %(name)s %(message)s)'
                    )
logging.info("This is my log with timestamp")


