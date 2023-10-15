def equalizeArray(arr):
    d = {}
    len_arr = len(arr)
    for items in arr:
        d[items] = arr.count(items)
    return len_arr - max(max(d.values()),0)