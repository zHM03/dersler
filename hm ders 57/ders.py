# class BankAccount:
#     def withdraw(self, amount):
#         return f"Withdraw {amount}"

# class BankCard:
#     def __init__(self, account):
#         self.account = account

#     def withdraw(self, amount):
#         if amount > 1000:
#             return "Withdraw limit exceeded"
#         return self.account.withdraw(amount)
    
# account = BankAccount()
# card = BankCard(account)
# print(card.withdraw(500))
# print(card.withdraw(1500))

# from abc import ABC, abstractmethod
# class Handler(ABC):
#     def __init__(self, successor=None):
#         self._successor = successor

#     @abstractmethod
#     def handle_request(self, request):
#         pass

# class Manager(Handler):
#     def handle_request(self, request):
#         if request == "raise":
#             return "Manager approved the raise"
        
#         elif self._successor is not None:
#             return self._successor.handle_request(request)
#         else:
#             return "Request not handled"
        
# class Director(Handler):
#     def handle_request(self, request):
#         if request == "hire":
#             return "Director approved the hire"
#         elif self._successor is not None:
#             return self._successor.handle_request(request)
        
#         else:
#             return "Request not handled"
        
# manager = Manager()
# director = Director(manager)
# print(director.handle_request("raise"))
# print(director.handle_request("hire"))

# from abc import ABC, abstractmethod

# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass

# class OrderCommand(Command):
#     def __init__(self, chef, dish):
#         self.chef = chef
#         self.dish = dish

#     def execute(self):
#         return self.chef.prepare(self.dish)
    
# class Chef:
#     def prepare(self, dish):
#         return f"Chef is preparing {dish}"
    
# chef = Chef()
# order = OrderCommand(chef, "Pasta")
# print(order.execute())

