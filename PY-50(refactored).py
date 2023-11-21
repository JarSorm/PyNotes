import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, filename='PY-50_log.log', filemode='w')
logging.info('Info')
logging.warning('Warning!')
logging.error('ERROR!')
logging.critical('CRITICAL ERROR!')

#class WrongArgumentValueError(Exception):
#    """аргументы не являются целыми числами или делитель равен 0"""
#    pass

def zero_division(a :int, b :int):
#    if not isinstance(a, int) or not isinstance(b, int) or b == 0:
#        raise WrongArgumentValueError('аргументы введены с ошибкой')
#        return ''
    try:
        a // b
    except ZeroDivisionError:
        print('Деление на 0 недопустимо')
        logger.error('checking', exc_info=True)
        return 0
    else:
        return c
    finally:
        logger.info('just finally')
        print('it was division "a" by "b"')

print(zero_division(6, 0))


