"""Main entry point for task 6"""

from csv_dataset import CSVDataset

def main():
    """Main functionality"""
    ds_csv = CSVDataset('employement-data.csv', 'test.csv')
    ds_csv.show_head_data()
    ds_csv.save_data()
    ds_csv.target_filename = "test2.csv"
    ds_csv.save_data()
    print(repr(ds_csv))
    print(str(ds_csv))

if __name__=="__main__":
    main()
