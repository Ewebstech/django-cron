"""
Author: Emmanuel Paul

"""
# -*- coding: utf-8 -*-  
import logging

def get_logger():
    logger = logging.getLogger()  
    logger.setLevel(logging.INFO)  
  
    logfile = './log.txt'  
    lf = logging.FileHandler(logfile, mode='a+')  
    lf.setLevel(logging.DEBUG)   #
  

    ld = logging.StreamHandler()     
    ld.setLevel(logging.INFO) #
  

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  
    lf.setFormatter(formatter)  
    ld.setFormatter(formatter)  
  

    logger.addHandler(lf)  
    logger.addHandler(ld)  

    return logger

if __name__ == "__main__":
    logger = get_logger()
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')