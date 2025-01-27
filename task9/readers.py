"""READERS logic"""
import pandas as pd
import read

class CSVReader(read.Reader, read.ObjectParameters):
    """CSV Reader implementation"""
    def show_head_data(self):
        """Method returns first 20 elements of the head of the dataframe"""
        print(self._my_data_set.head(20))

    def read(self):
        """reads the contents of a csv file and returns it as pandas dataframe"""
        if self.location != "" and self.name != "":
            full_name = self.location +  self.name
            print(full_name)
            with open(full_name,  'r', encoding = 'utf=8') as file:
                self._my_data_set = pd.read_csv(file)

class JSONReader(read.Reader, read.ObjectParameters):
    """JSON Reader implementation"""
    def show_head_data(self):
        """Method returns first 20 elements of the head of the dataframe"""
        print(self._my_data_set.head(20))

    def read(self):
        """reads the contents of a json file and returns it as pandas dataframe"""
        if self.location != "" and self.name != "":
            full_name = self.location +  self.name
            print(full_name)
            with open(full_name,  'r', encoding = 'utf=8') as file:
                self._my_data_set = pd.read_json(file)

class DatabaseReader(read.Reader, read.ObjectParameters):
    """Database Reader implementation"""
    def read(self):
        """reads a table from a db of your choice and returns it as pandas dataframe"""
        #FUTURE work

_csv_reader = CSVReader()
_json_reader = JSONReader()
_database_reader = DatabaseReader()
