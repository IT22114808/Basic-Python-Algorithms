A=[] #create Array

n=(int(input("Enter the Size of the Array: ")))

# Input numbers into the list
for v in range (n):
    A.append(int(input("Enter Number :")))

print("")
print("Size of the Array: ", n)
print("unsorted Numbers: ",A)

def partition(A,p,r):

    x = A[r]
    i = p - 1
    
    # Iterate over the range correctly (change r-1 to r)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

# Call QuickSort with correct indices (0 and len(A)-1)
QuickSort(A, 0, len(A) - 1)
print("Sorted Array: ", A)



    
        
        
