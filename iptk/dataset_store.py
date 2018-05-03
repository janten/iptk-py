import os
from .dataset import Dataset

class DatasetStore(object):
    """
    This helper class returns the absolute path on disk for a given IPTK 
    dataset identifier. Subclass this and overwrite the dataset_path method if
    you want to use a different layout.
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def dataset_path(self, dataset_id):
        chars = list(dataset_id[:4])
        subdir = "/".join(chars)
        path = os.path.join(self.root_dir, subdir, dataset_id)
        return path
        
    def dataset(self, dataset_id):
        dataset = Dataset(self.dataset_path(dataset_id))
        return dataset
    