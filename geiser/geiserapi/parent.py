import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


def log(message, level):
    if level == 'Debug':
        logging.debug(message)
    elif level == 'Warning':
        logging.warning(message)
    elif level == 'Info':
        logging.info(message)
    elif level == 'Error':
        logging.error(message)


