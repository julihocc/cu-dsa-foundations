def find_max(L: list[int]) -> int:
    """
    Input: A list of integers A.
    Output: The maximum integer in A.
    """
    max = None
    for number in L:
        if max is None or number > max:
            max = number
    return max