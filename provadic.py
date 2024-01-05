alunado = {1234  : "Diana Soares", 3456 : "João Gomes", 2345 : "Marcos Saraiva"}

while True:    
    matricula=int(input("Digite número de matrícula: "))
    if matricula == 0000:
        break        
    nome=str(input("Digite o nome do aluno: "))
    alunado.update([[matricula, nome]])
print(alunado)

deletar = int(input("Digite o número de matrícula a ser deletado: "))
del alunado[deletar]
print(alunado)


# alunos = [
#     {
#         "matricula": 1234,
#         "nome": "david"
#     },
#     {
#         "matricula": 34,
#         "nome": "vid"
#     },
#     {
#         "matricula": 234,
#         "nome": "da"
#     },
# ]

# newaluno = {
#     "matrivulo": input('digite a matricula'),
#     "nome": input('digiteo nome'),
# }

# alunos.append(newaluno)

# for aluno in alunos:
#     print(aluno["matricula"], aluno["nome"])

# ptint('[1] continuas'
#       '[2] deletar'
#       '[0] sair')

# res = input('sua escolha')

        