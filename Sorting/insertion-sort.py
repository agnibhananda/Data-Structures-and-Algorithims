

def insertion_sort(arr):
    #iterate from second element
    for i in range(1,len(arr)):
        key = arr[i] # store the current element
        #compare with previous element
        j = i-1
        while j >= 0 and key<arr[j]:
            #if current element smaller move the previous element to the right
            arr[j+1] = arr[j]
            j -= 1
        #insert current element in correct position
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(insertion_sort(arr))