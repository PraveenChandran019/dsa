capacity = int(input("Enter the required capacity: "))
a = [None] * capacity
size = 0


def insert(pos, val):
    global size
    if pos < 0 or capacity == size or pos > size:
        print("Invalid insert")
        return
    for i in range(size, pos, -1):
        a[i] = a[i - 1]
    a[pos] = val
    size += 1


def delete(pos):
    global size
    if pos < 0 or pos >= size:
        print("Invalid position")
        return
    for i in range(pos, size - 1):
        a[i] = a[i + 1]
    size -= 1
    a[size] = None


def update(pos, val):
    if pos < 0 or pos >= size:
        print("Invalid position")
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
            print("Not a sorted array, cannot do binary search")
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
    print("Element not found")


while True:
    print("\nChoose option from 1-6 (or 7 to exit)")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Traverse")
    print("5. Linear search")
    print("6. Binary search")
    print("7. Exit")

    ch = int(input("Enter an option from above: "))

    if ch == 1:
        pos = int(input("Enter the position you want to insert: "))
        val = int(input("Enter the value you want to insert: "))
        insert(pos, val)
    elif ch == 2:
        pos = int(input("Enter the position you want to delete: "))
        delete(pos)
    elif ch == 3:
        pos = int(input("Enter the position you want to update: "))
        val = int(input("Enter the value you want to update: "))
        update(pos, val)
    elif ch == 4:
        traversal()
    elif ch == 5:
        key = int(input("Enter the element you want to find: "))
        linear_search(key)
    elif ch == 6:
        key = int(input("Enter the element you want to find: "))
        binary_search(key)
    elif ch == 7:
        break
    else:
        print("Invalid option")



class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.a = [None] * capacity
        self.size = 0

    def insert(self, pos, val):
        if pos < 0 or self.capacity == self.size or pos > self.size:
            print("Invalid insert")
            return
        for i in range(self.size, pos, -1):
            self.a[i] = self.a[i - 1]
        self.a[pos] = val
        self.size += 1

    def delete(self, pos):
        if pos < 0 or pos >= self.size:
            print("Invalid position")
            return
        for i in range(pos, self.size - 1):
            self.a[i] = self.a[i + 1]
        self.size -= 1
        self.a[self.size] = None

    def update(self, pos, val):
        if pos < 0 or pos >= self.size:
            print("Invalid position")
        else:
            self.a[pos] = val

    def traversal(self):
        if self.size == 0:
            print("Array is empty")
            return
        for i in range(self.size):
            print(self.a[i], end=" ")
        print()

    def linear_search(self, key):
        for i in range(self.size):
            if self.a[i] == key:
                print("Found the element at index:", i)
                return
        print("Not found")

    def binary_search(self, key):
        for i in range(self.size - 1):
            if self.a[i] > self.a[i + 1]:
                print("Not a sorted array, cannot do binary search")
                return
        start = 0
        end = self.size - 1
        while start <= end:
            mid = (start + end) // 2
            if self.a[mid] == key:
                print("Key found at index:", mid)
                return
            elif self.a[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        print("Element not found")


if __name__ == "__main__":
    cap = int(input("Enter the required capacity: "))
    arr = Array(cap)

    while True:
        print("\nChoose option from 1-6 (or 7 to exit)")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Traverse")
        print("5. Linear search")
        print("6. Binary search")
        print("7. Exit")

        ch = int(input("Enter an option from above: "))

        if ch == 1:
            pos = int(input("Enter the position you want to insert: "))
            val = int(input("Enter the value you want to insert: "))
            arr.insert(pos, val)
        elif ch == 2:
            pos = int(input("Enter the position you want to delete: "))
            arr.delete(pos)
        elif ch == 3:
            pos = int(input("Enter the position you want to update: "))
            val = int(input("Enter the value you want to update: "))
            arr.update(pos, val)
        elif ch == 4:
            arr.traversal()
        elif ch == 5:
            key = int(input("Enter the element you want to find: "))
            arr.linear_search(key)
        elif ch == 6:
            key = int(input("Enter the element you want to find: "))
            arr.binary_search(key)
        elif ch == 7:
            break
        else:
            print("Invalid option")
