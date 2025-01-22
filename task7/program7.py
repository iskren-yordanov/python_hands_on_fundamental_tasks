"""Main entry point for task 7"""
from distance import Distance

def main():
    """main functionality"""
    dist_a = Distance(1, 55, 44)
    dist_b = Distance(3, 0, 0)

    dist_c = dist_a + dist_b

    print(dist_a)
    print(dist_b)
    print(dist_c)

    try:
        #dist_d = dist_a - dist_b
        #print(dist_d)
        dist_e = dist_a - dist_a
        print(dist_e)

    except ValueError as ve:
        print(ve)

    dist_b += dist_a
    print(dist_b)

if __name__=="__main__":
    main()
