def waterCollection(arr):

    waterSum = 0
    leftPointer = 0
    rightPointer = len(arr) -1
    leftMax = arr[0]
    rightMax = arr[-1]

    while leftPointer < rightPointer:

        if leftMax < rightMax:
            waterSum += leftMax - arr[leftPointer]
            leftPointer += 1
            leftMax = max(leftMax, arr[leftPointer])
        
        else:
            waterSum += rightMax - arr[rightPointer]
            rightPointer -= 1
            rightMax = max(rightMax, arr[rightPointer])

    return waterSum


if __name__ == '__main__':

    print(waterCollection(y))
