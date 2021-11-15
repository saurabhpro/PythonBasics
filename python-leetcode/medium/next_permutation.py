def next_perm(n: list) -> list:
    i = len(n) - 2
    while i >= 0 and n[i + 1] <= n[i]:
        i -= 1

    if i >= 0:
        j = len(n) - 1
        while n[j] <= n[i]:
            j -= 1

        swap(n, i, j)

    return reverse(n, i + 1)


def swap(n, i, j) -> None:
    n[i], n[j] = n[j], n[i]


def reverse(n, from_index) -> list:
    res = []
    for i in range(0, from_index):
        res.append(n[i])

    for i in range(len(n) - 1, from_index - 1, -1):
        res.append(n[i])

    return res

# print(next_perm([1, 2, 3]))
# print(next_perm([1, 3, 2]))
# print(next_perm([1, 3, 7, 2]))
