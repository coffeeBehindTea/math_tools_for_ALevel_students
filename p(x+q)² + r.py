a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if c:
    fir = float(b / (2 * a))
    mid = ''
    sec_mid = ''
    if fir >0:
        mid = '+'
    sec = float((b**2) / (4 * a))
    sec = float(c - sec)
    if sec > 0:
        sec_mid = '+'
    print(f"{a}(x{mid}{fir})²{sec_mid}{sec}")
else:
    fir = float(b / 2)
    fir_mid = ''
    sec_mid = ''
    if fir > 0:
        fir_mid = '+'
    sec = float(fir ** 2)
    if sec >0:
        sec_mid = '+'
    print(f"(x{fir_mid}{fir})²{sec_mid}{sec}")

q = input("")