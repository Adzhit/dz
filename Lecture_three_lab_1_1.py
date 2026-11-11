import math

def divide(numerator, denominator):
    if denominator == 0:
        if numerator == 0:
            raise ZeroDivisionError("Ділення на нуль не підтримується (чисельник і знаменник нульові)")
        raise ZeroDivisionError("Ділення на нуль не підтримується")
    return numerator / denominator

def calculate_variant_1(x, y, z, b):
    numerator_a = 2 * math.cos(x - math.pi / 6) * b
    denominator_a = 0.5 + math.sin(y)**2
    a = divide(numerator_a, denominator_a)

    # Используем abs(y) для избежания комплексных чисел при дробной степени отрицательного y
    denominator_m_raw = 3 + abs(y)**(2/5)
    m = 1 + divide(z**2, denominator_m_raw)

    return a, m
