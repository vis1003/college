def insertion_sort(a, n):
    for i in range(1, n):
        picked = a[i]
        j = i
        while picked < a[j - 1] and j > 0:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = picked
    return a


def merge_sort(a):
    n = len(a)
    if n > 1:
        mid = n // 2
        lefthalf = a[:mid]
        righthalf = a[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i = i + 1
            else:
                a[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            a[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return a


a = []
n = int(input("Enter length of list:"))
print("Enter the elements:")
for i in range(0, n):
    j = int(input())
    a.append(j)

ch = int(input("1. Insertion sort \n2. Merge sort \nEnter your choice:"))
if ch == 1:
    sorted = insertion_sort(a, n)
    print("The sorted list is:", sorted)
else:
    sorted = merge_sort(a)
    print("The sorted list is:", sorted)
