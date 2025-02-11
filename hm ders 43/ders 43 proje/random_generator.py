import random
def generate_random_number(start, end):
    """belirli aralıktaki rastgele bir tam sayi üretir"""
    return random.randint(start, end)

def shuffle_list(items):
    """"bir listeyi karıştırır"""
    random.shuffle(items)
    return items