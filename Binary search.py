# Binary search in python modified from program by THARUN1526

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

def search():
    while True:
        try:
            x = int(input("Input an integer: "))
            return x
        except ValueError:
            print("That's not a valid option! Try an integer.")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = search()

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
    print("Array: " + str(array))
else:
    print("Not found")
