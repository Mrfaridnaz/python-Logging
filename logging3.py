import logging
logging.basicConfig(filename='test3.log',level = logging.INFO)
logging.info("This is my first code in logging")

# Add more information

li = list(range(1,10))
for i in li:
    lis = []
    if i%2 ==0:
        lis.append(i)
        logging.info(lis)