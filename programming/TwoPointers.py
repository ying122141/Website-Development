def waterCollection(arr):

    waterSum = 0
    leftPointer = 0
    rightPointer = len(arr) -1

    # leftMax is the starting item
    leftMax = arr[0]

     # righttMax is the last item
    rightMax = arr[-1]

    # When two pointers do not meet yet
    while leftPointer < rightPointer:
        
        # Same as min(left, high) but if-then version
        if leftMax < rightMax:

            # If leftMax is min, the maximam water can be held 
            # must be at most height of min - arr[i]
            waterSum += leftMax - arr[leftPointer]

            # Move the pointer
            leftPointer += 1

            # Find the new max
            leftMax = max(leftMax, arr[leftPointer])
        
        else:
            # Same logic as left side
            waterSum += rightMax - arr[rightPointer]
            rightPointer -= 1
            rightMax = max(rightMax, arr[rightPointer])

    return waterSum


if __name__ == '__main__':

    print(waterCollection(y))
