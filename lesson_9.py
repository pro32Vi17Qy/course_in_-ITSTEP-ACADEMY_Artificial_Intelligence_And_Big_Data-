import logging

# import os
# path = os.mkdir("path")
# file = open("path/file.txt", "w+")
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w+",
                    format="\n\tWe have next logging massage:%(asctime)s%(levelname)s - %(message)s")

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
                    format="We have next logging massage:%(asctime)s%(levelname)s - %(message)s")
try:
    print(5 / 0)
except ZeroDivisionError:
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
