# basé sur https://docs.python.org/3/library/logging.html

# myapp.py
import logging, dotenv, os
import mylib
logger = logging.getLogger(__name__)

dotenv.load_dotenv()
LOG=os.environ['LOG']
level = getattr(logging, LOG, None)

def main():
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(process)d %(message)s') # filename='myapp.log'
    logger.debug('Ceci est un essai')
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()