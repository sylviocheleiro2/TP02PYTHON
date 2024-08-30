import pandas as pd
import csv


def exercicio_1():
    print("Exercicio 1")
    # Exercicio 1: Utilize o módulo csv de Python para criar um arquivo chamado data.csv e grave as seguintes linhas no arquivo:
    data = {
        "name": ["Alice", "Bob", "Carol"],
        "age": [30, 25, 27],
        "city": ["New York", "Los Angeles", "Chicago"]
    }
    with open("data.csv", mode="w", newline="") as file:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(data["name"])):
            writer.writerow({
                "name": data["name"][i],
                "age": data["age"][i],
                "city": data["city"][i]
            })


def exercicio_2():
    print("Exercicio 2")
    # Exercicio 2: Utilize o módulo csv para ler o conteúdo do arquivo data.csv criado na pergunta 1 e exiba os dados lidos na tela.

    with open("data.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def exercicio_3():
    print("Exercicio 3")
    # Exercicio 3: Escreva um código que leia o arquivo data.csv e armazene as informações em uma lista de dicionários. Cada dicionário deve representar uma linha do CSV.

    data_list = []
    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_list.append(dict(row))

            # Exercicio 4: Modifique o código da pergunta 3 para que ele leia o arquivo CSV e exiba a idade da pessoa que mora em Los Angeles.

            #
            if row['city'] == 'Los Angeles':
                print(f"A idade da pessoa que mora em Los Angeles é: {
                      row['age']})")
            #

        print(data_list)


def exercicio_4():
    print("Exercicio 4")
    # ACIMA!


