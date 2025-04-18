from .repository import IrisRepository

class IrisDataset:
    def __init__(self):
        self.df = IrisRepository().get_dataframe()

    