import math as m
print("type -999 to quit")
while 1:
    print("===============INPUT===============")
    x1 = float(input("x1= "))
    if x1 == -999.0:
        quit()
    y1 = float(input("y1= "))
    x2 = float(input("x2= "))
    y2 = float(input("y2= "))

    dis = pow((x2 - x1),2) + pow((y2 - y1),2)
    dis = round(m.sqrt(dis),3)
    mid = (round((x2 - x1)/2,3),round((y2 - y1)/2,3))
    print("================ANS================")
    print(f"distant = {dis}\nmid point = {mid}")
