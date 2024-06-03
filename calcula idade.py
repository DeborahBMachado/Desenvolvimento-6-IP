def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Nasceu em que ano? "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Digite um valor numérico válido para o ano.")

def calcular_idade(ano_nascimento):
    ano_atual = 2024
    idade = ano_atual - ano_nascimento
    return idade

def main():
    print("Bem-vindo ao sistema de cálculo de idade!")
    nome = input("Como se chama? ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"{nome} tem {idade} anos.")

if __name__ == "__main__":
    main()
