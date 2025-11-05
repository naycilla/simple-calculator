a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("5. Modulus")

opsi = input("Masukkan pilihan (1/2/3/4/5): ")

if opsi == "1":
    print("Hasil:", a + b)
elif opsi == "2":
    print("Hasil:", a - b)
elif opsi == "3":
    print("Hasil:", a * b)
elif opsi == "4":
    print("Hasil:", a / b)
elif opsi == "5":
    print("Hasil:", a % b)
else:
    print("Pilihan tidak valid.")
