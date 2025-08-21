def selection_sort(array):
    n = len(array)
    for i in range(0, n-1, 1):
        min_element = i
        for j in range(i+1, n):
            if array[j] < array[min_element]:
                min_element = j
        if min_element != i:
            array[i], array[min_element] = array[min_element],  array[i]
    return array



if __name__ == "__main__":
    item_list = [1,5,7,3,4,8,0]
    print(selection_sort(item_list))


