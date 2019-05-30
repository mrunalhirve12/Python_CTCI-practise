def noShifts(list):
    val = len(list)
    count = 0
    i = 0
    while list[i] < list[i + 1]:
        count += 1
        i += 1
    count += 1
    return count


print(noShifts([7, 9, 11, 12, 5]))

def noShiftsC(list):
    mins = list[0]
    for i in range(len(list)):
        if list[i] < mins:
            mins = list[i]
            min_index = i
    return min_index


print(noShiftsC([7, 9, 11, 12, 5]))
