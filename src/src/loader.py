import numpy as np
import pandas as pd
import sklearn
import src.data

def load_data(config):
    dic = {
        'excel':'csv',
        'csv':'CSVLoader'
    }
    class_name = dic.get(config.fmt)
    Loader = globals().get(class_name)
    if Loader is None:
        raise RuntimeError('No class defined for the format')
    loader = Loader(config)
    input_df = loader.load()
    return RawData(config, input_df)

class Loader():
    """ Meant to handle loading input_df from different file types i.e. excel, csv, aggregade """
    def __init__(self, config):
        self.config = config
    def load(self):
        raise NotImplementedError('Method load should be overriden')

class ExcelLoader(Loader):
    def __init__(self, name):
        super().__init__()
    def load(self):
        self.input_df = pd.read_excel(Config.path + name + '.xlsx', index_col=None, header=0)

class AggregateExcelLoader(Loader):
    """ all files must have same colums for same format """
    def __init__(self, fmt):
        super().__init__()
    def load(self):
        allFiles = glob.glob(Config.path + "/*.xlsx")
        list_ = []
        for file_ in allFiles:
            df = pd.read_excel(file_,index_col=None, header=0)
            list_.append(df)
        self.input_df = pd.concat(list_)

class CSVLoader(Loader):
    def __init__(self):
        super().__init__()
    def load(self):
        self.input_df = pd.read_csv(Config.path + name + '.csv', index_col=None, header=0)

