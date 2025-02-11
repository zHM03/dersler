import random

def random_choice(items):
    """listeden rastgele bir öğe seçer"""
    if not items:
        raise ValueError("Liste boş olamaz")
    return random.choice(items)