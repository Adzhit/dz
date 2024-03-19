number = int(input("Введіть 5-ти значне число: "))

ten_thousands, remainder = divmod(number, 10000)
thousands, remainder = divmod(remainder, 1000)
hundreds, remainder = divmod(remainder, 100)
tens, units = divmod(remainder, 10)

number_backwards= int(units * 10000 + tens * 1000 + hundreds * 100 + thousands * 10 + ten_thousands * 1)

print(number_backwards)