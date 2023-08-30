# William José Gomes Pinto Junior

# Inputs

nota1 = float(input("Informe um número: "))
nota2 = float(input("Informe um número: "))
nota3 = float(input("Informe um número: "))
nota4= float(input("Informe um número: "))
nota5 = float(input("Informe um número: "))

# Cálculos

media = (nota1 + nota2 + nota3+ nota4 + nota5) / 5

# Condições

if ( media >= 70):
    print(f"Parabéns!, você está aprovado, sua média foi {media:.2f}")
else:
    print(f"Infelizmente você foi reprovado, sua média foi {media:.2f}")