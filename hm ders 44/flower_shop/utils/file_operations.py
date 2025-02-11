import json

def save_to_file(data, filename):
    """ Verileri bir dosyaya kaydeder"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)
        
def load_from_file(filename):
    """Verileri bir dosyadan yükler"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []