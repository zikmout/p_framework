import pandas as pd
import numpy as np
import sklearn

from sklearn import preprocessing as skp

Class AutoEncoder:
    
    def __init__(self, input_df):
        self.input_df = input_df
        self.output_df = pd.NewDataFrame(0)
        self.imitems = pd.Series(list(np.array()))
        self.item = pd.Series(list())

    def get_imitem(self):
        
    def purge_imitems(self):
        self.output_df = np.concat([self.output_df, self.imitems])
        del.self.imitems()
    
    def encode(self, label, method, sparse_output=False):
        # self.item = self.input_df[label]
        main_method = method.split('_')[0]
        sub_method = method.split('_')[1]
        if main_method == 'binary':
            self.item = self.input_df[label]
            if sub_method == 'dependant': lb = skp.LabelBinaryizer(neg_label=-1, \
            pos_label=1, sparse_output=sparse_output)
            else if sub_method == 'independant': lb = skp.LabelBinaryizer(neg_label=0, \
            pos_label=1, sparse_output=sparse_output)
            
            lb.fit(self.item)
            if len(lb.classes_) != 2:
                u.echo_debug('Label \'{}\' cannot be binary_dependant \
                encoded:\nClasses are :\n{}'.format(label, lb.classes_))
            if sparse_output:
                lb.transform()
                return self.item
            else:
                return self.item
        
        else if main_method == 'numerical':
            self.item = self.input_df[label]
            scaler = skp.StandardScaler(copy=True, with_mean=True, \
            with_std=True).fit(self.item)
            if sub_method == 'dependant':
                self.item = scaler.scale_
            else if sub_method =='independant':
                self.item = pd.get_dummies(data=self.input_df, columns=label)
                self.item = scaler.transform(self)    
            return self.item
