from collections import namedtuple

# Создает класс именованного кортежа
Task = namedtuple('Task', 'title desc urgency')
# Также атрибуты модели данных могут задаваться в виде объекта list
# Task = namedtuple('Task', ['title', 'desc', 'urgency'])

# Создает экземпляр именованного кортежа
task_nt = Task('Laundry', 'Wash clothes', 3)

print(task_nt.title)
print(task_nt.desc)
print(task_nt.urgency)
