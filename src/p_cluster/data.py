import os
import pandas as pd
import sklearn
import numpy as np
import glob, os
# import src.loader
from sklearn import preprocessing as skp

class Data:
    """ Handles stats / save / load of each subclasses """
    path = '/Users/xxx/Projects/p_framework/data/'
    def __init__(self, config):
        self.config = config
    def _load_data(self):
        return 'jsonload'
    def get_stats(self):
        raise NotImplementedError()

class RawData(Data):
    def __init__(self, config, input_df):
        super().__init__(config)
        self.input_df = input_df
        self.output_df = None

    def get_stats(self):
        print('Stats on raw data <<<<>>>>>')

class CleanedData(Data):
    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.input_df = raw_data.output_df
    def get_stats(self):
        print('Stats on raw data..........')

