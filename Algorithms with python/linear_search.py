def basic_search(arr, value):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == value:
            return i
        else:
            i += 1
    return 'Value not found'    

def sentinel_search(arr, value):
    n = len(arr)
    arr.append(value)
    i = 0
    while arr[i] != value:
        i += 1
    arr.pop()
    if i < n:
        return i
    return 'Value no found'

if __name__ == "__main__":
    number_list = [1,25,6,31,6,2,3,4,51,23,25]
    number_to_find = 2
    #print(basic_search(number_list, number_to_find))
    print(sentinel_search(number_list, number_to_find))