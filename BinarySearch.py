

dataSourceAligned = [15,20,29,30,37, 55, 69, 73, 87, 90]



def my_index( toSearchValue, dataSource ):
    sizeData = len( dataSource )
    low = 0
    high = sizeData-1

    nTrials = 0
    while( low <= high ):
        middle = int((low+high)/2)
        nTrials += 1
        #print(" Trial :" , nTrials, "middle : ", middle )
        if( dataSource[middle] == toSearchValue ):
            #print("탐색 성공 at" , middle, "index" )
            break
        elif( toSearchValue >= dataSource[middle] ):
            low = middle + 1
        else:
            high = middle - 1        

    if( low<= high):
        return middle
    else:
        return -1

toSearchValue = 30
index = my_index( toSearchValue,  dataSourceAligned)
if( index >=0 ):
    print("Found", toSearchValue, "value",  "at", index, "index" )
else:
    print("NOT found", toSearchValue, "value" )









