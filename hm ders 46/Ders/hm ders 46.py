# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = [j + 1], arr[j]
#                 return arr
            
# arr = [65, 43, 32, 54, 65, 90]
# print("sıralanmış dizi:", bubble_sort(arr))

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
# arr = [64, 25, 12, 33 ,12]
# print("sıralanmış dize:", selection_sort(arr))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             arr[j + 1] = key
#     return arr
# arr = [12, 11, 13, 5, 7]
# print("sıralanmış dize:", insertion_sort(arr))

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L)
#         merge_sort(R)
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i +=1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i +=1
#             k +=1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k +=1
#     return arr
# arr = [38, 21, 32, 43, 54, 10]
# print("Sıralamış dize", merge_sort(arr))

# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     pivot = arr[len(arr)// 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# arr = [10, 32, 32, 43]
# print("sıralanmış dizi:", quick_sort(arr))
# import time
# def linear_search(arr, x):
#     start_time = time.time()
#     for i in range(len(arr)):
#         if arr[i] == x:
#             end_time = time.time()
#             elapsed_time = end_time - start_time
#             print(str(start_time))
#             print(str(elapsed_time))
#             return i
#     return -1
# arr = [32, 34, 54, 154, 3, 534, 43, 32]
# x = 123
# print("eleman indexi:", linear_search(arr, x))

# def binary_search(arr, low, hight, x):
#     if hight >= low:
#         mid = (hight + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid -1, x)
#         else:
#             return binary_search(arr, mid + 1, hight, x)
#     else:
#         return -1
    
# arr = [2, 3, 4, 10, 50]
# x = 10
# result = binary_search(arr, 0, len(arr) - 1, x)
# print("Eleman indeksi:", result)
