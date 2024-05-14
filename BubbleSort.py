A=[]

n = int(input("Enter Array of the Size: "))

for v in range(n):
    A.append(int(input("Enter Number: ")))

print("Unsorted Array: ",A)

def BubbleSort(A):
    n=len(A)
    for i in range(1,n):
        for j in range (1,n-i+1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
        


BubbleSort(A)
print("")
print("Array of the Size: ",n)
print("Sorted Array: ",A)
