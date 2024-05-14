A=[]

n= int(input("Enter size of the array:"))
       

for v in range (n):
    A.append(int(input("Enter Number :")))

print("Unsorted Array:",A)

def Selection(A):

    n=len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range (j+1,n):
            if A[i]<A[smallest]:
                smallest = i
         
            A[j], A[smallest] = A[smallest], A[j]



Selection(A)

print("")
print("Size of the Array:",n)
print("Sorted Array :",A)
