ht = float(input("digite a horas trabalhadas no mês: "))
vh = float(input("digite o valor hora trabalhada: "))
pd = float(input("digite a porcentual desconto: "))

sb= ht*vh
td= (pd/100)*sb
sl= sb-td

print("Valores H:",ht)
print("Valores salario bruto:R$",sb)
print("Valores desconto:R$",td)
print("Valores salario liquido:R$",sl)


