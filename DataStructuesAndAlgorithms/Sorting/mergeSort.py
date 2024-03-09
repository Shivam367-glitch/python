from bubbleSort import print_array

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)
    


def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    k = l
    ans = [0] * (r + 1)
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            ans[k] = arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        ans[k] = arr[i]
        i += 1
        k += 1

    while j <= r:
        ans[k] = arr[j]
        j += 1
        k += 1

    for x in range(l, r + 1):
        arr[x] = ans[x]           
            
    
if __name__=="__main__":
     arr=[2,9,1,3,4,7]
     print("Before Sorting is:")
     print_array(arr)
     merge_sort(arr,0,5)
     print("\nAfter Sorting is:")
     print_array(arr)    
    