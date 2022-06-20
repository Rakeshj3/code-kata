
# While

def while_iteration(array , codesk):
    count = len(codesk)

    if count == 0:
        return -1

    start = 0
    end = count-1

    max_iterations = int(count / 2) + 1
    i = 0

    mid = end

    while array != codesk[mid] and i <= max_iterations:
        mid = start + int((end - start) / 2)
        if array > codesk[mid]:
            start = mid
        elif array < codesk[mid]:
            end = mid

        i += 1

    if codesk[mid] == array:
        return mid
    return -1



# Recursion

def recursive(array, codesk, i=0):

    count = len(codesk)

    if count == 0:
        return -1

    middle_point = int(count / 2)

    if array == codesk[middle_point]:
        return i + middle_point
    elif array > codesk[middle_point]:
        i += middle_point+1
        return recursive(array, codesk[middle_point + 1:], i)
    elif array < codesk[middle_point]:
        return recursive(array, codesk[:middle_point], i)