import math
import logging
from numbers import Number

import student

# DEBUG 10
# INFO 20
# WARNING 30
# ERROR 40
# CRITICAL 50

formatter = "%(asctime)s:%(levelname)s:%(message)s"
logging.basicConfig(level=logging.ERROR, format=formatter, filename='demo.log')


def get_sqrt(num):
    logging.debug('finding if "num" is a valid number or not...')

    if isinstance(num, Number):
        logging.info(f'{num} is a valid number')
    else:
        logging.info(f'{num} is not a valid number')

    try:
        if 0 < num < 1:
            logging.warning('value is too low')

        logging.info(f'square root of {num} is {math.sqrt(num)}')
    except ValueError:
        logging.error('negative numbers not allowed')
    except TypeError:
       logging.error('only integer or floating point numbers are allowed')


# run the function
get_sqrt(-6)
