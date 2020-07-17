def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lessArr, equalArr, greatArr = [] ,[], []
    for num in arr:
        if num < pivot:
            lessArr.append(num)
        elif num > pivot:
            greatArr.append(num)
        else:
            equalArr.append(num)
    return QuickSort(lessArr) + equalArr + QuickSort(greatArr)

arr = [100, 30 , 20, 40, 70, 60, 90, 50, 80, 10]
print(QuickSort(arr))

