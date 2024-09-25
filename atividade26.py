# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0


#lista para armazenar as notas
notas = []


#recebe as notas dos alunos
for i in range(1, 6):
    nota = float(input(f"digite a nota {i}"))
    notas.append(nota)

#calcular a maior nota, menor nota e média
                       
maior_nota = max(notas)
menor_nota = min(notas)
média_nota = sum(notas) / len(notas) 

#exibe os resultados
print(f"maior nota: {maior_nota}")
print(f"menor nota: {menor_nota}")
print(f"média das notas: {média_nota}")
