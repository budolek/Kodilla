def is_palindrom(text):
    """
Funkcja sprawdza wyraz od lewej do prawej 
i porównuje go os prawej do lewej 
jeżeli pary liter są takie same 
to wyraz jest palindromem i funkja zwraca wartość True
jęsli nie funkca daje wynik False
Funkcja pomija wielkość liter w wyrazie
 
    """
    if text.lower() == text.lower()[::-1]:
        return True
    return False

print(is_palindrom("PotOp"))
print(is_palindrom("Auto"))