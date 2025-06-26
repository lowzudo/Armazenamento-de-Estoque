from usuario import UserValidation
from Pcs import PcGamer
from mercadoestoque import MercadoEstoque
from cosmeticos import Cosmeticos
from inputs_validation import input_sem_acentos, validacao_de_input, pergunta

class Megaestoque:

    def __init__(self):
        self.usuario = UserValidation()
        self.pc_gamer = PcGamer("", "", 0, 0, "")
        self.mercado = MercadoEstoque()
        self.cosmeticos = Cosmeticos("", 0, 0)
        self.estoque = {
            "computadores": self.pc_gamer.estoque,
            "mercado": self.mercado.estoque,
            "cosmeticos": self.cosmeticos.estoque
        }

    def iniciar(self):
        print("Bem-vindo ao Mega Estoque!\n")
        print("Você está prestes a criar uma conta.\n")
        print("Por favor, siga as instruções para criar sua conta.\n")
        self.usuario.criar_conta()

        while True:
            print("--MENU--")
            print("1. Computadores")
            print("2. Mercado")
            print("3. Cosméticos")
            print("4. Sair")

            opcao = validacao_de_input("Escolha uma opção: ", int, "Opção inválida.")
            match opcao:
                case 1:
                    self.pc_gamer.menu()
                case 2:
                    self.mercado.menu()
                case 3:
                    self.cosmeticos.menu()
                case 4:
                    print("Saindo do Mega Estoque.\n")
                    print(f"Todo o estoque: {self.estoque}")
                    return
                case _:
                    print("Opção inválida. Tente novamente.")


megaestoque1 = Megaestoque()
megaestoque1.iniciar()
