from bubbleSort import print_array

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
        
        
# take element from unsorted element and find place of current element in sorted array
if __name__=="__main__":
     arr=[2,9,1,3,4,7]
     print("Before Sorting is:")
     print_array(arr)
     insertion_sort(arr)
     print("\nAfter Sorting is:")
     print_array(arr)