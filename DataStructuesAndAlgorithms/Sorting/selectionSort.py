
from bubbleSort import print_array

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
            
        if min !=i:
            arr[min],arr[i]=arr[i],arr[min]


# select min element from unstored and put in sorted part of the array..



if __name__=="__main__":
     arr=[2,9,1,3,4,7]
     print("Before Sorting is:")
     print_array(arr)
     selection_sort(arr)
     print("\nAfter Sorting is:")
     print_array(arr)
    
        
    