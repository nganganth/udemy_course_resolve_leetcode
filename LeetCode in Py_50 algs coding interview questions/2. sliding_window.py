
def maxSum(arr, windowSize):
    arrSize = len(arr)
    if (arrSize <= windowSize):
        print("Invalid operation")
        return -1
    
    win_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = win_sum

    for i in range(arrSize - windowSize):
        win_sum = win_sum - arr[i] + arr[i + windowSize]
        max_sum = max(win_sum, max_sum)
    return max_sum

arr = [80, -50, 90, 100]
k = 2
answer = maxSum(arr, k)
print(answer)