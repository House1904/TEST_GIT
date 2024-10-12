import random

def generate_random_sequence(n, min_value, max_value):
    """Tạo dãy số ngẫu nhiên có n phần tử trong khoảng [min_value, max_value]"""
    return [random.randint(min_value, max_value) for tmp in range(n)]