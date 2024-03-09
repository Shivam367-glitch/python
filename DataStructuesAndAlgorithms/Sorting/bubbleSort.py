def bubble_sort(arr):
      n=len(arr)
      for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
              if arr[j]>arr[j+1]:
                  arr[j],arr[j+1]=arr[j+1],arr[j]
                  swapped=True


def print_array(arr):
    n=len(arr)
    
    for i in range(n):
        print(arr[i],end=" ")

    
    

if __name__=="__main__":
     arr=[12,1,23,12,1,23,134,56,3,7652,77,5,44,5,6,44,4]
     print("Before Sorting is:")
     print_array(arr)
     bubble_sort(arr)
     print("\nAfter Sorting is:")
     print_array(arr)
    