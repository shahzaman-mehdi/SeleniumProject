import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger


