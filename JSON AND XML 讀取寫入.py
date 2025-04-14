# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:30:17 2025

@author: User
"""
#In[1]

#import json

#with open('data.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)

#print(data)

#import json

#data = {
#    "name": "Alice",
#    "age": 25,
#    "city": "New York"
#}

#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)


#import xml.etree.ElementTree as ET

#In[2]

#tree = ET.parse('data.xml')
#root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)

#import xml.etree.ElementTree as ET

#root = ET.Element("person")
#name = ET.SubElement(root, "name")
#name.text = "Alice"
#age = ET.SubElement(root, "age")
#age.text = "25"
#city = ET.SubElement(root, "city")
#city.text = "New York"

#tree = ET.ElementTree(root)
#tree.write("data.xml", encoding="utf-8", xml_declaration=True)

#In[3]

#import sqlite3

#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()

#cursor.execute("SELECT * FROM users")
#rows = cursor.fetchall()

#for row in rows:
#    print(row)

#conn.close()


#import sqlite3

#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

#cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")

#conn.commit()


#conn.close()