def exercicio_5():
    print("Exercicio 5")
    # Exercicio 5: Crie um código que leia um arquivo com as colunas date, amount e calcule o total das vendas. O arquivo contém:

    data2 = [
        {"date": "2024-01-01", "amount": 200},
        {"date": "2024-01-02", "amount": 300},
        {"date": "2024-01-03", "amount": 300},
    ]
    with open("data2.csv", mode="w", newline="") as file:
        fieldnames = ["date", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data2)

    vendas_totais = 0
    with open("data2.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            vendas_totais += int(row['amount'])
        print(f"O total das vendas é: {vendas_totais}")


def exercicio_6():
    print("Exercicio 6")
    # Exercicio 6: Utilize o módulo csv para criar um arquivo orders.csv com as colunas order_id, product, quantity. Adicione dados de exemplo e leia o arquivo para imprimir os dados.
    orders_data = [
        {"order_id": 1, "product": "Laptop", "quantity": 2},
        {"order_id": 2, "product": "Mouse", "quantity": 5},
        {"order_id": 3, "product": "Keyboard", "quantity": 3},
    ]

    with open("orders.csv", mode="w", newline="") as file:
        fieldnames = ["order_id", "product", "quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders_data)

        print("Arquivo orders.csv criado com sucesso.")


def exercicio_7():
    print("Exercicio 7")
    # Exercicio 7: Escreva um código Python para contar o número de linhas no arquivo orders.csv criado na pergunta 6.
    line_count = 0
    with open("orders.csv", mode="r") as file:
        reader = csv.reader(file)
        for linha in reader:
            line_count += 1
        print(f"O arquivo 'orders.csv' contém {line_count} linhas.")


def exercicio_8():
    print("Exercicio 8")
    # Exercicio 8: Crie um DataFrame em Pandas a partir do arquivo employees.csv e salve o DataFrame em um novo arquivo employees_copy.csv.
    data3 = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Carol"],
        "salary": [50000, 55000, 60000]
    }

    df3 = pd.DataFrame(data3)

    df3.to_csv("employees.csv", index=False)


def exercicio_9():
    print("Exercicio 9")
    # Exercicio 9: Escreva um código utilizando Pandas para mostrar o nome do empregado com maior salário no arquivo criado na pergunta 8.

    df = pd.read_csv("employees.csv")
    max_salary_row = df.loc[df['salary'].idxmax()]
    print(f"O empregado com o maior salário é: {max_salary_row['name']}")


def exercicio_10():
    print("Exercicio 10")
    # Exercicio 10:  Escreva um código que leia o arquivo CSV seguinte e carregue apenas as linhas que contêm “In progress” na coluna description.
    data4 = {
        "id": [1, 2, 3, 4],
        "description": ["Complete sales report", "Meeting with ABC client", "Prepare presentation", "Approve website layout"],
        "status": ["In progress", "Completed", "In progress", "In progress"],
        "due_date": ["2024-09-09", "2024-08-01", "2024-08-10", "2024-08-10"]
    }
    df4 = pd.DataFrame(data4)
    df4.to_csv("empresa.csv", index=False)
    df4 = pd.read_csv("empresa.csv")
    filtered_df = df4[df4['status'] == 'In progress']
    print(filtered_df)


def exercicio_11():
    print("Exercicio 11")
    #  Exercicio 11: Leia um arquivo que usa pipes (|) como delimitador. O arquivo contém as colunas item|quantity|price. Imprima os dados lidos.
    data5 = {
        "item": ["Apples", "Oranges", "Bananas"],
        "quantity": [10, 5, 7],
        "price": [0.50, 0.75, 0.30]
    }
    df5 = pd.DataFrame(data5)
    df5.to_csv("items_pipe.csv", sep='|', index=False)
    df5 = pd.read_csv("items_pipe.csv", delimiter='|')
    print(df5)


def exercicio_12():
    print("Exercicio 12")
    # Exercicio 12: Escreva um código para salvar um DataFrame Pandas em um arquivo CSV onde o delimitador é um ponto e vírgula (;).
    data6 = {
        "item": ["Apples", "Oranges", "Bananas"],
        "quantity": [10, 6, 7],
        "price": [0.60, 0.76, 0.30]
    }
    df6 = pd.DataFrame(data6)
    df6.to_csv("frutas_with;.csv", sep=';', index=False)


def exercicio_13():
    print("Exercicio 13")
    # Exercicio 13: Crie um arquivo info.json com o seguinte conteúdo e leia-o em um DataFrame Pandas.
    data = {
        "name": ["Alice", "Bob", "Carol"],
        "age": [30, 25, 27],
        "city": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)
    df.to_json("data.json", orient="records")


def exercicio_14():
    print("Exercicio 14")
   # Exercicio 14:  Utilize Pandas para carregar um arquivo employees.json com dados de funcionários e exiba a média dos salários.
    df = pd.read_csv("employees.csv")
    df.to_json("employees.json", orient="records", lines=False)
    df = pd.read_json("employees.json", orient="records")
    media = df['salary'].mean()
    print(f"A média dos salários é: {media}")


def exercicio_15():
    print("Exercicio 15")
# Exercicio 15: Escreva um código para converter um DataFrame Pandas em um arquivo JSON e salve-o como output.json.
    df = pd.read_csv("empresa.csv")
    df.to_json("empresa.json", orient="records", lines=False)
    df = pd.read_json("empresa.json", orient="records")
    print(df)


def exercicio_16():
    print("Exercicio 16")
    # Exercicio 16: Leia o arquivo seguinte e utilize Pandas para normalizar e exibir as informações em um formato tabular.
    json = [
        {
            "user_id": 1,
            "username": "UserA",
            "activities": [
                {
                        "activity_id": "act001",
                        "action": "Login",
                        "timestamp": "2023-01-01T10:00:00"
                },
                {
                    "activity_id": "act002",
                    "action": "Post Comment",
                    "timestamp": "2023-01-01T10:05:00"
                }
            ]
        },
        {
            "user_id": 2,
            "username": "UserB",
            "activities": [
                {
                        "activity_id": "act003",
                        "action": "Upload Video",
                        "timestamp": "2023-01-02T09:30:00"
                }
            ]
        }
    ]
    df = pd.json_normalize(json, record_path='activities',
                           meta=['user_id', 'username'])
    print(df)

# NÃO EDITE O CÓDIGO ABAIXO


def main():
    functions = [
        exercicio_1, exercicio_2, exercicio_3, exercicio_4, exercicio_5,
        exercicio_6, exercicio_7, exercicio_8, exercicio_9, exercicio_10,
        exercicio_11, exercicio_12, exercicio_13, exercicio_14, exercicio_15,
        exercicio_16
    ]

    for func in functions:
        print(f"Executando exercício {func.__name__}()")
        try:
            func()
        except Exception as e:
            print(f"Ocorreu um erro ao executar o exercício {func.__name__}()")
            print(e)


if __name__ == "__main__":
    main()
