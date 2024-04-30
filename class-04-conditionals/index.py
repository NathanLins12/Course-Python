age = 71

CNH = True

if age >= 18:
    print("maior de idade")
else :
    print("menor de idade")

if age >= 18 and CNH:
    print("pode dirigir")
else :
    print("não pode dirigir")


if age >= 18 and age <= 70:
    print("voto obrigatório")
elif age < 16:
    print("não pode votar")
else:
    print("voto facultativo")


try:
    print(2/0)
except ZeroDivisionError:
    print("não pode dividiir por zero")
except TypeError:
    print("formato inválido")
except:
    print("error!")
finally:
    print("fim da aquisição!")

print("running...")