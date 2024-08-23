import logging
logging.basicConfig(filename='test4.txt',level = logging.INFO)
logging.info("This is my code in logging")
logging.warning("This is warning")

li = list(range(1,10))
for i in li:
    lis = []
    if i%2 ==0:
        lis.append(i)
        logging.info(lis)
        logging.info("This is the warning to the user that the have out 2 in list")