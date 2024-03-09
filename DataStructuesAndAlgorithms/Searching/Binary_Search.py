def Binary_Search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) 
        if arr[mid] == key:
            # key found at index mid
            return mid  
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Key not found


if __name__=="__main__":
    arr=[1,201,21,221,10,98,43,254,342,4234,9,8,7,6,5]
    sorted(arr)
    index= Binary_Search(arr, 1)
    index1= Binary_Search(arr, 100)
    
    if index ==-1:
        print("Key is Not Found:")
    else:
        print("Key Found at index:",index)
    
    
    if index1 ==-1:
        print("Key is Not Found:")
    else:
        print("Key Found at index:",index1)