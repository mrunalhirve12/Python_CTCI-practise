def get_number_of_pairs(int_array, server_weight):
    m = [0] * 1000
    n = len(int_array)
    for i in range(0, n):
        m[int_array[i]]
        m[int_array[i]] += 1
    twice_count = 0
    for i in range(0, n):
        twice_count += m[server_weight - int_array[i]]
        if (server_weight - int_array[i] == int_array[i]):
            twice_count -= 1
    return int(twice_count / 2)

print(get_number_of_pairs([6,1,3,5, 7, 1,9], 8))