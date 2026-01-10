def binary_search(array, number, mode):
    left = 0
    right = len(array) - 1
    mid = 0

    if mode == 'first':
        while left < right:
            mid = (left + right) // 2
            if array[mid] < number:
                left = mid + 1
            else:
                right = mid

        return left

    elif mode == 'last':
        while left < right:
            mid = (left + right) // 2
            if array[mid] <= number:
                left = mid + 1
            else:
                right = mid

        return left

    return ValueError("Неправильный режим")

