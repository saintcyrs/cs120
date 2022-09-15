from array import array
from asyncio import base_tasks
from cmath import log
from ctypes import sizeof
import math
import time
import random
from tkinter import N

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

"""def radixSort(U, b, arr):
    k = math.ceil(math.log(U)/math.log(b))
    n = len(arr)
    V = []
    for i in range(n-1):
        V.append(tuple((arr[0][i], (BC(arr[0][i], b, k)))))
    return i
print(radixSort(100, 10, [(14, "A"), (2, "B")]))"""

def radixSort(U, b, A) :
    n = len(A)
    k = math.ceil( (math. log (U)/math. log (b)). real)
    V_p = []
    for x in A:
        V_p.append (BC (x[0], b, k))
    A_2 = [[x, [y, v]] for [x, y], v in zip(A, V_p)]
    for i in range(k) :
        for j in range(n) :
            A_2[j][0] = A_2[j][1][1][i]
        A_2 = countSort (U, A_2)
    for i in range(n):
        ki = 0
        for j in range(k):
            ki += A_2[i][1][1][j] * (b ** j)
        A_2[i] = [ki, A_2[i][1][0]]
    return A_2

nput_data = [(100, 'A'), (34, 'B'), (45, 'C'), (83, 'D'), (10, 'E')]

def experiment():
    for trial in range(10):
        n = random.randint(2, 2**16)
        U = random.randint(2, 2**20)
        arr = []

        for i in range(n):
            arr.append((random.randint(1, U-1),i))

        t0 = time.time()
        countSort(U, arr)
        t1 = time.time()
        count = (t1 - t0)

        t2 = time.time()
        mergeSort(arr)
        t3 = time.time()
        merge = (t3-t2)

        t4 = time.time()
        radixSort(U, n, arr)
        t5 = time.time()
        radix = (t5-t4)

        print("n: ",n, end ='\n')
        print("U: ", U, end = '\n')
        print("CountSort Avg Time: ", count, end = '\n')
        print("MergeSort Avg. Time: ", merge, end = '\n')
        print("RadixSort Avg. Time: ", radix, end = '\n')
    return ()

experiment()