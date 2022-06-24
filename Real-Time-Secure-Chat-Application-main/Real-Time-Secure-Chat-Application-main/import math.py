import math
ktra = 1
ok = 'y'
for i in range(1000,3000):
    for j in range(2,int(math.sqrt(i))):
        if i % j == 0:
            ktra = 0
            break
    if ktra == 1:
        ok +='"'+i+'"'
print(ok)