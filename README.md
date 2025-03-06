# python

# Este programa permite que o usuário cadastre várias variáveis de forma interativa. 1 # Este programa permite que o usuário cadastre várias variáveis de forma interativa. 
# Ele solicita ao usuário que insira o nome da variável e o valor correspondente. 
# No final, ele exibe todas as variáveis cadastradas. 

# Criamos um dicionário para armazenar as variáveis cadastradas 
variaveis = {} 

print("Bem-vindo ao cadastro de variáveis!") 
print("Você pode cadastrar quantas variáveis quiser. Digite 'sair' para finalizar.") 
 
while True: 
    # Pedimos ao usuário para inserir o nome da variável 
    nome = input("Digite o nome da variável: ") 
 
    # Se o usuário digitar 'sair', o loop é interrompido 
    if nome.lower() == 'sair': 
        break 
 
    # Pedimos ao usuário para inserir o valor da variável 
    valor = input(f"Digite o valor para {nome}: ") 
    
    # Salvamos a variável no dicionário 
    variaveis [nome] = valor 

# Exibimos todas as variáveis cadastradas 
print("\nVariáveis cadastradas:") 
for nome, valor in variaveis.items(): 
    print(f"{nome} = {valor}") 

print("\nFim do programa! Obrigado por utilizar.") 
