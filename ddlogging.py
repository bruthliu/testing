#!/usr/bin/env python3


import logging
import time

class DDLogging:
    """log module"""
    def __init__(self, task_name, log_path):
        self.logger = logging.getLogger(task_name)
        self.level = 'INFO'
        self.logger.setLevel(logging.INFO)
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setLevel(logging.INFO)
        self.log_path=log_path
        self.fileHandler = logging.FileHandler(filename=self.log_path + '/' + task_name + '.' + time.strftime('%Y%m%d') + '.log', mode='a', encoding='utf8')
        self.fileHandler.setLevel(logging.INFO)
        loggerFormatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
        self.consoleHandler.setFormatter(loggerFormatter)
        self.fileHandler.setFormatter(loggerFormatter)

    def get_logger(self):
        self.logger.addHandler(self.consoleHandler)
        self.logger.addHandler(self.fileHandler)
        return self.logger

    def set_level(self, level):
        self.level = level
        if self.level == 'DEBUG':
            self.consoleHandler.setLevel(logging.DEBUG)
            self.fileHandler.setLevel(logging.DEBUG)
        elif self.level == 'INFO':
            self.consoleHandler.setLevel(logging.INFO)
            self.fileHandler.setLevel(logging.INFO)
        elif self.level == 'WARNING':
            self.consoleHandler.setLevel(logging.WARNING)
            self.fileHandler.setLevel(logging.WARNING)
        elif self.level == 'ERROR':
            self.consoleHandler.setLevel(logging.ERROR)
            self.fileHandler.setLevel(logging.ERROR)
        else:
            self.consoleHandler.setLevel(logging.DEBUG)
            self.fileHandler.setLevel(logging.DEBUG)
    def set_logfilepath(self,log_path):
        self.log_path=log_path

if __name__ == '__main__':
    myLog = DDLogging('mytest', '.')
#    myLog.set_level('INFO')
    myLogger = myLog.get_logger()
    myLogger.info('info')
    myLogger.debug('debug')
