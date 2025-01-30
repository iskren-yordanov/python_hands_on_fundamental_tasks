"""Main entry point for task 10"""
from dataset import JSONDataset, CSVDataset
from custom_library import Source, Sink, WaitActivity, CopyActivity, Pipeline

def main():
    src: Source = Source(JSONDataset('task10/users_1k.json'))
    sink: Sink = Sink(CSVDataset('task10/users_1k.csv'))

    wait = WaitActivity(5)
    copy = CopyActivity(src, sink)

    #src.Dataset.get_data()
    #src.Dataset.preview()

    pl = Pipeline()
    pl.add_activity(wait)
    pl.add_activity(copy)

    pl.execute()

if __name__ == "__main__":
    main()