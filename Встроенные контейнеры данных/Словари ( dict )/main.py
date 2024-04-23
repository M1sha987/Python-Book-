"""
В словаре каждый элемент имеет уникальный ключ 
и ассоциированое с ним некоторое значение.
"""

dict = {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}

# Получение данных
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgen_keys = urgencies.keys()
urgen_values = urgencies.values()
urgen_items = urgencies.items()
print(urgen_keys, urgen_values, urgen_items, sep="\n")
