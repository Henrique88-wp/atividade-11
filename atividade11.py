# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)


a = int(input("coloque sua idade"))
if a<=12 :
    print("você é criança")
elif a<=17 :
    print("você é adolecente")
elif a<=59 :
    print("você é adulto")
elif a<=60 :
    print("você é idoso.")