def permutations(arr, start=0):

    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]

        permutations(arr, start + 1)

        arr[start], arr[i] = arr[i], arr[start]

numbers = [1, 2, 3]

permutations(numbers)