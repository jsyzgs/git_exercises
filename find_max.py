import numpy as np

def find_max(array):
    return np.max(array)

if __name__ == '__main__':
    list_ = [1,2,3,4,5]
    result = find_max(list_)
    print(result)