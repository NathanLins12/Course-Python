def calc_imc(peso, altura):
    total =  peso / (altura * altura) 
    return total

peso = float(input("digite seu peso(kg): "))
altura = float(input("digite sua altura(m): "))
total = calc_imc(peso, altura)

print(f"Seu imc é {total:.2f}")
