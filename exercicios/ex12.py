a = float(input("peso "))
b = float(input("altura ")) / 100
imc = a/(b*b)
print(imc)
if imc < 18.5:
    print("Abaixo do Peso")
if imc > 18.6 and imc < 24.99:
    print("Saudavel")
if imc > 25.0 and imc < 29.99:
    print("Peso em excesso")
if imc > 30.0 and imc < 34.99:
    print("Obesidade Grau I")
if imc > 35.0 and imc < 39.99:
    print("Obesidade Grau II(severa)")
if imc >= 40.0:
    print("Obesidade Grau III(morbida)")
