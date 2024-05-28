n = int(input("Введите номер месяца = "))

def month_to_season(n):
    if n in [12, 1, 2]:
        print("Зима")
    if n in [3, 4, 5]:
        print("Весна")
    if n in [6, 7, 8]:
        print("Лето")
    if n in [9, 10, 11]:
        print("Осень")


month_to_season(n)