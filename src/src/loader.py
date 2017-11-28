import numpy as np
import pandas as pd
import sklearn
import src.data
from src.config import Config
import glob

def load_data(config):
    dic = {
        'excel':'ExcelLoader',
        'csv':'CSVLoader'
    }
    print('FUNCTION LOAD DATA')
    class_name = dic.get(config.fmt)
    Loader = globals().get(class_name)
    print('OOO /\ class_name = {}'.format(class_name))
    print('OOO /\ config.fmt = {}'.format(config.fmt))
    if Loader is None:
        raise RuntimeError('No class defined for the format')
    loader = Loader(config)
    input_df = loader.load()
    return R_Data(config, input_df)

class Loader():
    """ Meant to handle loading input_df from different file
        types i.e. excel, csv, aggregade """
    def __init__(self, config):
        self.config = config
    def load(self):
        raise NotImplementedError('Method load should be overriden')

class ExcelLoader(Loader):
    def __init__(self, config):
        super().__init__(config)

    def load(self):
        return pd.read_excel(self.config.project_path + self.config.name + '.xlsm', index_col=None, header=0)

class AggregateExcelLoader(Loader):
    """ all files must have same colums for same format """
    def __init__(self, config):
        super().__init__(config)

    def load(self):
        allFiles = glob.glob(self.config.project_path + '\\*.xlsx')
        list_ = []
        for file_ in allFiles:
            df = pd.read_excel(file_,index_col=None, header=0)
            list_.append(df)
        self.input_df = pd.concat(list_)

class CSVLoader(Loader):
    def __init__(self, config):
        super().__init__(config)
    def load(self):
        self.input_df = pd.read_csv(self.config.project_path + self.config.name + '.csv', index_col=None, header=0)
    
