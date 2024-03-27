digit1= float(input("Введите число_1: "))
mathematical_action = input("Выберите математическую операцыю (+,-,*,/): ")
digit2  = float(input("Введите число_2: "))

if mathematical_action == "+":
    result = (digit1 + digit2)
elif mathematical_action == "-":
    result = (digit1 - digit2)
elif mathematical_action == "*":
    result = (digit1 * digit2)
elif mathematical_action == "/":
    if digit2 != 0:
        result = (digit1 / digit2)
    else:
        print("Ошибка! Деление на 0 - невозможно!")

print(result)










