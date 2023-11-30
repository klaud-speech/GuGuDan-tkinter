import numpy as np

def  selectionSorting(arr, descending = False):
    print( " Initial Status = ", arr)
    for i in range(len(arr)-1):
        print( "i = ", i)
        small_idx = i
        for j in range(i+1, len(arr)):     #comparion 
            print( small_idx)
            #if arr[small_idx]>arr[j]:
            #if arr[small_idx]<arr[j]:
            comp = arr[small_idx]>arr[j]
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
                small_idx = j
        arr[i], arr[small_idx] = arr[small_idx], arr[i]   #swap    
        print( " small_idx = ", small_idx )
        print( "  Partial Result = ", arr)

    print("Final: ")
    print(arr)
    return arr

#################

random = True;
if(random == False ):
    arr = [40, 70, 60, 30, 10, 50]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)

print("INPUT:  ", arr ) 

result = selectionSorting(arr, descending=False)
print(":::::::::: RESULT: ", result)

