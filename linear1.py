print("")
#-----------linear search----------------

print("Linear Search : ")

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    return -1
        
result = linear_search([1,2,35,788,26,82,5,7], 5)
if result == -1:
    print("Element not found.")
else:
    print("Element found at index" , result)

#-----------linear search----------------

print("\nLinear Search-2 : ")

def linear_search2(arr, x):
   for j in range(len(arr)):
      if arr[j] == x:
         return j
   return -1
arr = ['t','u','t','o','r','i','a']
x = 'w'

result2 = linear_search2(arr,x)
if result2 == -1:
    print("Element not found.")
else:
    print("Element found at index ", result2)









print("")