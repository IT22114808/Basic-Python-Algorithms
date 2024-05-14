A=[]

#Get Array Length from the user
n=int(input("Enter the Length of the Array: "))

#Get numbers between 0 and 100 
for i in range(n):
    number = int(input('Enter Number :'))
    if(number>0 and number<100):
        A.append(number)
    else:
        print("Invalid Number")
    i=i+1

print('unsorted Data "',A)


def Insertion(A):

    for j in range (1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and key<A[i]:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

Insertion(A)
print('')
print('Length of the Array :',n)
print('Unsorted Data :',A)
        
        

