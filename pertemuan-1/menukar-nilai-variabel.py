# Menukar Nilai Variabel

"""

[ Algoritma ]

1. Membuat tiga variabel (x, y, z) yang berfungsi sebagai piring.
2. Masukkan “Manggis” ke dalam variabel x, “Pisang” ke dalam variabel y, dan string kosong ke dalam variable z.
3. Membuat fungsi menukar_posisi yang memiliki tiga parameter yaitu x, y, dan z.
4. Di dalam fungsi, masukkan nilai variabel x ke variabel z dan kosongkan nilai variabel x.
5. Di dalam fungsi, masukkan nilai variabel y ke variabel x dan kosongkan nilai variable y.
6. Di dalam fungsi, masukkan nilai variabel z ke variabel y dan kosongkan nilai variabel z.
7. Di dalam fungsi, tampilkan nilai variabel x, y, dan z ke layar. 
8. Panggil fungsi menukar_posisi dan masukkan x, y, dan z sebagai parameternya.

[ Pseudocode ]

x ← "Manggis"
y ← "Pisang"
z ← ""

Print("[ Sebelum Ditukar ]")
Print("Piring 1:", x)
Print("Piring 2:", y)
Print("Piring 3:", z)

Function menukar_posisi(x, y, z)
    z ← x
    x ← ""

    Print()
    Print("[ Proses ]")
    Print("Piring 1:", x)
    Print("Piring 2:", y)
    Print("Piring 3:", z)

    x ← y
    y ← z
    z ← ""
    Print()
    Print("[ Setelah Ditukar ]")
    Print("Piring 1:", x)
    Print("Piring 2:", y)
    Print("Piring 3:", z)
EndFunction

menukar_posisi(x, y, z)

"""

x = "Manggis"
y = "Pisang"
z = ""

print("[ Sebelum Ditukar ]")
print(f"Piring 1: {x}")
print(f"Piring 2: {y}")
print(f"Piring 3: {z}")


def menukar_posisi(x, y, z):
    z = x
    x = ""

    print()
    print("[ Proses ]")
    print(f"Piring 1: {x}")
    print(f"Piring 2: {y}")
    print(f"Piring 3: {z}")

    x = y
    y = z
    z = ""
    print()
    print("[ Setelah Ditukar ]")
    print(f"Piring 1: {x}")
    print(f"Piring 2: {y}")
    print(f"Piring 3: {z}")


menukar_posisi(x, y, z)
