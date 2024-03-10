from bubbleSort import print_array

def quick_sort(arr,low,high):
    
    if low<high:
        partition=getPartition(arr,low,high)
        quick_sort(arr,low,partition-1)
        quick_sort(arr,partition+1,high)
        
        
    
    
    
def getPartition(arr,low,high):
    
    i=low
    j=high
    pivot=low
    
    while(i<j):
        while arr[i]<=arr[pivot] and i<=high-1:i+=1
        while arr[j]>arr[pivot]  and j>=low+1:j-=1
        if i<j:arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    
    return j
        
    
if __name__=="__main__":
     arr=[2,9,1,3,4,7]
     print("Before Sorting is:")
     print_array(arr)
     quick_sort(arr,0,5)
     print("\nAfter Sorting is:")
     print_array(arr)    
    
    
    
    
    