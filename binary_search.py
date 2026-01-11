def binary_search(array, number, mode):
    left = 0
    right = len(array) - 1
    mid = 0

    if mode == 'first': # поиск индекса первого элемента, меньшего или равного number
        while left < right:
            mid = (left + right) // 2
            if array[mid] < number:
                left = mid + 1
            else:
                right = mid

        return left

    elif mode == 'last': # поиск индекса первого элемента, большего number
        while left < right:
            mid = (left + right) // 2
            if array[mid] <= number:
                left = mid + 1
            else:
                right = mid

        return left

    raise ValueError("Неправильный режим")

