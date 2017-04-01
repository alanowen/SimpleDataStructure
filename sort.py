import random
import time

def timer(func):
    def _wrapper(sequence):
        print(time.ctime())
        func(sequence)
        print(time.ctime())
    return _wrapper


@timer
def insert_sort(sequence):
    i = 1
    while i < len(sequence):
        if sequence[i] < sequence[i-1]:
            d = sequence[i]
            sequence[i] = sequence[i-1]
            j = i - 1
            while d < sequence[j] and j >= 0:
                sequence[j+1] = sequence[j]
                j -= 1
            sequence[j+1] = d
        i += 1


@timer
def bi_insert_sort(sequence):
    i = 1
    while i < len(sequence):
        d = sequence[i]
        low, high = 0, i-1
        while low <= high:
            m = int((low + high)//2)
            if sequence[m] < d:
                low = m+1
            else:
                high = m-1
        j = i - 1
        while j >= high:
            sequence[j+1] = sequence[j]
            j -= 1
        sequence[high+1] = d
        i += 1


@timer
def shell_insert_sort(sequence):
    pass


if __name__ == '__main__':

    l = list(range(10000, 0, -1))
    insert_sort(l)
    bi_insert_sort(l)
