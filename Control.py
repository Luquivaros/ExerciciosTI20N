from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model()
        self.opcao = 0


    def mostrarMenu(self):
        print('Escolha uma das opções abaixo: ' +
              '\n1. Sair'                       +
              '\n2. Trocar'                     +
              '\n3. Tabuada'                    +
              '\n4. Media'                      +
              '\n5. Imprimir números de 1 a 10' +
              '\n6. Imprimir números pares de 1 a 20' +
              '\n7. Calcular a soma dos números de 1 a 100' +
              '\n8. Imprimir múltiplos de 5 de 1 a 50' +
              '\n9. Verificar se um número é par ou ímpar' +
              '\n10. Verificar se um número é positivo, negativo ou zero' +
              '\n11. Imprimir a tabuada de um número' +
              '\n12. Imprimir os números de 1 até o número informado' +
              '\n13. Imprimir a soma dos números de 1 até o número informado' +
              '\n14. Imprimir números primos de 1 a 20' +
              '\n15. Verificar se um número é primo' +
              '\n16. Calcular o fatorial de um número' +
              '\n17. Imprimir a sequência de Fibonacci até o décimo termo' +
              '\n18. Verificar se um número é um número de Fibonacci' +
              '\n19. Calcular a soma dos dígitos de um número' +
              '\n20. Imprima os números pares e ímpares' +
              '\n21. Imprimir números primos até o número informado' +
              '\n22. Imprimir a sequência de Collatz de um número' +
              '\n23. Calcular a soma dos números pares e ímpares de 1 até um número' +
              '\n24. Verificar se um número é perfeito' +
              '\n25. Antecessor' +
              '\n26. Área do Retângulo' +
              '\n27. Idade em Dias' +
              '\n28. Percentuais de Votos' +
              '\n29. Reajuste Salarial' +
              '\n30. Cálculo do Custo do Carro' +
              '\n31. Média Final do Aluno' +
              '\n32. Cálculo do Custo das Maçãs' +
              '\n33. Ordenar 10 Valores' +
              '\n34. Cálculo do Salário do Vendedor' +
              '\n35. Cálculo do Saldo da Conta' +
              '\n36. Mais uma Tabuada')


    def operacoes(self):
        while(self.opcao != 1): # != SINAL DE DIFERENTE
            self.mostrarMenu()
            self.opcao = int(input('Informe o número: ')) #int() força que a informação armazenada seja por obrigação um número
            if self.opcao == 1:
                print('Obrigado')

            elif self.opcao == 2:
                valorA = int(input('Informe um valor para A'))
                valorB = int(input('Informe um valor para B'))
                print(self.modelo.trocar(valorA, valorB))

            elif self.opcao == 3:
                num =  int(input('Informe um número: '))
                print(self.modelo.tabuada(num))

            elif self.opcao == 4:

                nota1 =  float(input('Primeira nota: '))
                while(nota1 < 0 or nota1 > 10):
                    print('Erro! Informe uma nota de 0 a 10.')
                    nota1 = float(input('Primeira nota: '))

                nota2 = float(input('Segunda nota: '))
                while (nota2 < 0 or nota2 > 10):
                    print('Erro! Informe uma nota de 0 a 10.')
                    nota2 = float(input('Segunda nota: '))

                nota3 = float(input('Terceira nota: '))
                while (nota3 < 0 or nota3 > 10):
                    print('Erro! Informe uma nota de 0 a 10.')
                    nota3 = float(input('Terceira nota: '))


            elif self.opcao == 5:
                for i in range(1, 11):
                    print(i)



            elif self.opcao == 6:
                for i in range(1, 21):
                    if i % 2 == 0:
                        print(i)


            elif self.opcao == 7:
                soma = sum(range(1, 101))
                print(f'A soma dos números de 1 a 100 é: {soma}')



            elif self.opcao == 8:
                for i in range(1, 51):
                    if i % 5 == 0:
                        print(i)


            elif self.opcao == 9:
                numero = int(input('Informe um número: '))
                if numero % 2 == 0:
                    print(f'O número {numero} é par.')
                else:
                    print(f'O número {numero} é ímpar.')



            elif self.opcao == 10:
                numero = float(input('Informe um número: '))
                if numero > 0:
                    print(f'O número {numero} é positivo.')
                elif numero < 0:
                    print(f'O número {numero} é negativo.')
                else:
                    print('O número é zero.')



            elif self.opcao == 11:
                num = int(input('Informe um número para a tabuada: '))
                print(self.modelo.tabuada(num))


            elif self.opcao == 12:
                numero = int(input('Informe um número: '))
                for i in range(1, numero + 1):
                    print(i)


            elif self.opcao == 13:
                numero = int(input('Informe um número: '))
                soma = sum(range(1, numero + 1))
                print(f'A soma dos números de 1 até {numero} é: {soma}')


            elif self.opcao == 14:
                print('Números primos de 1 a 20:')
                for num in range(1, 21):
                    if self.modelo.eh_primo(num):
                        print(num)


            elif self.opcao == 15:
                numero = int(input('Informe um número para verificar se é primo: '))
                if self.modelo.eh_primo(numero):
                    print(f'O número {numero} é primo.')
                else:
                    print(f'O número {numero} não é primo.')


            elif self.opcao == 16:
                numero = int(input('Informe um número para calcular o fatorial: '))
                if numero < 0:
                    print('Fatorial não é definido para números negativos.')
                else:
                    fatorial = self.modelo.calcular_fatorial(numero)
                    print(f'O fatorial de {numero} é: {fatorial}')


            elif self.opcao == 17:
                self.modelo.imprimir_fibonacci()


            elif self.opcao == 18:
                numero = int(input('Informe um número para verificar se é um número de Fibonacci: '))
                if self.modelo.eh_fibonacci(numero):
                    print(f'O número {numero} é um número de Fibonacci.')
                else:
                    print(f'O número {numero} não é um número de Fibonacci.')


            elif self.opcao == 19:
                numero = int(input('Informe um número para calcular a soma dos seus dígitos: '))
                soma_digitos = self.modelo.soma_dos_digitos(numero)
                print(f'A soma dos dígitos de {numero} é: {soma_digitos}')


            elif self.opcao == 20:
                numero = int(input('Informe um número: '))
                self.modelo.imprimir_pares_e_impares(numero)


            elif self.opcao == 21:
                numero = int(input('Informe um número: '))
                self.modelo.imprimir_numeros_primos(numero)


            elif self.opcao == 22:
                numero = int(input('Informe um número para calcular a sequência de Collatz: '))
                self.modelo.sequencia_collatz(numero)


            elif self.opcao == 23:
                numero = int(input('Informe um número: '))
                self.modelo.soma_pares_impares(numero)


            elif self.opcao == 24:
                numero = int(input('Informe um número: '))
                self.modelo.verificar_numero_perfeito(numero)


            elif self.opcao == 25:
                num = int(input('Informe um número: '))
                antecessor = self.modelo.antecessor(num)
                print(f'O antecessor de {num} é: {antecessor}')


            elif self.opcao == 26:
                base = float(input('Informe a base do retângulo: '))
                altura = float(input('Informe a altura do retângulo: '))
                area = self.modelo.area_retangulo(base, altura)
                print(f'A área do retângulo é: {area}')


            elif self.opcao == 27:
                anos = int(input('Informe os anos: '))
                meses = int(input('Informe os meses: '))
                dias = int(input('Informe os dias: '))
                total_dias = self.modelo.idade_em_dias(anos, meses, dias)
                print(f'A idade expressa em dias é: {total_dias}')


            elif self.opcao == 28:
                total_eleitores = int(input('Informe o número total de eleitores: '))
                brancos = int(input('Informe o número de votos brancos: '))
                nulos = int(input('Informe o número de votos nulos: '))
                validos = int(input('Informe o número de votos válidos: '))

                if brancos + nulos + validos > total_eleitores:
                    print('Erro! A soma dos votos brancos, nulos e válidos não pode exceder o total de eleitores.')
                else:
                    percentual_brancos, percentual_nulos, percentual_validos = self.modelo.calcular_percentuais_votos(
                        total_eleitores, brancos, nulos, validos)
                    print(f'Percentual de votos brancos: {percentual_brancos:.2f}%')
                    print(f'Percentual de votos nulos: {percentual_nulos:.2f}%')
                    print(f'Percentual de votos válidos: {percentual_validos:.2f}%')


            elif self.opcao == 29:
                salario_atual = float(input('Informe o salário atual: '))
                percentual_reajuste = float(input('Informe o percentual de reajuste: '))
                novo_salario = self.modelo.calcular_novo_salario(salario_atual, percentual_reajuste)
                print(f'O novo salário com reajuste é: R$ {novo_salario:.2f}')


            elif self.opcao == 30:
                custo_fabrica = float(input('Informe o custo de fábrica do carro: '))
                custo_final = self.modelo.calcular_custo_carro(custo_fabrica)
                print(f'O custo final do carro ao consumidor é: R$ {custo_final:.2f}')



            elif self.opcao == 31:
                nota1 = float(input('Informe a primeira nota: '))
                nota2 = float(input('Informe a segunda nota: '))
                nota3 = float(input('Informe a terceira nota: '))
                media_final = self.modelo.calcular_media_final(nota1, nota2, nota3)
                print(f'A média final do aluno é: {media_final:.2f}')


            elif self.opcao == 32:
                quantidade = int(input('Informe o número de maçãs compradas: '))
                custo_total = self.modelo.calcular_custo_macas(quantidade)
                print(f'O custo total da compra é: R$ {custo_total:.2f}')


            elif self.opcao == 33:
                valores = []
                print("Informe 10 valores distintos:")
                while len(valores) < 10:
                    valor = int(input(f'Informe o valor {len(valores) + 1}: '))
                    if valor in valores:
                        print('Valor repetido! Informe um valor diferente.')
                    else:
                        valores.append(valor)
                valores_ordenados = self.modelo.ordenar_valores(valores)
                print(f'Valores em ordem crescente: {valores_ordenados}')


            elif self.opcao == 34:
                salario_fixo = float(input('Informe o salário fixo do vendedor: '))
                vendas = float(input('Informe o valor total das vendas: '))
                salario_total = self.modelo.calcular_salario_vendedor(salario_fixo, vendas)
                print(f'O salário total do vendedor é: R$ {salario_total:.2f}')


            elif self.opcao == 35:
                numero_conta = input('Informe o número da conta do cliente: ')
                saldo = float(input('Informe o saldo: '))
                debito = float(input('Informe o débito: '))
                credito = float(input('Informe o crédito: '))

                saldo_atual = self.modelo.calcular_saldo(saldo, debito, credito)

                print(f'Saldo atual da conta {numero_conta}: R$ {saldo_atual:.2f}')

                if saldo_atual >= 0:
                    print('Saldo Positivo')
                else:
                    print('Saldo Negativo')


            elif self.opcao == 16:
                valor = int(input('Informe um número entre 1 e 10: '))
                tabuada_resultado = self.modelo.tabuada_limited(valor)
                print(tabuada_resultado)



            else:
                print('Opção escolhida não é válida!')