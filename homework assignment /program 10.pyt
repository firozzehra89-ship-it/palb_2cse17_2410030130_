def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    max_reach = arr[0]
    steps_left = arr[0]
    jumps = 1

    for i in range(1, n - 1):
        max_reach = max(max_reach, i + arr[i])
        steps_left -= 1

        if steps_left == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps_left = max_reach - i

    return jumps

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))
