'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python looging .  

'''

import logging

def logger_init(name):
    
       '''
       Description: 
           The function initializes and configures a logger with both file and 
           console output. The logger is set to log messages at the DEBUG level 
           or higher, and includes a specific format for log messages. The logs 
           are saved in a file named 'all.log' and also displayed in the console.
       Parameters:
           name (str): The name of the logger, usually used to distinguish log 
           sources (e.g., module or class name).
       Return:
           logging.Logger: A configured logger instance that writes logs to both 
           a file and the console.
       '''
    
       logger = logging.getLogger(name)
       # configuring our specific logger
       # setting the log level for the logger
       logger.setLevel(logging.DEBUG)
       # creating a formatter
       formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
       file_handler = logging.FileHandler('all.log')
       # adding the formatting to the file handler
       file_handler.setFormatter(formatter)
       # to display the result in the console
       stream_handler = logging.StreamHandler()
       # adding the formatting to the stream handler
       stream_handler.setFormatter(formatter)
       # adding file handler and stream_handler to the logger
       logger.addHandler(file_handler)
       logger.addHandler(stream_handler)
       return logger