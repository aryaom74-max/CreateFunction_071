import math


def konversi_suhu(nilai, satuan):
    satuan = satuan.upper()
    if satuan == "C":
        hasil = (nilai * 9/5) + 32
        return f"{nilai}°C = {hasil}°F"
    elif satuan == "F":
        hasil = (nilai - 32) * 5/9
        return f"{nilai}°F = {hasil:.2f}°C"
    else:
        return "Satuan tidak valid. Gunakan 'C' atau 'F'."


luas_lingkaran = lambda r: math.pi * (r**2)



print("=== UJI COBA POIN 1 (KONVERSI SUHU) ===")

print(konversi_suhu(37, "C"))   # Output: 37°C = 98.6°F
print(konversi_suhu(100, "F"))  # Output: 100°F = 37.78°C
print(konversi_suhu(0, "C"))    # Output: 0°C = 32°F
print(konversi_suhu(98.6, "F")) # Output: 98.6°F = 37.00°C

print("\n=== UJI COBA POIN 2 (LUAS LINGKARAN) ===")
jari_jari = 10
print(f"Luas lingkaran (r={jari_jari}): {luas_lingkaran(jari_jari):.2f}")