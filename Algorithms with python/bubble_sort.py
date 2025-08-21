"""def bubble_sort1(array):
    array_list = len(array)

    swapped = False
    for i in range(array_list - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swapped = True            
    return array
"""

def bubble_sort2(array):
    n = len(array)
    while n > 1:
        newn = 0
        for i in range(1, n):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                newn = i
        n = newn
    return array


if __name__ == "__main__":
    item_list = [21,41,1,32,1,2,7,4,3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(bubble_sort2(item_list))
