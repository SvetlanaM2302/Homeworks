from address import Address
from mailing import Mailing

to_address = Address(354000, "г. Сочи", "ул. Мира", 163, 56)
from_address = Address(350000, "г. Краснодар", "ул. Любимого", 16, 96)
mailing = Mailing(to_address, from_address, 1350, "ABC232567")

print("Отправление",
    mailing.tr,
    "из",
    from_address.i, from_address.c, from_address.s, from_address.h, "-", from_address.an,
    "в",
    to_address.i, to_address.c, to_address.s, to_address.h, "-", to_address.an,
    ". Стоимость", mailing.c, "рублей.",)