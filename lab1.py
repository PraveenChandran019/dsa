capacity = int(input("Enter the required capacity: "))
a = [None] * capacity
size = 0

def insert(pos, val):
    global size
    if pos < 0 or capacity == size or pos > size:
        print('Invalid insert')
        return
    for i in range(size, pos, -1):
        a[i] = a[i - 1]
    a[pos] = val
    size += 1

def delete(pos):
    global size
    if pos < 0 or pos >= size:
        print('Invalid position')
        return
    for i in range(pos, size - 1):
        a[i] = a[i + 1]
    size -= 1
    a[size] = None

def update(pos, val):
    if pos < 0 or pos >= size:
        print('Invalid position')
    else:
        a[pos] = val

def traversal():
    if size == 0:
        print("Array is empty")
        return
    for i in range(size):
        print(a[i], end=" ")
    print()

def linear_search(key):
    for i in range(size):
        if a[i] == key:
            print("Found the element at index:", i)
            return
    print("Not found")

def binary_search(key):
    for i in range(size - 1):
        if a[i] > a[i + 1]:
            print('Not a sorted array, cannot do binary search')
            return
    start = 0
    end = size - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            print("Key found at index:", mid)
            return
        elif a[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    print('Element not found')
