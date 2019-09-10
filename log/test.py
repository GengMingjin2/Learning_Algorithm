#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: A test scripts for logging.conf

Authors: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 16:47:54
"""

import logging
import logging.config

logging.config.fileConfig('logging.conf')

root_logger = logging.getLogger('root')
logger = logging.getLogger('main')

if __name__ == "__main__":
    root_logger.info("test root logger...")
    logger.info("test main logger...")
