class Model:
    def __init__(self):
        self.num1 = 0  # self é um código que permite que a variavel seja global
        self.num2 = 0

    def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'  # return apenas guarda a mensagem e finaliza o método

    def tabuada(self, num):
        resultado = "" #ASPAS MOSTRA QUE A VARIÁVEL É STRING
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num *i}\n' #+= É POR EXEMPLO: RESULTADO = RESULTADO +

        return resultado

    def mediaTres(self, nota1, nota2, nota3):
        return (nota1, nota2, nota3)/3


    def eh_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def calcular_fatorial(self, n):
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

    def imprimir_fibonacci(self):
        a, b = 0, 1
        print('Sequência de Fibonacci até o décimo termo:')
        for _ in range(10):
            print(a, end=' ')
            a, b = b, a + b
        print()

    def eh_fibonacci(self, n):
        if n < 0:
            return False
        a, b = 0, 1
        while a < n:
            a, b = b, a + b
        return a == n

    def soma_dos_digitos(self, n):
        soma = 0
        while n > 0:
            soma += n % 10
            n //= 10
        return soma


    def imprimir_pares_e_impares(self, n):
        pares = []
        impares = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                pares.append(i)
            else:
                impares.append(i)

        print(f'Números pares de 1 até {n}: {pares}')
        print(f'Números ímpares de 1 até {n}: {impares}')


    def imprimir_numeros_primos(self, n):
        primos = []
        for num in range(2, n + 1):
            if self.eh_primo(num):
                primos.append(num)

        print(f'Números primos de 1 até {n}: {primos}')


    def sequencia_collatz(self, n):
        sequencia = []
        while n != 1:
            sequencia.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        sequencia.append(1)
        print(f'Sequência de Collatz: {sequencia}')


    def soma_pares_impares(self, n):
        soma_pares = sum(i for i in range(1, n + 1) if i % 2 == 0)
        soma_impares = sum(i for i in range(1, n + 1) if i % 2 != 0)
        print(f'A soma dos números pares de 1 até {n} é: {soma_pares}')
        print(f'A soma dos números ímpares de 1 até {n} é: {soma_impares}')


    def verificar_numero_perfeito(self, n):
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        if soma_divisores == n:
            print(f'O número {n} é um número perfeito.')
        else:
            print(f'O número {n} não é um número perfeito.')


    def antecessor(self, num):
        return num - 1


    def area_retangulo(self, base, altura):
        return base * altura


    def idade_em_dias(self, anos, meses, dias):
        return (anos * 365) + (meses * 30) + dias


    def calcular_percentuais_votos(self, total_eleitores, brancos, nulos, validos):
        percentual_brancos = (brancos / total_eleitores) * 100
        percentual_nulos = (nulos / total_eleitores) * 100
        percentual_validos = (validos / total_eleitores) * 100
        return percentual_brancos, percentual_nulos, percentual_validos


    def calcular_novo_salario(self, salario_atual, percentual_reajuste):
        novo_salario = salario_atual + (salario_atual * (percentual_reajuste / 100))
        return novo_salario


    def calcular_custo_carro(self, custo_fabrica):
        percentual_distribuidor = 0.28
        percentual_impostos = 0.45
        custo_final = custo_fabrica + (custo_fabrica * percentual_distribuidor) + (custo_fabrica * percentual_impostos)
        return custo_final


    def calcular_media_final(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3


    def calcular_custo_macas(self, quantidade):
        if quantidade < 12:
            preco = 1.30
        else:
            preco = 1.00
        return quantidade * preco


    def ordenar_valores(self, valores):
        valores.sort()
        return valores


    def calcular_salario_vendedor(self, salario_fixo, vendas):
        if vendas <= 1500:
            comissao = vendas * 0.03
        else:
            comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)
        return salario_fixo + comissao


    def calcular_saldo(self, saldo, debito, credito):
        saldo_atual = saldo - debito + credito
        return saldo_atual



    def tabuada_limited(self, num):
        if 1 <= num <= 10:
            resultado = ""
            for i in range(1, 11):
                resultado += f'{num} * {i} = {num * i}\n'
            return resultado
        else:
            return "Número inválido! Por favor, insira um número entre 1 e 10."