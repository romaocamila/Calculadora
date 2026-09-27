sim_equivalencias = {"s", "si", "sim", "yes"}
nao_equivalencias = {"n", "nao", "não", "no"}

operacao = ""

while operacao != "0":

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

    elif operacao not in {"1", "2", "3", "4", "5"}:
        print("Operação inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    except ValueError:
        print("Por favor, digite números válidos.")
        continue

    if operacao == "1":
        print(num1 + num2)

    elif operacao == "2":
        print(num1 - num2)

    elif operacao == "3":
        print(num1 * num2)

    elif operacao == "4":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Não é possível dividir por zero.")

    elif operacao == "5":
        print(num1 ** num2)

    loop = input(
        "Você deseja continuar calculando? Digite SIM ou NÃO: "
    ).strip().lower()

    if loop in sim_equivalencias:
        continue

    elif loop in nao_equivalencias:
        print("Obrigado por usar a calculadora!")
        break

    else:
        print("Resposta inválida. Por favor, digite 'SIM' ou 'NÃO'.")
        break