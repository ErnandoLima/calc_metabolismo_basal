print("Ola, seja bem vindo a calculadora de metabolismo basal")
print("Por favor, forneça os seguintes dados solicitados")

sexo = input("Digite -m- para masculino ou -f- para feminino: ")
peso_em_kg = float(input("Digite seu peso em KG: "))
altura_em_cm = int(input("Informe sua altura em centímetros: "))
idade = int(input("Informe sua idade: "))


if sexo == "m":
    tmb_homem = 88.362 + (13.397 * peso_em_kg) + (4.799 * altura_em_cm) - (5.677 * idade) 
    print("Sua taxa de metabolismo basal é: ",tmb_homem)

elif sexo == "f":
    tmb_mulher = 447.593 + (9.247 * peso_em_kg) + (3.098 * altura_em_cm) - (4.330 * idade)
    print("Sua taxa de metabolismo basal é: ", tmb_mulher)

else:
    print("Inválido")