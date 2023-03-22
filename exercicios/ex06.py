valor = int(input("digite o valor "))
porcentagem = int(input("digite a porcentagem "))
desconto = (porcentagem/100)*valor
valor_com_desconto = valor - desconto
print(f"valor total é: {valor}")
print(f"valor do desconto é: {desconto}")
print(f"valor total com desconto é: {valor_com_desconto}")