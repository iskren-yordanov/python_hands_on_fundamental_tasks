"""main entry point for task 9"""
from reader_factory import ReaderFactory

def main():
    """Main functionality"""
    my_factory = ReaderFactory().get_reader("CSV")
    my_factory.location = "task9/"
    my_factory.name = "employement-data.csv"
    my_factory.read()
    my_factory.show_head_data()

    my_factory = ReaderFactory().get_reader("JSON")
    my_factory.location = "task9/"
    my_factory.name="example_2.json"
    my_factory.read()
    my_factory.show_head_data()

    # I did not fully understand what is wanted in this task to be honest

if __name__=="__main__":
    main()
