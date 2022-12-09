lst = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {lst}")
result = []
[result.append(i) for i in lst if i not in result]
print(f"Список из неповторяющихся элементов: {result}")