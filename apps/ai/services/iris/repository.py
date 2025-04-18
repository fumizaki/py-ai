import pandas as pd


class IrisRepository:

    def __init__(self):
        pass
    
    def get_dataframe(self) -> pd.DataFrame:
        return pd.read_csv('datasets/Iris.csv', header=0, encoding='utf-8')

