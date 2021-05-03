from matplotlib import pyplot as plt
from math import tan,radians
x=[*range(-10,11)]
y=[*[-i for i in range(-10,1)],*[i for i in range(1,11)]]
r=(len(x)-1)/4 #cemberin yaricapi.0 da dahil oldugu icin -1 eklendi
cember_x,cember_y=[],[]
#plt.axis("off")
for i in range(91):
    x_=(r**2/(tan(radians(i))**2+1))**0.5   #cemberin x ekseninde uzerinde olan bir noktanin konumu
    y_=tan(radians(i))*x_                   #cemberin y ekseninde uzerinde olan bir noktanin konumu
    cember_x.append(x_+r)
    cember_y.append(y_+max(y)               )#cemberin merkezi dogrularin yukseklik noktasinda olmali
    cember_x.append(-x_ - r + max(x))
    cember_y.append(y_ + max(y))
    plt.plot(cember_x, cember_y)
cember_x,cember_y=[],[]


for i in range(91):
    x_=(r**2/(tan(radians(i))**2+1))**0.5
    y_=tan(radians(i))*x_
    cember_x.append(x_-r)
    cember_y.append(y_+max(y))#cemberin merkezi dogrularin yukseklik noktasinda olmali
    cember_x.append(-x_ - r)
    cember_y.append(y_ + max(y))
    plt.plot(cember_x, cember_y)

plt.plot(x,y)
plt.show()