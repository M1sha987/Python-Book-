# Сортировка чисел
numbers = [12, 4, 1, 3, 7, 5, 9, 8]
numbers.sort()
print(numbers)

# Сортировка в обратном порядке
number = [12, 4, 1, 3, 7, 5, 9, 8]
number.sort(reverse=True)
print(number)

# Сортировка строк
names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort()
print(names)

# Сортировка строк и чисел
mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]
mixed.sort(key=str)
print(mixed)


#  Сортировка задач с назначением аргумента key
tasks = [
 {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
 {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
 {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

def using_urgency_level(task):
    return task['urgency']

tasks.sort(key=using_urgency_level, reverse=True)
print(tasks)