# Calculadora de IMC (Índice de Massa Corporal)

# É necessário o seu peso (em Kg) e sua altura (Metros e centímetros)
# EX: 65 e 1.70

# O cálculo utilizado será o peso dividido pela altura ao quadrado (x²)


print("Olá, bem vindo a Calculadora de IMC")

pergunta_do_nome = input("Qual é o seu nome?")
Nome = print("Olá", pergunta_do_nome)
Idade = input(f"Quantos anos você tem?")
Peso = float(input("Qual é o seu peso(Em kg)?"))
Altura = float(input("Qual é a sua altura(Em metros, usando o ponto para os centímetros)?"))


print("Calculando")

IMC = (Peso / (Altura * Altura))

print(pergunta_do_nome)
print(Idade str("anos"))
print(Peso)
print(Altura)
print(IMC)

if IMC <= 16:
    print("Magreza grave\nProcure imediatamente atendimento médico")

elif IMC > 16 and IMC < 16.9:
    print("Magreza moderada\nTenha um maior cuidado com a sua saúde e alimentação")

elif IMC > 16.9 and IMC < 18.5:
    print("Magreza leve\nComece a rever a sua alimentação")

elif IMC > 18.5 and IMC < 24.9:
    print("Ideal\nVocê está normal. Continue assim, campeão!")

elif IMC > 24.9 and IMC < 29.9:
    print("Sobrepeso\nReveja a sua alimentação")

elif IMC > 29.9 and IMC < 34.9:
    print("Obesidade Grau I\nProcure um nutricionista")

elif IMC > 34.9 and IMC < 39.9:
    print("Obesidade Grau II\nProcure um nutricionista e um médico")

elif IMC >= 40:
    print("Procure imediatamente um nutricionista e um médico. Cuide de sua saúde!")



import pandas as pd

Tabela = {'IMC(Kg/m²)': {0: 'Abaixo de 16',
                         1: 'Entre 16 e 16,9',
                         2: 'Entre 17 e 18,5',
                         3: 'Entre 18,6 e 24,9',
                         4: 'Entre 25 e 29,9',
                         5: 'Entre 30 e 34,9',
                         6: 'Entre 35 e 39,9',
                         7: 'Igual ou maior que 40'},

          'Classificação': {0: 'Magreza grave',
                            1: 'Magreza moderada',
                            2: 'Magreza leve',
                            3: 'Ideal',
                            4: 'Sobrepeso',
                            5: 'Obesidade grau I',
                            6: 'Obesidade grau II ou severa',
                            7: 'Obesidade grau III ou mórbida' }}


df = pd.DataFrame(Tabela)

print(df)












                         
                         
                         

                        
                        
          
          
          
          
          
          
          
          
          