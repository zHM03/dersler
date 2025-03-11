# import copy 

# class Document:
    
#     def __init__(self, content):
#         self.content = content
        
#     def clone(self):
#         return copy.deepcopy(self)
    
# original = Document("Original Content")
# copy_doc = original.clone()
# copy_doc.content = "Copied Content"
# print(original.content)
# print(copy_doc.content)

# class USBC:
#     def connect(self):
#         return "Connected via USB-C"
    
# class HDMI:
#     def connect(self):
#         return "Connected via HDMI"
    
# class USBCToHDMIAdapter:
#     def __init__(self, usbc):
#         self.usbc = usbc
        
#     def connect(self):
#         return f"Adapter: {self.usbc.connect()} to HDMI"
    
# usbc = USBC()
# adapter = USBCToHDMIAdapter(usbc)
# print(adapter.connect())

from abc import ABC, abstractmethod

# class TV(ABC):
#     @abstractmethod
#     def on(self):
#         pass

#     @abstractmethod
#     def off(self):
#         pass
    
# class SonyTV(TV):
#     def on(self):
#         return "Sony TV is on"
    
#     def off(self):
#         return "Sony TV is off"
    
# class RemoteControl:
    
#     def __init__(self, tv):
#         self.tv = tv
        
#     def turn_on(self):
#         return self.tv.on
    
#     def turn_off(self):
#         return self.tv.off()
    
# tv = SonyTV()
# remote = RemoteControl(tv)
# print(remote.turn_on())

class FileSystemComponent(ABC):
    @abstractmethod
    def show(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"File: {self.name}"

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def show(self):
        result = f"Folder: {self.name}"
        for child in self.children:
            result += "\n " + child.show()
        return result
file1 = File("file1.txt")
file2 = File("file2.txt")
folder = Folder("Folder1")
folder.add(file1)
folder.add(file2)
print(folder.show())