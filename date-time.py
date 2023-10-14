import datetime as dt

print ("= = = KALKULATOR DAY'S = = =")
print ("Silahkan untuk memasukan tanggal lahir anda ^_^\n")

tanggal = int(input("Masukkan tanggal : "))
bulan = int(input("Masukan bulan : "))
tahun = int(input("Masukan tahun : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)

print(f"Tanggal lahir anda : {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}\n")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}\n")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days / 365
print (f"Umur anda adakah {umur_tahun} tahun")