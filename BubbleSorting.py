
arr = [40, 70, 60, 30, 10, 50]

# acending
for i in range( len(arr)-1, 0, -1):    # number of pairs
    for j in range(i):
        print( "i=", i, "j=", j )
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1]   = arr[j+1], arr[j]
        print(" Inner Result: ", arr )
    
    print(" >> Partial Result: ", arr )

print(">>>> Final Result: ", arr )

