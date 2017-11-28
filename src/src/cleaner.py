import pandas as pd
import numpy as np

class Cleaner():
    ''' Supposed to Clean data from nans for instance'''
    def __init__(self, R_Data):
        self.input_df = R_Data.output_df;
        self.clean_nans()
    def clean_nans(self):
        self.input_df = np.dropna()
        self.output_df = self.input_df
        pass
    def get_output_df(self):
        self.output_df = self.input_df
        return self.output_df
    def get_stats(self):
        pass
    