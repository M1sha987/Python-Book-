good_stocks = ["AAPL", "GOOG", "AMZN", "NVDA"]
client0 = ["GOOG", "AMZN"]
client1 = ["AMZN", "SNAP"]

"""
Проверка вхождения всех элементов в другой список
"""
def all_contained_in_recommended(recommended, personal):
    print(f"Is {personal} contained in {recommended}?")
    for stock in personal:
        if stock not in recommended: 
            return False
    return True

print(all_contained_in_recommended(good_stocks, client0))

# Проверка вхождения всех элементов в другой список методом issuperset
good_stocks_set = set(good_stocks) 
contained0 = good_stocks_set.issuperset(client0) 
print(f"Is {client0} contained in {good_stocks}? {contained0}")


"""
Содержит ли список любой из элементов другого списка
"""
good_stocks_set & set(client0)
# Вывод: {'AMZN', 'GOOG'}
bool(good_stocks_set & set(client0))
# Вывод: True
good_stocks_set & set(client1)
# Вывод: {'AMZN'}
bool(good_stocks_set & set(client1))
# Вывод: True

"""
Работа с несколькими объектами set
"""
tasks_a = {"Homework", "Laundry", "Grocery"}
tasks_b = {"Laundry", "Gaming"}

# Операция объединения (|)
tasks_a | tasks_b 
# Вывод: {'Laundry', 'Gaming', 'Homework', 'Grocery'}

# Операция пересечения (&)
tasks_a & tasks_b 
# Вывод: {'Laundry'}

# Операция симметрической разности (^)
tasks_a ^ tasks_b 
# Вывод: {'Homework', 'Grocery', 'Gaming'}

# Операция разности (-)
tasks_a - tasks_b 
# Вывод: {'Homework', 'Grocery'}

