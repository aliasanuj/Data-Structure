============================
Python - Sorting Algorithms
============================
1. Sorting refers to arranging data in a particular format. 
Sorting algorithm specifies the way to arrange data in a particular order. 
Most common orders are in numerical or lexicographical order.

2. The importance of sorting lies in the fact that data searching can be optimized to a very high level, 
if data is stored in a sorted manner. Sorting is also used to represent data in more readable formats. 
Below we see five such implementations of sorting in python.

1. Bubble Sort
2. Merge Sort
3. Insertion Sort
4. Shell Sort
5. Selection Sort

==============================
==============================
1. Bubble Sort :
==============================
==============================
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

array = [1,14,12,54,67,28,61,27,34,62]
list1 = bubbleSort(array)
print(list(list1))
#[1, 12, 14, 27, 28, 34, 54, 61, 62, 67]
=====================
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

array = [1,14,12,54,67,28,61,27,34,62]
list1 = bubbleSort(array)
print(list(list1))
#[67, 62, 61, 54, 34, 28, 27, 14, 12, 1]
========================
def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
				
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
#[17, 20, 26, 31, 44, 54, 55, 77, 93]
==============================
def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] < alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
				
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
#[93, 77, 55, 54, 44, 31, 26, 20, 17]
=============================
=============================
2. Merge sort :
=============================
=============================
1. Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two 
halves and then merges the two sorted halves. The merge() function is used for merging two halves.

2. Merge sort is a perfectly elegant example of a Divide and Conquer algorithm. It simple uses the 2 main steps of such an algorithm:

==> Continuously divide the unsorted list until you have N sublists, where each sublist has 1 element that is “unsorted” and N is the 
number of elements in the original array.
==> Repeatedly merge i.e conquer the sublists together 2 at a time to produce new sorted sublists until all elements have been fully 
merged into a single sorted array.

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf ,righthalf = alist[:mid], alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        return alist
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
#[17, 20, 26, 31, 44, 54, 55, 77, 93]

=============================
=============================
3. Insert sort :
=============================
=============================
Insertion sort is both faster and well-arguably more simplistic than both bubble sort and selection sort. Funny enough, it’s 
how many people sort their cards when playing a card game! On each loop iteration, insertion sort removes one element from the array.
It then finds the location where that element belongs within another sorted array and inserts it there. It repeats this process until
no input elements remain.

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        while i > 0 and arr[i - 1] > cursor:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = cursor
    return arr

arr = [4,7,8,9,6,5]
insertion_sort(arr)
print(arr)
#[4, 5, 6, 7, 8, 9]

=============================
=============================
4. Shell sort :
=============================
=============================

http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html

ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has 
to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. In shellSort, we make the 
array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all 
sublists of every h’th element is sorted.


def shellSort(arr):
    # Start with a big gap, then reduce the gap
    mid = len(arr) // 2
    while mid > 0:
        for i in range(mid, len(arr)):
            temp = arr[i]
            j = i
            while j >= mid and arr[j - mid] > temp:
                arr[j] = arr[j - mid]
                j -= mid

            arr[j] = temp
        mid //= 2

arr = [1,4,7,8,9,5,6,3]
shellSort(arr)
print(arr)
#[1, 3, 4, 5, 6, 7, 8, 9]

=============================
=============================
5. Selection sort :
=============================
=============================

Selection sort is also quite simple but frequently outperforms bubble sort. If you are choosing between the two, it’s best to just 
default right to selection sort. With Selection sort, we divide our input list / array into two parts: the sublist of items already 
sorted and the sublist of items remaining to be sorted that make up the rest of the list. We first find the smallest element in the 
unsorted sublist and place it at the end of the sorted sublist. Thus, we are continuously grabbing the smallest unsorted element and 
placing it in sorted order in the sorted sublist. This process continues iteratively until the list is fully sorted.

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr
arr = [1,4,7,5,8,9,3,2]
selection_sort(arr)
print(arr)
#[1, 2, 3, 4, 5, 7, 8, 9]
