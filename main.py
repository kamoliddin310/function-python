
def get_max(num1: int, num2: int, num3: int) -> int:
    """Bu function berilgan 3 ta sonning eng kattasini topib beradi.

    Args:
        - num1 (int): Birinchi son.
        - num2 (int): ikkinchi son.
        - num3 (int): uchinchi son.

    Returns:
        int: Eng katta son.
    """
    mx = num1
    if mx < num2:
        mx = num2
    if mx < num3:
        mx = num3
    
    return mx

m = get_max(-2, -7, -5)
print(m)
