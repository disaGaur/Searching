def linear_search(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
        else:
            return -1


arr = ['D', 'I', 'S', 'A']
elt = input("Enter the element you want to search:-\n")
print("Element found at index " + str(linear_search(arr, elt)))
