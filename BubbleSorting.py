import numpy as np

random = True;

if( random == False ):
    arr = [40, 70, 60, 30, 10, 50]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)

print("INPUT:  ", arr )



def BubbleSorting( data ):
    # acending
    for i in range( len(arr)-1, 0, -1):    # number of pairs.    
        for j in range(i):
            print( "i=", i, "j=", j )
            if arr[j] > arr[j+1]:           # comparision 
                arr[j], arr[j+1]   = arr[j+1], arr[j]   #swap 
            print(" Inner Result: ", arr )
        
        print(" >> Partial Result: ", arr )

    print(">>>> Final Result: ", arr )
    return arr



result = BubbleSorting( arr)
print("\n\nResult :",  result )


