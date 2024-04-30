student_g1 = float(input("digite a primeira nota do aluno: "))
student_g2 = float(input("digite a segunda nota do aluno: "))

average = (student_g1 + student_g2) / 2

if average < 7:
    print("não passou!")
else:
    print("passou!")