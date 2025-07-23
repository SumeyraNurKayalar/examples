# Romen rakamları sözlüğü
roman_map = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# Arap rakamı -> Roma dönüşümü için sıralı liste
int_to_roman_map = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def roman_to_int(s):
    total = 0
    prev = 0
    for char in reversed(s.upper()):
        if char not in roman_map:
            raise ValueError("Geçersiz Roma rakamı karakteri.")
        value = roman_map[char]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total

def int_to_roman(num):
    if num < 1 or num > 3999:
        raise ValueError("Sayı 1 ile 3999 arasında olmalıdır.")
    result = ""
    for value, symbol in int_to_roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result

def main():
    print("=== Romen Rakamları Çevirici ===")
    print("1. Romen rakamını Arap rakamına çevir")
    print("2. Arap rakamını Romen rakamına çevir")
    choice = input("Seçiminiz (1/2): ")

    if choice == "1":
        roman_input = input("Romen rakamını girin (örn: XIV): ")
        try:
            result = roman_to_int(roman_input)
            print(f"Arap rakamı: {result}")
        except ValueError as e:
            print("Hata:", e)

    elif choice == "2":
        try:
            number = int(input("Arap rakamını girin (1-3999): "))
            result = int_to_roman(number)
            print(f"Romen rakamı: {result}")
        except ValueError as e:
            print("Hata:", e)
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
