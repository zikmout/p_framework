# p_framework implemented at home
import sys
# import src.loader
# import src.data

from src.loader import *
from src.config import Config
from src.loader import Loader

def main():
    print('Welcome to the program p_framework')
    # Loader.ExcelLoader()
    conf = Config('config', 'excel')
    conf.print_config()

    RawData = load_data(conf) 
    # loader = Loader(conf)
    # loader.load(conf) 


if __name__ == '__main__':
    try:
        main()
    except IOError or KeyboardInterrupt:
        sys.exit(0)
        