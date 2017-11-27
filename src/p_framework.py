# p_framework implemented at home
import sys
import src.loader
from src import data

def main():
    print('Welcome to the program p_framework')
    # Loader.ExcelLoader()
    conf = Config('config', 'excel')
    conf.print_config()


if __name__ == '__main__':
    try:
        main()
    except IOError or KeyboardInterrupt:
        sys.exit(0)
        