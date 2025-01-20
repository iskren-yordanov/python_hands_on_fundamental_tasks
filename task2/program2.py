"""entry point for task2"""

def sub_task_1(sentence: str) -> list:
    """task 2 sub task 1"""
    word_list = sentence.split()

    # does this count as a lambda ?
    new_list = [[x, str.upper(x), str.lower(x), len(x)] for x in word_list]

    #tr = lambda x: [x, str.upper(x), str.lower(x), len(x)]
    #for w in word_list:
        #new_list.append(tr(w))
    #    new_list.append(lambda w: [w, str.upper(w), str.lower(w), len(w)])
    #new_list = list(map(lambda x: [x, str.upper(x), str.lower(x), len(x)], word_list))

    return new_list

def sub_task_2(sentence: str) -> list:
    """task 2 sub task 2"""
    word_list = sentence.split()
    new_list = list(map(lambda x: [str.upper(x), str.lower(x), len(x)], word_list))
    return new_list

def sub_task_3(lst_a: list, lst_b: list) -> list:
    """task 2 sub task 3"""
    x = lambda b,c: set(b) & set(c)
    return sorted(list(x(lst_a, lst_b)))[::-1]

    #using lambda directly
    #return sorted(list((lambda a,b: set(a) & set(b))(lst_a, lst_b)))[::-1]

def sub_task_4(sentence: str) -> list:
    """task 2 sub task 4"""
    word_list = sentence.split()
    word_list.sort(key=lambda x: str.lower(x[len(x)-1]))
    return word_list

if __name__ == "__main__":
    SENTENCE = 'This is a lAmBdA FuNction task'
    A = [1, 11, 23, 44, 16]
    B = [2, 3, 5, 6, 7, 8, 44, 16]

    print(sub_task_1(SENTENCE))
    print(sub_task_2(SENTENCE))
    print(sub_task_3(A, B))
    print(sub_task_4(SENTENCE))
    