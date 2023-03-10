
import yaml
import logging.config
from src.helper_functions import add, multiply

with open('config/main.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

logging.config.dictConfig(config['logging'])
main_logger = logging.getLogger('main')

main_logger.info('{} : {}'.format('Addition result', add(3, 2)))
main_logger.info('{} : {}'.format('Multiplication result', multiply(3, 2)))