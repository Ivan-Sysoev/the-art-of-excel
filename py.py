def decor(func):
    def _repeater(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
            print(f"Номер итерации: {i + 1}")
    return _repeater

@decor
def square_sum(a, b, c, d, *args):
    return sum([elem ** 2 for elem in [a, b, c, d, *args]])

square_sum(1,2,3,4,5,6,7,8)