A=[]

for v in range(4):
    A.append(int(input("Enter NUmber :")))

print(A)

key = int(input("Enter Number: "))

def BINARY_SEARCH(A,min,max,key):  
    if max<min:
        return -1
    else:
        mid = (min+max)//2
        if A[mid]>key:
            return BINARY_SEARCH(A,min,mid-1,key)
        elif A[mid]<key:
            return BINARY_SEARCH(A,mid+1,max,key)
        else:
            return mid

result=BINARY_SEARCH(A,0,len(A)-1,key)

if result != -1:
    print("Element is present in index",result)
else:
    print("Element is not present in index")
