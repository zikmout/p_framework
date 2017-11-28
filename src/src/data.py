import os
import pandas as pd
import sklearn
import numpy as np
import glob, os
# import src.loader
from sklearn import preprocessing as skp

class Data:
    """ Handles stats / save / load of each subclasses """
    # path = '/Users/xxx/Projects/p_framework/data/'
    def __init__(self, config):
        self.config = config
    def _load_data(self):
        return 'jsonload'
    def get_stats(self):
        raise NotImplementedError()

class R_Data(Data):
    def __init__(self, config, input_df):
        super().__init__(config)
        self.input_df = input_df
        self.output_df = None
        if self.output_df is not None:
            print(self.input_df.shape)
        else:
            print('There is no ouput df')

    def get_stats(self):
        print('Stats on R_Data')

class C_Data(Data):
    def __init__(self, R_Data):
        super().__init__(R_Data)
        self.input_df = R_Data.output_df
        self.output_df = None
    def get_stats(self):
        print('Stats on C_Data')

class N_Data(Data):
    def __init__(self, C_Data):
        self.input_df = C_Data.output_df
        self.output_df = None
    def get_stats(self):
        print('Stats on N_Data')


class S_Data(Data):
    def __init__(self, N_Data):
        self.input_df = N_Data.output_df
        self.output_df = None
    def get_stats(self):
        print('Stats on S_Data')

