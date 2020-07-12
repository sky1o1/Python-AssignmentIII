import sys

# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.

# a) Bubble Sort

# def bubble(bub):
#     bub_len = len(bub)
#     new_bub = []
#     for i in range(bub_len):
#         for j in range(bub_len - 1):
#             if bub[j] > bub[j + 1]:
#                 bub[j], bub[j + 1] = bub[j + 1], bub[j]
#             else:
#                 pass
#     return bub
#
#
# bub_list = [1, 4, 6, 2, 8, 3, 10]
# print(bubble(bub_list))

# b) Insertion Sort

# def insertion(ins):
#     ins_len = len(ins)
#     for i in range(1, ins_len):
#         num = ins[i]
#         j = i - 1
#         while j >= 0 and num < ins[j]:
#             ins[j + 1] = ins[j]
#             j -= 1
#         ins[j + 1] = num
#
#
# ins_list = [1, 4, 6, 2, 8, 3, 10]
# insertion(ins_list)
# print(ins_list)

# c) Quick Sort

# def quick(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end
#
#     while True:
#
#         while low <= high and array[high] >= pivot:
#             high = high - 1
#
#         while low <= high and array[low] <= pivot:
#             low = low + 1
#
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#
#         else:
#
#             break
#
#     array[start], array[high] = array[high], array[start]
#
#     return high
#
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     p = quick(array, start, end)
#     quick_sort(array, start, p - 1)
#     quick_sort(array, p + 1, end)
#
#
# array = [1, 4, 6, 2, 8, 3, 10]
# print(array)
#
# quick_sort(array, 0, len(array) - 1)
# print(array)

# d) Merge Sort

# def merge(list):
#     if len(list) > 1:
#         mid = len(list) // 2
#         Lmid = list[:mid]
#         Rmid = list[mid:]
#
#         merge(Lmid)
#         merge(Rmid)
#         i = j = k = 0
#         while len(Lmid) > i and len(Rmid) > j:
#             if Lmid[i] < Rmid[j]:
#                 list[k] = Lmid[j]
#                 i = i + 1
#             else:
#                 list[k] = Rmid[j]
#                 j = j + 1
#             k = k + 1
#         while i < len(Lmid):
#             list[k] = Lmid[i]
#             i = i + 1
#             k = k + 1
#
#         while j < len(Rmid):
#             list[k] = Rmid[j]
#             j = j + 1
#             k = k + 1
#     return (list)
#
#
# list = []
# n = int(input(" enter the number of item in the list : "))
# for i in range(0, n):
#     element = int(input("enter number: "))
#     list.append(element)
# print("sorted list")
# print(merge(list))


# e) Linear Search


# def linear(list):
#     for i in range(len(list)):
#         if x == list[i]:
#             print("The index is ", i)
#     return -1
#
# list = []
# n = int(input(" enter the number of item in the list : "))
#
# x = int(input(" enter the number you want to search for : "))
# for i in range(0, n):
#     element = int(input("enter number: "))
#     list.append(element)
# print(list)
# print(linear(list))


# f) Binary Search

# def binary(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#
#     while low <= high:
#
#         mid = (high + low) // 2
#
#         if arr[mid] < x:
#             low = mid + 1
#
#         elif arr[mid] > x:
#             high = mid - 1
#
#         else:
#             return mid
#
#     return -1
#
#
# arr = []
# n = int(input(" enter the number of item in the list : "))
# for i in range(0, n):
#     element = int(input("enter number: "))
#     arr.append(element)
# x = int(input(" enter the item in the list  to find : "))
#
# result = binary(arr, x)
#
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")

# g) Interpolation Search

# def interpolation(list, index):
#     (left, right) = (0, len(list) - 1)
#
#     while list[right] != list[left] and list[left] <= index <= list[right]:
#         mid = left + (index - list[left]) * (right - left) // (list[right] - list[left])
#         if index == list[mid]:
#             return mid
#
#         elif index < list[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     if index == list[left]:
#         return left
#     return -1
#
#
# list = []
# n = int(input(" enter the number of item in the list : "))
# for i in range(0, n):
#     element = int(input("enter number: "))
#     list.append(element)
# key = int(input("enter the key to search for : "))
# print(list)
# index = interpolation(list, key)
#
# if index != -1:
# 	print("Element found at index", index)
# else:
# 	print("Element found not in the list")


# h) Dijkstra’s Algorithm

# vertices = [[0, 0, 1, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 1, 0],
#             [1, 1, 0, 1, 1, 0, 0],
#             [1, 0, 1, 0, 0, 0, 1],
#             [0, 0, 1, 0, 0, 1, 0],
#             [0, 1, 0, 0, 1, 0, 1],
#             [0, 0, 0, 1, 0, 1, 0]]
#
# edges = [[0, 0, 1, 2, 0, 0, 0],
#          [0, 0, 2, 0, 0, 3, 0],
#          [1, 2, 0, 1, 3, 0, 0],
#          [2, 0, 1, 0, 0, 0, 1],
#          [0, 0, 3, 0, 0, 2, 0],
#          [0, 3, 0, 0, 2, 0, 1],
#          [0, 0, 0, 1, 0, 1, 0]]
#
#
# def to_be_visited():
#     global visited_and_distance
#     v = -10
#     for index in range(num_of_vertices):
#         if visited_and_distance[index][0] == 0 \
#                 and (v < 0 or visited_and_distance[index][1] <=
#                      visited_and_distance[v][1]):
#             v = index
#     return v
#
#
# num_of_vertices = len(vertices[0])
#
# visited_and_distance = [[0, 0]]
# for i in range(num_of_vertices - 1):
#     visited_and_distance.append([0, sys.maxsize])
#
# for vertex in range(num_of_vertices):
#
#     to_visit = to_be_visited()
#     for neighbor_index in range(num_of_vertices):
#
#         if vertices[to_visit][neighbor_index] == 1 and \
#                 visited_and_distance[neighbor_index][0] == 0:
#             new_distance = visited_and_distance[to_visit][1] \
#                            + edges[to_visit][neighbor_index]
#             if visited_and_distance[neighbor_index][1] > new_distance:
#                 visited_and_distance[neighbor_index][1] = new_distance
#
#         visited_and_distance[to_visit][0] = 1
#
# i = 0
#
# for distance in visited_and_distance:
#     print("Distance of ", chr(ord('a') + i),
#           " from source vertex: ", distance[1])
#     i = i + 1


# i) Tower of Hanoi problem for ‘n’ number of disks.

def TowerOfHanoi(n, source, target, midway):
    if n == 1:
        print("Move disk 1 source", source, "to target", target)
        return
    TowerOfHanoi(n - 1, source, midway, target)
    print("Move disk", n, "from source", source, "to target", target)
    TowerOfHanoi(n - 1, midway, target, source)

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')