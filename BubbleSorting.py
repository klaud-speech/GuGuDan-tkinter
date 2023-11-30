import numpy as np

def BubbleSorting( arr, descending = False ):
    # acending
    for i in range( len(arr)-1, 0, -1):    # number of pairs.    
        for j in range(i):
            print( "i=", i, "j=", j )
            #if arr[j] > arr[j+1]:           # comparision 
            #if arr[j] < arr[j+1]:           # comparision 
            comp = arr[j] > arr[j+1]
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
                arr[j], arr[j+1]   = arr[j+1], arr[j]   #swap 
            print(" Inner Result: ", arr )
        
        print(" >> Partial Result: ", arr )

    print(">>>> Final Result: ", arr )
    return arr

###############################


random = True;
if( random == False ):
    arr = [40, 70, 60, 30, 10, 50]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)

print("INPUT:  ", arr )

result = BubbleSorting( arr, descending = False )
print(":::::::::: RESULT: ", result)



