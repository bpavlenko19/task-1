def roman_to_integer(s: str) -> int:
    # Мапа римських цифр
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(s):  # Перебір з права наліво
        current_value = roman_map[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value  # Оновлення попереднього значення

    return total

# Приклади використання
print(roman_to_integer("III"))       # Вивід: 3
print(roman_to_integer("LVIII"))     # Вивід: 58
print(roman_to_integer("MCMXCIV"))   # Вивід: 1994
