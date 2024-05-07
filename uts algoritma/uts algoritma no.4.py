def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def beri_rekomendasi(bmi):
    if bmi < 18.5:
        return "Kurus. Anda mungkin perlu menambah berat badan."
    elif 18.5 <= bmi < 25:
        return "Normal. Berat badan Anda ideal."
    elif 25 <= bmi < 30:
        return "Gemuk. Anda mungkin perlu mengurangi berat badan."
    else:
        return "Obesitas. Anda perlu konsultasi dengan dokter untuk menurunkan berat badan."

# Meminta pengguna untuk memasukkan berat badan (dalam kilogram)
berat_badan = float(input("Masukkan berat badan Anda (kg): "))

# Meminta pengguna untuk memasukkan tinggi badan (dalam meter)
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

# Menghitung BMI
bmi = hitung_bmi(berat_badan, tinggi_badan)

# Memberi rekomendasi berdasarkan BMI
rekomendasi = beri_rekomendasi(bmi)

# Menampilkan hasil
print("BMI Anda adalah:", round(bmi, 2))
print("Rekomendasi:", rekomendasi)