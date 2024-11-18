def bob_sort(arr: list):
    lenth = arr.__len__()
    for i in range(lenth):
        for j in range(0, lenth-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


a = [i for i in range(10)]
print(a)
# arr = [3,1,2]
# bob_sort(arr)
# print(arr)