from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "23 Ultra", "+71111111111")
phone2 = Smartphone("Apple iPhone", "12 Pro", "+72222222222")
phone3 = Smartphone("Xiaomi", "M 5", "+73333333333")
phone4 = Smartphone("Honor", "90 lite", "+74444444444")
phone5 = Smartphone("HUAWEI", "Nova 12", "+75555555555")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
      print(f"{phone.brand} - {phone.model}. {phone.number}")
