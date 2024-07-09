#Questão 05

var_1 = int(input("Digite o primeiro valor positivo: "))
var_2 = int(input("Digite o segundo valor positivo: "))

var_soma1 = 0
var_soma = 0

for i in range(var_1, var_2 + 1):
    print(i, end= (" , "))
    if i == 3 or i == 5 or i == 2:
        var_soma1 += i
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 :
        print("Esse numero não é primo: " , i)
    else:
       var_soma += i
var_final = var_soma + var_soma1

print("O valor final é: ", var_final -1)
