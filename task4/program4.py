"""entry point for task4"""

# 1. Split decorator
def split_decorator(func):
    """Split decorator"""
    #print("split_decorator")

    def splitter(*args, **kwargs):
        data = func(*args, **kwargs)
        return data.split()

    return splitter

# 2. Upper case decorator
def uppercase_decorator(func):
    """Uppercase decorator"""
    #print("uppercase decorator")

    def upper_case(*args, **kwards):
        data = func(*args, **kwards)
        new_data = list(x.upper() for x in data)
        return new_data

    return upper_case

# 3. Filter decorator
def filter_decorator(func):
    """Filter decorator"""
    #print("fitler decorator")

    def filter_more_than_4_chars(*args, **kwards):
        data = func(*args, **kwards)
        new_data = []
        for d in data:
            if len(d) > 4:
                new_data.append(d)
        return new_data

    return filter_more_than_4_chars



# decorators are from bottom to top (closes to the def of the function is first)
# order matters since they are all enrapped so they are connected in a way
@filter_decorator
@uppercase_decorator
@split_decorator
def get_data(data):
    """test function that we want to decorate"""
    return data

if __name__ == "__main__":
    DATA = 'This is An exAmPlE StRinG'
    print(get_data(DATA))
