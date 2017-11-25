import pandas as pd
import numpy as np
import sklearn
import data

from sklearn import preprocessing as skp

class Sparser(Data):
    
    def __init__(self, input_df):
        self.input_df = input_df
        self.output_df = pd.NewDataFrame(0)
        self.imitems = pd.Series(list(np.array()))
        self.item = pd.Series(list())