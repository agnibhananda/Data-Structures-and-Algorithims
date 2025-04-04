def bubble_sort(arr):
    for i in range(len(arr)):
        #compare each element with every other element
        for j in range(i+1, len(arr)):
            #swap if the current element is greater than the next element
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))