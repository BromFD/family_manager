def gen_gaps(length): # Генерация последовательности Пратта
    gaps = [1]
    index_of_2 = 0
    index_of_3 = 0
    is_next_el_overflow = False
    while not is_next_el_overflow:
        next_2 = gaps[index_of_2] * 2
        next_3 = gaps[index_of_3] * 3
        next_el = min(next_2, next_3)

        if next_el == next_2:
            index_of_2 += 1
        if next_el == next_3:
            index_of_3 += 1

        if next_el >= length:
            is_next_el_overflow = True

        if not is_next_el_overflow:
            gaps.append(next_el)

    return gaps[::-1]


def shell_sort(array, values, secondary_values=None): # Модифицированная сортировка Шелла, сортирует сначала по основным значениям, но если они равны, то сортирует по вторичным
    length = len(values)
    gaps = gen_gaps(length)
    if secondary_values is None:
        secondary_values = [0] * length
    for gap in gaps:
        for el in range(gap, length):
            hole = el
            value = values[el]
            secondary_value = secondary_values[el]
            item = array[el]
            while hole >= gap and (values[hole - gap] > value or (values[hole - gap] == value and secondary_values[hole - gap] > secondary_value)):
                values[hole] = values[hole - gap]
                secondary_values[hole] = secondary_values[hole - gap]
                array[hole] = array[hole - gap]
                hole -= gap

            values[hole] = value
            secondary_values[hole] = secondary_value
            array[hole] = item

    return array

