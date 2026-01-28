def month_to_season(n):
    if n <=2 and n == 12:
        print ("Зима")
    elif 3 <= n <= 5:
        print ("Весна")
    elif 6 <= n <= 8:
        print ("Лето")
    else: 9 <= n <= 11
    print("Осень")
n = int(input("Введите порядковый номер месяца: "))
month_to_season(n)