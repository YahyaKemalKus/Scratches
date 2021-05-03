import builtins
print(builtins.help(print(end="")))
print(float.as_integer_ratio(1.5))#ondalikli olarka gosterim
print(float.is_integer(3.0))#verilen ondalikli sayi tam sayi mi
print(float.hex(4.0))#floati hexadecimale cevirme
print(float.fromhex("a70"))#hexadecimali floata cevirme
x=[[]]*3
x[0].append("a")
print(x)#olusturulan ilk listeden uretilen 3 liste,ilk listeden referans aldigi icin degerleri ayni oluyor.
print("yahya".center(20,"a"))
a=3
b=3
liste=["a","b","c"]
print(a.__eq__(b))#equal/a==b/esit
print(a.__le__(b))#less than or equal/a<=b/kucuk esit
print(a.__lt__(b))#less than/a<b/kucuktur
print(a.__ge__(b))#greater than or equal/a>=b/buyuk esit
print(a.__gt__(b))#greater than/a>b/buyuktur
print(a.__ne__(b))#not equal/a!=b/esit degildir
print(liste.__contains__("a"))#in/"a" in liste)/iceriyor mu
print(format(1234567,"8.2f"))
print(f'{255:X}')#Format'in bir diger kullanim sekli
print(int(33).__format__("X"))#format bir diger kullanim sekli
print(globals())
print(locals())
