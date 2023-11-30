import numpy as np

random = True;

if( random == False ):
    arr=[40,60,70,50,10,20,30]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)
print("INPUT:  ", arr ) 

ascending = False;

def insertionSorting( arr, ascending ):
    # double for문,  with i, j variables
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            print("i 번째", i, ", j 인덱스 ", j )

            comp = arr[j-1] > arr[j];
            #print("comp =",)
            
            #if arr[j-1] > arr[j]:
            ##if arr[j-1] < arr[j]:
            if( (ascending==True and comp==True ) or ( ascending==False and comp==False  )):
                arr[j], arr[j-1] = arr[j-1], arr[j]

            print("Inner Result: ", arr )
        print(">>Partial Result: ", arr )

    print(">>>> Final Result ", arr )


    # while문 and without j variable
    print("\n\n while문 사용")

    if( random == False ):
        arr=[40,60,70,50,10,20,30]

    for i in range(1,len(arr)):
        
        #while i>0 and arr[i-1] > arr[i]:
        while i>0:
            comp = arr[i-1] > arr[i]            
            if( (ascending==True and comp==True ) or ( ascending==False and comp==False  )):
                arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1

    print(arr)
    return arr



result = insertionSorting(arr, True)
print("RESULT: ", result)


