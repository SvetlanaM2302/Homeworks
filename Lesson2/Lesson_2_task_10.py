x = int(input("Введите сумму вклада = "))
y = int(input("Введите срок вклада = "))

def bank(x, y):
   balance = x * (1.1 ** y)
   balance = round(balance,2)
   return balance

print(bank(x, y))

