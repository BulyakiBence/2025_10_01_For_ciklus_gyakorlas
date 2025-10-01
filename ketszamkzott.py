"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
"""
a = int(input('Adj meg egy számot:'))
b = int(input('Adj meg mégegy számot:'))
if a > b:
    for i in range(b+1, a):
        print(f"{i}")
elif a < b:
    for i in range(b-1, a,-1):
        print(i)
else: 
    print('A két szám egyenlő')
    