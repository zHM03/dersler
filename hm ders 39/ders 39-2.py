from forex_python.converter import CurrencyRates

cr = CurrencyRates()
try: 
    amount_in_try= float(input("lütfen TL miktarını girin: "))
    amount_in_usd = cr.convert('TRY', 'USD', amount_in_try)
    print(f'{amount_in_try} TRY = {amount_in_usd} USD')
    
    amount_in_usd = float(input("lütfen tl miktarını girin: "))
    amount_in_try = cr.convert('USD', 'TRY', amount_in_usd)
    print(f'{amount_in_usd} USD = {amount_in_try} TRY')
    
except Exception as e:
    print(f"Hata: {e}")