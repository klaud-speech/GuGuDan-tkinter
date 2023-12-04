import numpy as np


def make_heap (a,b, descending=False):   #최대힙
    for j in range(1,b+1):
        print("\t j =", j)
        c=j 
        while c!=0:
            r=(c-1)//2
            
            #if a[r]<a[c]:   #최대힙
            #if a[r]>a[c]:   #최소힙
            comp = a[r]<a[c]
            if( (descending==False and comp==True ) or ( descending==True and comp==False  )):
                a[r],a[c]=a[c],a[r]
                print("\t\t r=", r, " c=", c, "switched")
            else:
                print("\t\t r=", r, " c=", c)
            c=r
    
def heap_sort( a, descending=True ):
    for i in range(len(a)-1,0,-1):
        print("i=", i)
        make_heap(a,i, descending )
        a[0],a[i]=a[i],a[0]
        print(">>>Partial: ", a)
    return a
#########################

random = False;
if( random == False ):
    arr=[40,70,60,30,10,50,90,80,20]
else:
    arr =[]
    for i in range(10):
        num1 = np.random.randint(100);
        arr.append(num1)

result = heap_sort( arr, descending = False )
print(":::::::::: RESULT: ", result)



     