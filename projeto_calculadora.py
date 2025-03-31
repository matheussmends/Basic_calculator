""" 
    Este projeto tem como finalidade exercer calculos básicos de uma calculadora funcional, tais como:

        1. Adição
        2. Subtração
        3. Multiplicação
        4. Divisão
        5. Raiz Quadrada
        6. Potênciação
        7. Porcentagem
"""


import math

print("===" * 15)
def calcular():
    while True:
        try:    
            print("Escolha a operação matemática. \n")
            print("1. Adição")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Raiz Quadrada")
            print("6. Potência")
            print("7. Porcentagem")
            print("8. Sair\n") # Precisa dessa opção para sair do loop infinito.
        
            selecao = input("Selecione a opção desejada: ")

            if selecao =='1':
                print("Você selecionou Adição!\n")

                numero1 = float(input("Digite o primeiro numero: "))
                numero2 = float(input("Digite o segundo numero: "))
                print(f"\nO seu resultado é: {numero1 + numero2}")
                print("===" * 15)
                break

            elif selecao == '2':
                print("Você selecionou Subtração!\n")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                print(f"\nO resultado da é: {numero1 - numero2}")
                print("===" * 15)
                break
            
            elif selecao == '3':
                print("Você selecionou Multiplicação!\n")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                print(f"\nO resultado é: {numero1 * numero2}")
                print("===" * 15)
                break
            
            elif selecao == '4':
                print("Você selecionou Divisão!")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                if numero2 == 0:
                    print("\nNão é possível fazer divisões por 0")
                    print("===" * 15)
                else:
                    print(f"\nO resultado é: {numero1 / numero2}")
                    print("===" * 15)
                    break

            elif selecao == '5':
                print("Você selecionou Raiz Quadrada! ")
                numero1 = float(input("Digite um numero para calcular a Raiz Quadrada: "))
                if numero1 < 0:
                    print("Não é possível calcular a raiz quadrada de um número Negativo")
                else:
                    print(f"\nO resultado da Raiz Quadrada de {numero1} é: {math.sqrt(numero1)}")
                    print("===" * 15)
                    break

            elif selecao == '6':
                print("Você Selecionou Potência!")
                numero1 = float(input("Digite o número: "))
                print(f"\nO resultado da potência é: {numero1 ** 2}")
                print("===" * 15)
                break
                
            elif selecao == '7':
                print("Você selecionou Porcentagem!")
                numero1 = float(input("Digite o número: "))
                porcentagem = float(input("Quantos % você quer saber do número? "))
                print(f"\nResultado: {porcentagem}% de {numero1} é: {porcentagem / 100 * numero1}")
                print("===" * 15)
                break

            elif selecao == '8':
                print("\nAté o próximo cálculo!! :)")
                print("===" * 15)
                break
            else:
                print("\nOpcão inválida, tente novamente.\n")
                print("===" * 15)
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            print("===" * 15)
            break


if __name__ == "__main__":
    calcular()