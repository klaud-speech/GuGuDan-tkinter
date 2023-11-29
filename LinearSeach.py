

dataSource = [12,10,25,5,7,96]

indexValue = 0
toSearchValue = 10

sizeData = len( dataSource )
#print("sizeData =", sizeData )

while( indexValue < sizeData ):
    if( dataSource[indexValue] == toSearchValue ):
        print("탐색 성공 at" , indexValue, "index" )
        break
    indexValue += 1

if(indexValue == sizeData ):
    print( toSearchValue, "를 찾지 못함")
print("Done", flush=True)






