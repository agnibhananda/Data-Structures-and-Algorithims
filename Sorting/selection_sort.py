#Selection sort repeatedly selects the minimum element from the unsorted part of the list and places it at the beginning of the sorted part
def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))
