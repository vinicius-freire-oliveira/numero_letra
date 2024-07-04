def numero_para_letras(numeros):
    # Cria uma string vazia para armazenar o resultado
    resultado = ''
    
    # Percorre cada número na string de entrada
    for numero in numeros:
        # Converte o número (caractere) em inteiro
        posicao = int(numero)
        
        # Calcula a letra correspondente (A = 1, B = 2, ..., Z = 26)
        # chr(64 + posicao) converte a posição na letra correta
        letra = chr(64 + posicao)
        
        # Adiciona a letra ao resultado
        resultado += letra
    
    return resultado

def letras_para_numero(letras):
    # Cria uma string vazia para armazenar o resultado
    resultado = ''
    
    # Percorre cada letra na string de entrada
    for letra in letras:
        # Calcula a posição numérica da letra (A = 1, B = 2, ..., Z = 26)
        # ord(letra) - 64 converte a letra na posição correta
        posicao = ord(letra.upper()) - 64
        
        # Adiciona a posição ao resultado
        resultado += str(posicao)
    
    return resultado

def mostrar_menu():
    # Exibe o menu de opções para o usuário
    print("\nEscolha a operação desejada:")
    print("1 - Converter números para letras")
    print("2 - Converter letras para números")
    print("3 - Sair")

def main():
    while True:
        # Exibe o menu e solicita uma opção ao usuário
        mostrar_menu()
        opcao = int(input("Escolha uma opção (1-3): "))

        if opcao == 1:
            # Solicita ao usuário que digite uma sequência de números
            numeros = input("Digite uma sequência de números: ")
            # Converte a sequência de números em letras
            resultado = numero_para_letras(numeros)
            print("Resultado:", resultado)
        
        elif opcao == 2:
            # Solicita ao usuário que digite uma sequência de letras
            letras = input("Digite uma sequência de letras: ")
            # Converte a sequência de letras em números
            resultado = letras_para_numero(letras)
            print("Resultado:", resultado)
        
        elif opcao == 3:
            # Sai do programa se o usuário escolher a opção 3
            print("Saindo do programa.")
            break
        
        else:
            # Informa ao usuário que a opção é inválida
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
