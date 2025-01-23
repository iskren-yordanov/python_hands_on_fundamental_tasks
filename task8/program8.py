"""main entry point for task 8"""
import importlib
my_import = importlib.import_module("data-helper")

def main():
    """Main functionality"""
    rand_date = getattr(my_import, "get_random_date")
    rand_str = getattr(my_import, "get_random_string")
    rand_int = getattr(my_import, "get_random_integer")
    rand_double = getattr(my_import, "get_random_double")
    print(rand_date())
    print(rand_str())
    print(rand_int())
    print(rand_double())

if __name__=="__main__":
    main()
