num1 = int(input('Digite o valor inicial:'))
num2 = int(input('Digite o valor final:'))
num3 = int(input('Digite o incremento:'))

for i in range(num1, num2, num3):  
    tempf = i*1.8+32
    print(f"{i}°C = {tempf}°F")
print('Programa encerrou')