import logging
logging.basicConfig(level=logging.WARNING, filename='PY-50_log.log', filemode='w')
logging.warning('warning!')
logging.error('ERROR!')
logging.critical('CRITICAL ERROR!')
def zero_division():
    try:
        division = 5/0
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    try:
        raise Warning('таки не делим на ноль')
    finally:
        print('division = 5/0')


zero_division()