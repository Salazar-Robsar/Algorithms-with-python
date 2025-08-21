def merge_sort(arry):
    if len(arry) <= 1:
        return arry
    
    mid = len(arry) // 2
    left = arry[:mid]
    right = arry[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    print(right, left)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    numbers = [7,1,2,6,8,2,9,22,13,23,11,2]
    print(merge_sort(numbers))