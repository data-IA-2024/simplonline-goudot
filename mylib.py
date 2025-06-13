# mylib.py
import logging, dotenv, os
logger = logging.getLogger(__name__)

dotenv.load_dotenv()
logger.setLevel(os.environ['LOG_MYLIB'])

def do_something():
    logger.info('Doing something')
    logger.debug("Essai")