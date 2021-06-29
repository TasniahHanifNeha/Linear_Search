print("")


#---------------linear search---------------

#list1 = [int(item) for item in input("Enter the list items : ").split()]


def linear_search(list1, search_number):
    for i in range(len(list1)):
        if list1[i] == search_number:
            return i
    return -1

list1 = [int(item) for item in input("Enter the list items : "). split()]
search_number = int(input("Enter searching number : "))
result = linear_search(list1, search_number)

if result == -1:
    print("Element not found.")
else:
    print("Element found at index" , result)

print("")



#---------------linear search-2----------------

def linear_search2(list2, search_item):
    for j in range(len(list2)):
        if list2[j] == search_item:
            return j
    return -1

list2 = [str(item2) for item2 in input("Enter the list items : "). split()]
search_item = str(input("Enter searching char : "))
result2 = linear_search2(list2, search_item)

if result2 == -1:
    print("Element not found.")
else:
    print("Element found at index" , result2)




print("")