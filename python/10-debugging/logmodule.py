#!/usr/bin/python3

# Python's logging module makes it easy to create a record of custom messages that you write. These log messages will describe when the program execution has reached the logging function call and list any variables you have specified at that point in time. On the other hand, a missing log message indicates a part of the code was skipped and never executed.

import logging

# TO DISABLE LOGGING
# Will disable CRITICAL level and below --in other words, everything
# logging.disable(logging.CRITICAL)

# Logging Levels: Lowest -> Highest
# DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
# eg. logging.info('Log module is working')
# eg. logging.critical('CRITICAL ERROR: Program is unable to recover!')

# passing .logging.ERROR to level will only show logs with level ERROR and above

# you can even write the log messages to a file by adding:
# filename='myProgramLog.txt' to the arguments
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# When Python logs an event, it creates a LogRecord object that holds information about that event. The logging module's basicConfig() function lets you specify what details about the LogRecord object you want to see and how you want those details displayed.

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial({})'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')
