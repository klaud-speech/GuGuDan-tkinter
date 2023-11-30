arr=[40,60,70,50,10,20,30]

for i in range(1,len(arr)):
    for j in range(i, 0, -1):
        print("i 번째", i, ", j 인덱스 ", j )
        if arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        print("Inner Result: ", arr )
    print(">>Partial Result: ", arr )

print(">>>> Final Result ", arr )

