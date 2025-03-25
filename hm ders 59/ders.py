# from abc import ABC, abstractmethod

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def set_width(self, width):
#         self.width = width

#     def set_height(self, height):
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# class Square(Rectangle):
#     def set_width(self, width):
#         self.width = width
#         self.height = width

#     def set_height(self, height):
#         self.width = height
#         self.height = height

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side
    
# shapes = [Rectangle(5, 10), Square(5)]
# for shape in shapes:
#     print(shape.area())
    
# class Printer:
#     def print(self, document):
#         pass
#     def scan(self, document):
#         pass
#     def fax (self, document):
#         pass

# class Printer:
#     def print(self, document):
#         pass
# class Scanner:
#     def scan(self, document):
#         pass
# class Fax:
#     def fax(self, document):
#         pass
    
# class MultiFunctionDevice(Printer, Scanner, Fax):
#     def print(self, document):
#         print("Printing document...")

#     def scan(self, document):
#         print("Scanning document...")

#     def fax(self, document):
#         print("Faxing document...")


# mfd = MultiFunctionDevice()
# mfd.print("My document")
# mfd.scan("My document")
# mfd.fax("My document")

# from abc import ABC, abstractmethod

# class LightBulb:

#     def turn_on(self):
#         print("LightBulb: Turned on...")

#     def turn_off(self):
#         print("Lightbulb:Turned off...")

# class ElectricPowerSwitch:

#     def __init__(self, bulb: LightBulb):
#         self.bulb = bulb
#         self.on = False

#     def press(self):
#         if self.on:
#             self.bulb.turn_off()
#             self.on = False
#         else: 
#             self.bulb.turn_on()
#             self.on = True

# class Switchable(ABC):

#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass

# class LightBulb(Switchable):
#     def turn_on(self):
#         print("LightBulb: Turned on...")

#     def turn_off(self):
#         print("Lightbulb: Turned off...")

# class ElectricPowerSwitch:
#     def __init__(self, device: Switchable):
#         self.device = device
#         self.on = False
#     def press(self):
#         if self.on:
#             self.device.turn_off()
#             self.on = False
#         else:
#             self.device.turn_on()
#             self.on = True

# bulb = LightBulb()
# switch = ElectricPowerSwitch(bulb)
# switch.press()
# switch.press()