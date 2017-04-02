import random
import time
import asyncio

def timer(func):
    def _wrapper(*args):
        print(time.ctime())
        func(*args)
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
def shell_sort(sequence):
    step = int(len(sequence) // 2)
    while step > 0:
        i = 0
        j = step + i
        while j < len(sequence):
            h = j
            while h >= 0 and sequence[i] > sequence[h]:
                sequence[i], sequence[h] = sequence[h], sequence[i]
                h -= 1
            i += 1
            j += 1
        step = int(step//2)


@timer
def bubble_sort(sequence):
    i, l = 0, len(sequence)
    while i < l-1:
        j = 0
        while j < l-i-1:
            if sequence[j] > sequence[j+1]:
                sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
            j += 1
        i += 1


@timer
def quick_sort(sequence):
    def _partion(sequence, low, high):
        pivot = sequence[low]
        while low < high:
            while low < high and sequence[high] >= pivot:
                high -= 1
            sequence[low] = sequence[high]
            while low < high and sequence[low] <= pivot:
                low += 1
            sequence[high] = sequence[low]
        sequence[low] = pivot
        return low

    def _quick_sort(sequence, low, high):
        if low < high:
            pivotloc = _partion(sequence, low, high)
            _quick_sort(sequence, pivotloc-1, high)
            _quick_sort(sequence, pivotloc+1, high)

    _quick_sort(l, 0, len(l)-1)


if __name__ == '__main__':

    # l = list(range(10000, 0, -1))
    # insert_sort(l)
    # l = list(range(10000, 0, -1))
    # l = list(range(10000, 0, -1))
    # bi_insert_sort(l)
    l = list(range(3, 0, -1))
    quick_sort(l)
