# import logging
# from log_config import LOGGING

# class LogWriter:
#     def __init__(self):
#         self.loggers = self._setup_loggers()

#     def _setup_loggers(self):
#         loggers = {}
#         for key, config in LOGGING.items():
#             logger = logging.getLogger(key)
#             handler = logging.FileHandler(config['file_path'])
#             formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#             handler.setFormatter(formatter)
#             logger.setLevel(config['level'])
#             logger.addHandler(handler)
#             loggers[key] = logger
#         return loggers

#     def write_log(self, level, log_string, source):
#         try:
#             logger = self.loggers[source]
#             if level == "info":
#                 logger.info(log_string)
#             elif level == "error":
#                 logger.error(log_string)
#             elif level == "success":
#                 logger.info(log_string)
#         except Exception as e:
#             print(f"Error writing log: {e}")














import logging
from log_config import LOGGING

class LogWriter:
    def __init__(self):
        self.loggers = self._setup_loggers()

    def _setup_loggers(self):
        loggers = {}
        for key, config in LOGGING.items():
            logger = logging.getLogger(key)
            handler = logging.FileHandler(config['file_path'])
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.setLevel(config['level'])
            logger.addHandler(handler)
            loggers[key] = logger
        return loggers

    def write_log(self, level, log_string, source):
        try:
            logger = self.loggers[source]
            if level == "info":
                logger.info(log_string)
            elif level == "error":
                logger.error(log_string)
            elif level == "success":
                logger.info(log_string)
        except Exception as e:
            print(f"Error writing log: {e}")
