"""Class for a csv file dataset usage"""
from datetime import datetime
import pandas as pd
import dataset

class CSVDataset(dataset.Dataset):
    """Class CSVDataset"""

    def __init__(self, src_filename, target_filename):
        super().__init__()
        self._src_file_name = src_filename
        self._target_file_name = target_filename

        # hidden call inside constructor
        self._fetch_data()
        self._clean_data()
        self._transform_data()

    @property
    def src_filename(self):
        """getter for _src_file_name"""
        return self._src_file_name

    @src_filename.setter
    def src_filename(self, value):
        """setter for _src_file_name"""
        self._src_file_name = value

        # hidden call inside constructor
        self._fetch_data()
        self._clean_data()
        self._transform_data()

    @property
    def target_filename(self):
        """getter for _target_file_name"""
        return self._target_file_name

    @target_filename.setter
    def target_filename(self, value):
        """setter for _src_file_name"""
        self._target_file_name = value

    def _fetch_data(self):
        """reads data from file"""
        with open("task6/" + self._src_file_name,  'r', encoding = 'utf=8') as file:
            self._my_data_set = pd.read_csv(file)

    def save_data(self):
        with open("task6/" + self._target_file_name,  'w', encoding = 'utf=8') as file:
            self._my_data_set.to_csv(file, index=False, lineterminator='\n') # ,header=False)

    def show_head_data(self):
        """Method returns first 20 elements of the head of the dataframe"""
        print(self._my_data_set.head(20))

    #def see_a_record(self):
        #print(self._my_data_set.dtypes)
        #print(self._my_data_set.iloc[0]['Subject'])
        #if self._my_data_set.size != 0:
            #print(self._my_data_set.iloc[0])
            #print("val", self._my_data_set.iloc[0]['Series_title_5'] ,
            # type(self._my_data_set.iloc[0]['Series_title_5'] ))
            #if not float.is_integer(self._my_data_set.iloc[0]['Series_title_5']):
            #    print("Is NaN")

        #for a in self._my_data_set.columns:
        #    print(self._my_data_set[0][a])

    def _transform_data(self):
        """at this point in time, add a current timestamp column to the end of the dataframe"""
        t = datetime.today()
        self._my_data_set['current_time'] = t.strftime('%Y-%m-%d %H:%M:%S')

    def _clean_data(self):
        """drops na values"""
        #self._my_data_set.replace({pd.NA: pd.NaT}, inplace = True)
        self._my_data_set.dropna(axis="columns", inplace=True)

    def __str__(self):
        """The __str__() method is defined to return a string representation 
        of the instance in a human-readable format
        """
        result = self._my_data_set.to_string(index = False)
        return result

    def __repr__(self):
        """the __repr__() method is defined to return a string representation 
        of the instance that can be used to recreate the object
        """
        return f'CSVDataset("{self.src_filename}", "{self.target_filename}")'
