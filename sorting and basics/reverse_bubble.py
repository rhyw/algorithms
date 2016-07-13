#!/usr/bin/env python

def reverse_bubble_sort(arr):
    # For a n-length array, (n-1) loop is needed.
    print "Original array: {}".format(arr)
    for i in range(len(arr)-1):
        # Each loop moves the smallest item to left.
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print "After loop {}: {}".format(i, arr)

if __name__ == '__main__':
    l = [144, 233, 5, 8, 21, 13, 55, 34, 89, 2, 3]
    reverse_bubble_sort(l)

    # Worse case
    ll = range(30, 10, -3)
    reverse_bubble_sort(ll)
