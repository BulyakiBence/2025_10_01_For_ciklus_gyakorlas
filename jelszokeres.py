"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.

"""
megfelelojelszo = "admin"
while True:
        jelszo = input("kérem a jelszót: ")
        if jelszo == megfelelojelszo:
            print('Sikeres belépés')
            break
        else:
            print('A jelszó hibás! ')