arr=[40,70,60,30,10,50,90,80,20]

def big_heap (a,b, descending=False):   #최대힙
    for j in range(1,b+1):
        print("\t j =", j)
        c=j 
        while c!=0:
            r=(c-1)//2
            print("\t\t r=", r)
            #if a[r]<a[c]:   #최대힙
            #if a[r]>a[c]:   #최소힙
            comp = a[r]<a[c]
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
                a[r],a[c]=a[c],a[r]
            c=r
    
def heap_s(a, descending=False):
    for i in range(len(a)-1,0,-1):
        print("i=", i)
        big_heap(a,i, descending )
        a[0],a[i]=a[i],a[0]
    return a


result = heap_s(arr, descending = False)
print(":::::::::: RESULT: ", result)



     