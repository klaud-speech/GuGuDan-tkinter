import numpy as np

def insertionSorting( arr, descending ):
    # double for문,  with i, j variables
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            print("i 번째", i, ", j 인덱스 ", j )

            comp = arr[j-1] > arr[j];
            #print("comp =",)
            
            #if arr[j-1] > arr[j]:  높은 순서로
            #if arr[j-1] < arr[j]:  
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
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
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
                arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1

    print(">>>> FinalResult : " , arr)
    return arr




random = True;
if( random == False ):
    arr=[40,60,70,50,10,20,30]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)
print("INPUT:  ", arr ) 


result = insertionSorting(arr, descending=False)
print(":::::::::: RESULT: ", result)


