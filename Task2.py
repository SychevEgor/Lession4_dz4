user_number = int(input('Введите число: '))
index = 2
result = []
while user_number > 1:
    if user_number % index == 0:
        result.append(index)
        user_number = user_number / index
    else: index += 1


print(result)