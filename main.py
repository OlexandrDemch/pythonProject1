print("Програма для визначення вартості покупки")
a = float(input("Введіть ціну зошита ->"))
a1 = int(input("Введіть кількість Зошитів ->"))
a2 = float(a*a1)
print("Вартість зошитів дорівнює",a2,"гривень")
b = float(input("Введіть ціну альбома ->"))
b1 = int(input("Введіть кількість альбомів ->"))
b2 = float(b*b1)
print("Вартість альбомів дорівнює",b2,"гривень")
c = float(input("Введіть ціну ручки ->"))
c1 = int(input("Введіть кількість ручок ->"))
c2 = float(c*c1)
print("Вартість ручок дорівнює",c2,"гривень")
d = float(input("Введіть ціну олівця ->"))
d1 = int(input("Введіть кількість олівців ->"))
d2 = float(d*d1)
print("Вартість олівців дорівнює",d2,"гривень")
s = float(a2+b2+c2+d2)
print("Загальна вартість покупки дорівнює",s,"гривень")
