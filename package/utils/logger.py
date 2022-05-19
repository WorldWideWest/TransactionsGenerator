import logging, os, sys

class Logger(object):

    def __init__(self, level = logging.DEBUG,
        file = os.path.join(os.getcwd(), "exports/.logs.log"),
        formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s")):

        self.level = level
        self.file = file
        self.formatter = formatter

    def get_logger(self) -> logging.Logger:

        logger = logging.getLogger()
        logger.setLevel(self.level)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setLevel(self.level)
        consoleHandler.setFormatter(self.formatter)

        fileHandler = logging.FileHandler(self.file)
        fileHandler.setLevel(self.level)
        fileHandler.setFormatter(self.formatter)

        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)

        return logger