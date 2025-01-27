"""Reader Factory logic"""
from readers import _csv_reader, _database_reader, _json_reader

class ReaderFactory():
    """Reader factory implementation"""
    @staticmethod
    def get_reader(reader_type: str):
        """Get the reader object based on class"""
        #static method that returns the reader based on the type that is passed
        if reader_type == "CSV":
            return _csv_reader
        if reader_type == "JSON":
            return _json_reader
        if reader_type == "DB":
            return _database_reader

        raise TypeError("Unsuported reader")
