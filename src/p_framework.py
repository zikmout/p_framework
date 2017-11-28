# p_framework implemented at home
import sys
# import src.loader
# import src.data

from src.loader import *
from src.config import Config
from src.loader import Loader
from src.cleaner import Cleaner
from src.normalizer import Normalizer
from src.sparsifier import Sparsifier
from src.data import *

def main():
    print('Welcome to the program p_framework')
    # Loader.ExcelLoader()
    conf = Config('config', 'excel')
    conf.print_config()

    R_Data = load_data(conf)
    R_Data.get_stats()

    C_Data = Cleaner(R_Data)
    R_Data.get_stats()

    N_Data = Normalizer(C_Data)
    C_Data.get_stats()

    S_Data = Sparsifier(N_Data)
    S_Data.get_stats()

if __name__ == '__main__':
    try:
        main()
    except IOError or KeyboardInterrupt:
        sys.exit(0)
        