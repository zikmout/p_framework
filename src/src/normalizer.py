from src.data import Data

class Normalizer(Data):
    
    def __init__(self, C_Data):
        super().__init__()
        self.output_df = pd.DataFrame()
        self.imitems = pd.Series(list(np.array()))
        self.item = pd.Series(list())

    def get_imitem(self):
        print(self.item.info())
        return self.item
        
    def purge_imitems(self):
        self.output_df = np.concat([self.output_df, self.imitems])
        # del.self.imitems()
    
    def auto_encoder(self, label, method, sparse_output=False):
        # self.item = self.input_df[label]
        main_method = method.split('_')[0]
        sub_method = method.split('_')[1]
        
        if main_method == 'binary':
            self.item = self.input_df[label]
            if sub_method == 'dependant': lb = skp.LabelBinaryizer(neg_label=-1, \
            pos_label=1, sparse_output=sparse_output)
            elif sub_method == 'independant': lb = skp.LabelBinaryizer(neg_label=0, \
            pos_label=1, sparse_output=sparse_output)
            
            lb.fit(self.item)
            if len(lb.classes_) != 2:
                u.echo_debug('Label ... cannot be binary_dependant encoded. Classes are :') # .format(label, lb.classes_))
            if sparse_output:
                lb.transform()
                return self.item
            return self.item
        
        elif main_method == 'numerical':
            self.item = self.input_df[label]
            scaler = skp.StandardScaler(copy=True, with_mean=True, \
            with_std=True).fit(self.item)
            if sub_method == 'dependant':
                self.item = scaler.scale_
            elif sub_method =='independant':
                self.item = pd.get_dummies(data=self.input_df, columns=label)
                self.item = scaler.transform(self.item)    
            return self.item

        elif main_method == 'categorical':
            # self.item = self.input_df[label]

            if sub_method == 'dependant_le':
                print('Debug -> {}'.format(self.item.values_counts()))
                self.item = pd.get_dummies(data=self.input_df, columns=label)
                le = skp.LabelEncoder()
                self.item = le.fit_transform(self.item)
                # or df.apply(LabelEncoder().fit_transform)
                return self.item
            elif sub_method == 'dependant_bd':
                self.item = self.input_df.select_dtypes(include=[label]).copy()
                bd = ce.backward_difference.BackwardDifferenceEncoder(cols=[''.join(label,'_type')])
                bd.fit(self.item, verbose=1)
                return self.item
                # show ? bd.transform(self.item).iloc[]
            elif sub_method == 'dependant_pe':
                pe = ce.polynomialEncoder(cols=''.join(label,'_type'))
                pe.fit(self.item, verbose=1)
                return self.item

            echo_debug('Vous n etes pas cense etre la.')
    
    
                # show ? pee.transform(self.item).iloc[]

