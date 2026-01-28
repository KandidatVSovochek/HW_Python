def is_year_leap(year):
    return True if year % 4 == 0 else False


numyear = int(input("Введите год"))
result = is_year_leap(numyear)
print(f"год {numyear}:{result}")
