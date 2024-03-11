import bisect

def binarySearch(mat, n, target):
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is at the start or end of the row
        if mat[mid][0] == target or mat[mid][n-1] == target:
            # print(mid)
            return mid
        # Check if target lies within the range of the row
        elif mat[mid][0] < target and mat[mid][n-1] > target:
            # Perform binary search on the row
            if bisect.bisect_left(mat[mid], target) < n:
                return mid
            else:
                return -1
        elif mat[mid][0] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    mat = [[1, 5, 6], [8, 10, 11], [15, 16, 18]]
    ans = binarySearch(mat, 3, 18)
    
    print(ans)  # Output: 2 (index of the row containing 18)
