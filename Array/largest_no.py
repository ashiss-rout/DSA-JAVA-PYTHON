#largest no. in array 

n=int(input("enter no of input"))
arr = input("enter array") 
L=arr[0]
for i in range(0,n-1):
    if(arr[i]>L):
        L=arr[i]
print(L)
     
