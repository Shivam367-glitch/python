#linear searchng in array

# if element found in array the function return index of array if not then `return -1


def linear_Search(arr,key)->int:
    n=len(arr)
    for i in range(n):
        if arr[i] is key:
            return i
        
    
    return -1



if __name__=="__main__":
    arr=[1,2,3,45,6,7,89,9,0,2221,32,23213,244,22122,222143,3221,3332,45,678,4,4555,4544]
    
    index=linear_Search(arr,4)
    index1=linear_Search(arr,100)
    if index ==-1:
        print("Number is not found in the array")
    else:
        print("Number found in the index:",index)
        
    if index1 ==-1:
        print("Number is not found in the array")
    else:
        print("Number found in the index:",index1)
        
        


