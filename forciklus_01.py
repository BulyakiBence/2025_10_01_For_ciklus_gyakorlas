"""
1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.

"""
x = int(input('Adj meg egy egész számmot: '))
y = 0

for i in range(x):
    y += i
print(f'Az előtte lévő számok összege: {y}')