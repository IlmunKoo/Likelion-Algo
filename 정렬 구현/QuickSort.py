def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lessArr, equalArr, greatArr = [], [], []
    for num in arr:
        if num < pivot:
            lessArr.append(num)
        elif num > pivot:
            greatArr.append(num)
        else:
            equalArr.append(num)

    return QuickSort(lessArr) + equalArr + QuickSort(greatArr)

arr = [100, 20, 60, 50, 70, 90, 80, 40, 30, 10]

print(QuickSort(arr))