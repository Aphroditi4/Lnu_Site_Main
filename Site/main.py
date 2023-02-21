def task_1(A, B):
    m, n = len(A), len(B)
    C = [0] * (m + n)
    i, j, k = 0, 0, 0

    while i < m and j < n:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < m:
        C[k] = A[i]
        i += 1
        k += 1

    while j < n:
        C[k] = B[j]
        j += 1
        k += 1

    return C


def task_2(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    a = len(arr1)
    b = len(arr2)
    c = len(arr3)
    while i < a and j < b and k < c:
        if arr1[i] == arr2[j] == arr3[k]:
            return arr1[i]

        smallest = arr1[i]
        if arr2[j] < smallest:
            smallest = arr2[j]
        if arr3[k] < smallest:
            smallest = arr3[k]

        if smallest == arr1[i]:
            i += 1
        elif smallest == arr2[j]:
            j += 1
        else:
            k += 1

    # If no common element found, return an error or None
    return None

def task_3():
    pass
def main():
    a = [1, 2, 2, 3, 5, 6]
    b = [1, 3, 3, 5, 8]
    result = task_1(b, a)
    print(result)
    arr1 = [1, 4, 7, 10, 13]
    arr2 = [1, 3, 4, 6, 7, 9, 10, 12]
    arr3 = [1, 2, 4, 5, 7, 8, 10, 11]

    result_2 = task_2(arr1, arr2, arr3)
    print(result_2)


if __name__ == '__main__':
    main()
