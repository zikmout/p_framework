import pandas as pd
import numpy as np
from src.data import *

class Sparsifier():
    ''' Supposed to Sparsify data '''
    def __init__(self, N_Data):
        self.input_df = N_Data.output_df;

    def get_output_df(self):
        self.output_df = self.input_df
        return self.output_df

    def get_stats(self):
        pass