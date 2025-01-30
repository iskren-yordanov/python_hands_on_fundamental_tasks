from abc import ABC, abstractmethod
import pandas as pd
import json

class Dataset(ABC):

    _temp_dataset = None    

    @property
    def dataset(self):
        return self._temp_dataset
    
    @dataset.setter
    def dataset(self, new_dataset):
        self._temp_dataset = new_dataset

    def __init__(self):
        pass

    @abstractmethod
    def preview():
        raise NotImplementedError

    @abstractmethod
    def show_schema():
        raise NotImplementedError

    @abstractmethod
    def get_data():
        raise NotImplementedError

    @abstractmethod
    def write_data():
        raise NotImplementedError



class JSONDataset(Dataset):
    
    
    def __init__(self, filename):
        self._filename = filename
        self.dataset = None

   

    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def preview(self):
        """Method returns first 20 elements of the head of the dataframe"""
        print(self.dataset.head(20))
    
    def show_schema(self):
        print(self.dataset.info)

    def get_data(self):
        """reads the contents of a json file and returns it as pandas dataframe"""
        if self.filename != "":
            with open(self.filename,  'r', encoding = 'utf=8') as file:
                self.dataset = pd.read_json(file)

                # will create a list of Dicts to contain the data before we parse it to a Dataframe and Join to the Original set
                friends_list_tmp = []
                for idx, elem in self.dataset.iterrows():
                    friends = elem['friends']
                    
                    for f in friends:
                        hobbies_list = ', '.join(f['hobbies'])

                        data = {'id': idx, 'friend_name': f['name'], 'friend_hobbies': hobbies_list}
                        friends_list_tmp.append(data)

                tmp_df = pd.DataFrame.from_dict(friends_list_tmp)
                self.dataset = self.dataset.merge(tmp_df, on='id', how="left")

                #Remove the list after we read and flattened it
                self.dataset.drop(columns = ["friends"], inplace=True)
    
    def write_data(self):
        with open(self.filename,  'w', encoding = 'utf=8') as file:
            self.dataset.to_json(file, index=False, lineterminator='\n') # ,header=False)

class CSVDataset(Dataset):

    def __init__(self, filename):
        self._filename = filename
        self.dataset = None

    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def preview(self):
        """Method returns first 20 elements of the head of the dataframe"""
        print(self.dataset.head(20))

    
    def show_schema(self):
        print(self.dataset.info)

    
    def get_data(self):
        """reads the contents of a csv file and returns it as pandas dataframe"""
        if self.filename != "":
            with open(self.filename,  'r', encoding = 'utf=8') as file:
                self.dataset = pd.read_csv(file)

    
    def write_data(self):
        with open(self.filename,  'w', encoding = 'utf=8') as file:
            self.dataset.to_csv(file, index=False, lineterminator='\n') # ,header=False)