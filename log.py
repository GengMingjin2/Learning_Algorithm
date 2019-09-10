#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: logging initializer

Authors: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 15:25:43
"""

import logging

class Logger:
    """ The class for log """
    def __init__(self, path, clevel = logging.DEBUG, flevel = logging.DEBUG):
        """
        The initialization of the class
        Args:
             path: the path to the log file.(Caution! In ubuntu is not the same as in windows!
             clevel: the CMD log level. The default is DEBUG.
             flevel: the file log level. The default is DEBUG.
        """
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # set the CMD log handler
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # set the file log handler
        fh = logging.FileHandler(path)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        # add the two log handlers to the logging module!
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        """ log the debug message """
        self.logger.debug(message)

    def info(self, message):
        """ log the info message """
        self.logger.info(message)

    def warn(self, message):
        """ log the warning message """
        self.logger.warning(message)

    def error(self, message):
        """ log the error message """
        self.logger.error(message)

    def cri(self, message):
        """ log the critical message """
        self.logger.critical(message)

if __name__ == "__main__":
    logger = Logger("log/log_test.txt", logging.ERROR, logging.DEBUG)
    logger.debug("A DEBUG message!")
    logger.error("An ERROR message!")
    logger.warn("A WARNING message!")
    logger.info("An INFO message!")
    logger.cri("A CRITICAL message!")
