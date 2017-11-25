import numpy as np
import pandas as pd
import sklearn
import data

class Loader():
    """ Meant to handle loading input_df from different file types i.e. excel, csv, aggregade """
    __init__(self, name):
        self.name = name
        self.input_df = pd.DataFrame()
    def load(self):
        raise NotImplementedError('Method load should be overriden')

class CSVLoader(Loader):
    def __init__(self):
        super().__init__()
    def load(self):
        self.input_df = pd.read_csv(Data.path + name + '.csv')

class ExcelLoader(Loader):
    def __init__(self):
        super().__init__()
    def load(self):
        self.input_df = pd.read_excel(Data.path + name + '.xlsx')

class AggregateExcelLoader(Loader):
    """ all files must have same colums for same format """
    def __init__(self, fmt):
        super().__init__()
    def load(self):
        allFiles = glob.glob(Data.path + "/*.xlsx")
        list_ = []
        for file_ in allFiles:
            df = pd.read_excel(file_,index_col=None, header=0)
            list_.append(df)
        self.input_df = pd.concat(list_)