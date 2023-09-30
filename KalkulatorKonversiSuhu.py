print("= = = = = = = = = = = = = = = = = ")
print("= KALKULATOR KONVERSI TEMPERATUR =")
print("= = = = = = = = = = = = = = = = = ")

celcius = float(input('Masukan sushu ke dalam Celcius = '))
print("Suhu adalah ", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Fahrenheit
farenhait = ((9/6) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", farenhait, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

print ("===========================================\n")

Fahrenheit = float (input('Masukan suhu ke dalam Fahrenheit = '))
print("Suhu dalam Fahrenheit adalah ", Fahrenheit, "Fahrenheit")

# Kelvin
FahrenheittoKelvin =  (Fahrenheit - 32) * (5/9) + 273
print("Suhu Fahrenheit to Kelvin:  ", FahrenheittoKelvin, "Kelvin")

print ("===========================================\n")

Kelvin = float (input('Masukan suhu ke dalam Kelvin ='))
print("Suhu dalam kelvin adalah ", Kelvin, "Kelvin")

# Fahrenheit
KelvintoFahrenheit = (Kelvin - 273) * (9/5) + 32
print("Suhu Kelvin to Fahrenheit:  ", KelvintoFahrenheit, "Fahrenheit")
