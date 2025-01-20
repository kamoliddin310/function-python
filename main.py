

def sum_of(n: int) -> int:
    if n == 1:
        return 1

    return n + sum_of(n - 1)

s = sum_of(10)
print(s)

