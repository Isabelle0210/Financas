
import pandas as pd

meses = [
    {"nome": "Janeiro", "contas": []},
    {"nome": "Fevereiro", "contas": []},
    {"nome": "Março", "contas": []},
    {"nome": "Abril", "contas": []},
    {"nome": "Maio", "contas": []},
    {"nome": "Junho", "contas": []},
    {"nome": "Julho", "contas": []},
    {"nome": "Agosto", "contas": []},
    {"nome": "Setembro", "contas": []},
    {"nome": "Outubro", "contas": []},
    {"nome": "Novembro", "contas": []},
    {"nome": "Dezembro", "contas": []},
]


while True:
    print("--------------------------------------------------------")
    print("\nMenu:")
    print("1. Adicionar conta")
    print("2. Listar contas")
    print("3. Deletar conta")
    print("4. Sair")
    print("5. Gerar excel")
    print("--------------------------------------------------------")
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        nome = input('Nome da conta: ')
        mes = int(input('Mês (1-12): ')) - 1
        valor = float(input('Valor da conta, se for parcelado fale o valor total: '))
        meses[mes]["contas"].append({"nome": nome, "valor": valor})
        parcela = input('A conta é parcelada? (s/n): ').strip().lower()
        if parcela == 's':
            num_parcelas = int(input('Número de parcelas: '))
            valor_parcela = valor / num_parcelas
            for i in range(1, num_parcelas):
                mes_parcela = (mes + i) % 12
                meses[mes_parcela]["contas"].append({"nome": f'{nome} - Parcela {i+1}/{num_parcelas}', "valor": valor_parcela})
        print(f'Conta "{nome}" adicionada ao mês de {meses[mes]["nome"]}.')
        
        
        
    elif escolha == "2":
        mes = int(input('Mês para listar (1-12): ')) - 1
        if 0 <= mes < 12:
            print(f'\nContas de {meses[mes]["nome"]}:')
            if not meses[mes]["contas"]:
                print("  Nenhuma conta registrada.")
            else:
                for conta in meses[mes]["contas"]:
                    print(f'  - {conta["nome"]}: R$ {conta["valor"]:.2f}')
                    print(f'Total: R$ {sum(c["valor"] for c in meses[mes]["contas"]):.2f}')
    elif escolha == "3":
        mes = int(input('Mês para deletar conta (1-12): ')) - 1
        if 0 <= mes < 12:
            nome = input('Nome da conta a ser deletada: ')
            contas_mes = meses[mes]["contas"]
            for conta in contas_mes:
                if conta["nome"] == nome:
                    contas_mes.remove(conta)
                    print(f'Conta "{nome}" removida de {meses[mes]["nome"]}.')
                    break
            else:
                print(f'Conta "{nome}" não encontrada em {meses[mes]["nome"]}.')
    elif escolha == "4":
        print("Saindo...")
        break
    elif escolha == "5":
        dados = {}
        for i, mes in enumerate(meses):
            dados[mes["nome"]] = [conta["valor"] for conta in mes["contas"]]
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dados.items()]))
        df.to_excel("contas_mensais.xlsx", index=False)
        print("Arquivo 'contas_mensais.xlsx' gerado com sucesso.")
    
    else:
        print("Opção inválida. Tente novamente.")


