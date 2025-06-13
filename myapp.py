# basé sur https://docs.python.org/3/library/logging.html

# myapp.py
import logging, dotenv, os, ecs_logging
import mylib
logger = logging.getLogger(__name__)

dotenv.load_dotenv()
LOG=os.environ['LOG']
level = getattr(logging, LOG, None)

# Add an ECS formatter to the Handler
#handler = logging.StreamHandler()
handler = logging.FileHandler('myapp-json.log')
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)


def main():
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(process)d %(message)s') # filename='myapp.log'
    logger.debug('Ceci est un essai')
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished', extra={"http.request.method": "get"})

if __name__ == '__main__':
    main()