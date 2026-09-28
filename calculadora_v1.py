while True:
    operacao = input(
        "Qual operação você deseja realizar?\n"
        "1 - Soma\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "5 - Potência\n"
        "0 - Sair\n"
    )

    if operacao == "0":
        print("Obrigado por usar a calculadora!")
        break

    elif operacao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1 + num2)

    elif operacao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1 - num2)

    elif operacao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1 * num2)

    elif operacao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1 / num2)

    elif operacao == "5":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1 ** num2)

    else:
        print("Operação inválida!")