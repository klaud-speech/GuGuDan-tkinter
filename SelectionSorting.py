import numpy as np

random = True;

if(random == False ):
    arr = [40, 70, 60, 30, 10, 50]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)

print("INPUT:  ", arr ) 




print( " Initial Status = ", arr)
for i in range(len(arr)-1):
    print( "i = ", i)
    small_idx = i
    for j in range(i+1, len(arr)):     #comparion 
        print( small_idx)
        if arr[small_idx]>arr[j]:
            small_idx = j
    arr[i], arr[small_idx] = arr[small_idx], arr[i]   #swap    
    print( " small_idx = ", small_idx )
    print( "  Partial Result = ", arr)

print("Final: ")
print(arr)
