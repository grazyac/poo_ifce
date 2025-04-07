from usuario import Usuario
from conta import Conta
import datetime
import random

def main():
    print("Criando usuário e conta bancária.")
    pessoa = Usuario()
    
    print("Por favor, informe seus dados pessoais:")
    pessoa.set_rg(int(input("RG (apenas números): ")))
    pessoa.set_cpf(int(input("CPF (apenas números): ")))
    pessoa.set_nome(input("Nome completo: "))
    
    print("Data de nascimento (dd/mm/aaaa): ")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    data_nasc = datetime.datetime(ano, mes, dia)
    pessoa.set_data_nascimento(data_nasc)
    
    print("\nAgora vamos criar sua conta bancária:")
    agencia = random.randint(0, 999)
    saldo_inicial = float(input("Saldo inicial: R$ "))
    data_abertura = datetime.datetime.now()
    
    minha_conta = Conta(agencia, pessoa, data_abertura, saldo_inicial)
    
    print("\nDados da conta criada:")
    print(f"Agência: {minha_conta.get_agencia():03d}")
    print(f"Data de abertura: {minha_conta.get_data_abertura().strftime('%d/%m/%Y %H:%M')}")
    print(f"Saldo atual: R$ {minha_conta.get_saldo():.2f}")
    
    print("\nDados do titular:")
    usuario = minha_conta.get_usuario()
    print(f"Nome: {usuario.get_nome()}")
    print(f"RG: {usuario.get_rg()}")
    print(f"CPF: {usuario.get_cpf()}")
    print(f"Data de Nascimento: {usuario.get_data_nascimento().strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()