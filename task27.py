# Pulni to‘lov birliklariga ajratish

# bu yerda moneyni input qilsak ham bo'ladi
money = 38500

ten = money // 10_000
money -= (ten * 10_000)

fife = money // 5_000
money -= (fife * 5_000)

two = money // 2_000
money -= (two * 2_000)

fife_hundred = money // 500
money -= (fife_hundred * 500)

print("O'n minglik: ", ten)
print("Besh minglik: ", fife)
print("Ikki minglik: ", two)
print("Besh yuzlik: ", fife_hundred)
print("Qoldiq: ", money) 

# Qoldiqni o'zim qo'shdim, agar boshqa son olsak, qoldiq chiqib qolsa