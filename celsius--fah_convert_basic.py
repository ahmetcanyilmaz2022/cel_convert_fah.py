
#1. YÖNTEM FORMAT METHODU

f1_convert_c1  = (( 1 * 1.8) + 32)
c1_convert_f1 = ((1-32)/1.8)
print(f1_convert_c1)
print(c1_convert_f1)
fahrenheit = -17.22 # 1 fah = -17.22 cel
celsius = 33.8 # 1 cel =33.8 fah

print("{} Celsius derece {} derece Fahrenheit'a eşittir.".format(celsius,fahrenheit))
print("{} Fahrenheit derece {} derece Celsius'a eşittir.".format(fahrenheit,celsius))
print(" 1 Celsius derece {} derece Fahrenheit'a eşittir.".format(fahrenheit))
print(" Fahrenheit derece {} derece Celsius'a eşittir.".format(celsius))

----------------------------------------------------------------------------------------------------
#2. YÖNTEM İMPUT İLE..

#  celsius -  fahrenheit dönüştürücü

celsius = float(input("Sıcaklık:"))

# hesapla
fahrenheit = (celsius * 1.8) + 32

print("%0.1f Celsius derece %0.1f derece Fahrenheit'a eşittir." %(celsius,fahrenheit))

------------------------------------------------------------------------------------------------------
