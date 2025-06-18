import random

alunos = ["Adrian", "Angelo", "Arthur", "carlos", "Christopher", 
         "Douglas", "Emanuelly", "Everson", "Gabriel", "Guilherme", 
         "Gustavo A.", "Gustavo P.", "Gustavo F.", "Isabella", "Jamile", 
         "Joao M.", "João O.", "Joaquim", "Kalikey", "Luis", 
         "Maria", "Pedro A.", "pedro G", "Rafael N.", "Raphael S", 
         "Rapahel H.", "Roberto", "Sofia", "Stephanie"]

random.shuffle(alunos)

largura = max(len(nome) for nome in alunos) + 4
for i in range(0, len(alunos), 4):
    linha = alunos[i:i+4]

    linha_topo = "".join("+" + "-" * largura for _ in linha) + "+"
    linha_meio = "".join("|" + nome.center(largura) for nome in linha) + "|"
    linha_base = "".join("+" + "-" * largura for _ in linha) + "+"

    print(linha_topo)
    print(linha_meio)
    print(linha_base)
