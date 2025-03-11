# import yaml
# import os

# data = {"isim": "Hişam", "yas": 21, "sehir": "Şam"}
# yaml_string = yaml.dump(data)
# print(yaml_string)

# script_dir = os.path.dirname(__file__)
# abs_file_path = os.path.join(script_dir, "veri.yaml")
# with open(abs_file_path, "w", encoding="utf-8") as yaml_file:
#     yaml.dump(data, yaml_file)
    
# with open(abs_file_path, "r", encoding="utf-8") as yaml_file:
#     data_loaded = yaml.load(yaml_file, Loader=yaml.FullLoader)
# print(data_loaded)

# import xml.etree.ElementTree as ET

# data = {"isim": "Tayfun", "yas": 30, "sehir": "giresun"}

# root = ET.Element("kisi")
# for key, value in data.items():
#     child = ET.SubElement(root, key)
#     child.text = str(value)
# tree = ET.ElementTree(root)
# tree.write("veri.xml")
# tree = ET.parse("veri.xml")
# root= tree.getroot()
# data_loaded = {child.tag: child.text for child in root}
# print(data_loaded)

# import requests
# import json

# # URL to access GitHub API for user data
# url = 'https://api.github.com/users/zHM03'

# response = requests.get(url)

# # Check if the response is successful (HTTP 200)
# if response.status_code == 200:
#     data = response.json()

#     # Save data to a JSON file
#     with open('octocat.json', 'w') as f:
#         json.dump(data, f, indent=4)

#     print("Data saved successfully!")
# else:
#     print(f"Failed to fetch data. HTTP Status code: {response.status_code}")

import json
import pickle
import xml.etree.ElementTree as ET
import yaml
import csv

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = []

    def add_users(self, name, age, email):
        self.users.append({'name': name, 'age': age, 'email': email})

    def save_to_json(self):
        with open(f'{self.filename}.json', 'w') as f:
            json.dump(self.users, f)

    def save_to_pickle(self):
        with open(f'{self.filename}.pkl', 'wb') as f:
            pickle.dump(self.users, f)

    def save_to_xml(self):
        root = ET.Element('users')
        for user in self.users:
            user_elem = ET.SubElement(root, 'user')
            name_elem = ET.SubElement(user_elem, 'name')
            name_elem.text = user['name']
            age_elem = ET.SubElement(user_elem, 'age')
            age_elem.text = str(user['age'])
            email_elem = ET.SubElement(user_elem, 'email')
            email_elem.text = user['email']
        
        tree = ET.ElementTree(root)
        tree.write(f'{self.filename}.xml', encoding='utf-8', xml_declaration=True)

    def save_to_yaml(self):
        with open(f'{self.filename}.yaml', 'w') as f:
            yaml.dump(self.users, f)

    def save_to_csv(self):
        with open(f'{self.filename}.csv', mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'age', 'email'])
            writer.writeheader()
            writer.writerows(self.users)

    def load_from_json(self):
        with open(f'{self.filename}.json', 'r') as f:
            self.users = json.load(f)

    def load_from_pickle(self):
        with open(f'{self.filename}.pkl', 'rb') as f:
            self.users = pickle.load(f)

    def load_from_xml(self):
        tree = ET.parse(f'{self.filename}.xml')
        root = tree.getroot()
        self.users = []
        for user_elem in root.findall('user'):
            name = user_elem.find('name').text
            age = int(user_elem.find('age').text)
            email = user_elem.find('email').text
            self.users.append({'name': name, 'age': age, 'email': email})

    def load_from_yaml(self):
        with open(f'{self.filename}.yaml', 'r') as f:
            self.users = yaml.load(f, Loader=yaml.FullLoader)

    def load_from_csv(self):
        self.users = []
        with open(f'{self.filename}.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.users.append({'name': row['name'], 'age': int(row['age']), 'email': row['email']})

    def display_users(self):
        for user in self.users:
            print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
manager = UserManager('users')
manager.add_users('Alice', 25, 'alice@example.com')
manager.add_users('Bob', 30, 'bob@example.com')
manager.save_to_json()
manager.save_to_pickle()
manager.save_to_xml()
manager.save_to_yaml()
manager.save_to_csv()
print("Loaded from CSV:")
manager.load_from_csv()
manager.display_users()



