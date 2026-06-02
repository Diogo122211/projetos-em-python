print("MENU")
print("1 Dolar para Real ")
print("2 EURO para Real ")

opcao = input("Escolha uma Opção")

if opcao == "1":
    dolar = float(input("Digite o valor em $: "))
    calculo = dolar * 5.16
    print("Valor em R$:", calculo)

if opcao == "2":
    euro = float(input("Digite o valor em $: "))
    calculo = euro * 5.60
    print("Valor em R$:", calculo)



