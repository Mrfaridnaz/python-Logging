
import logging
logging.basicConfig(filename = 'test8.txt',
                    level = logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s)'
                    )
logging.info("This is my log with timestamp with levelname")