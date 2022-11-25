def sum_of_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_n_numbers(n-1)