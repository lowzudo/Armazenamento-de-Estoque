from inputs_validation import input_sem_acentos, validacao_de_input, pergunta

class PcGamer:
    estoque = []

    def __init__(self, placa_video, placa_mae, memoria, RAM, processador):
        self.placa_video = placa_video
        self.placa_mae = placa_mae
        self.processador = processador
        self.RAM = RAM
        self.memoria = memoria

    def Add_Pc(self):
        self.placa_video = input_sem_acentos("Placa de vídeo: ")
        self.placa_mae = input_sem_acentos("Placa mãe: ")
        self.processador = input_sem_acentos("Processador: ")
        self.memoria = validacao_de_input("Memória (GB, APENAS NÚMEROS !): ", int, "Valor inválido.")
        self.RAM = validacao_de_input("RAM (GB, APENAS NÚMEROS !): ", int, "Valor inválido.")
        
        computador = {
            "Placa de Video": self.placa_video,
            "Placa Mãe": self.placa_mae,
            "Processador": self.processador,
            "RAM": f"{self.RAM} GB",
            "Memória": self.memoria
        }
        
        confirmacao = pergunta(f"Confirmar adição do computador: {computador}? (s/n): ")
        if confirmacao == "s":
            PcGamer.estoque.append(computador)
            return "Computador adicionado!"
        return "Operação cancelada."

    @classmethod
    def Remover(cls):
        if not cls.estoque:
            print("Nenhum computador no estoque.")
            return
            
        print("Computadores disponíveis para remover:")
        for i, comp in enumerate(cls.estoque):
            print(f"{i+1} - {comp['Placa de Video']}")
            
        indice = validacao_de_input("Qual deseja remover? ", int, "Índice inválido.") - 1
        
        if 0 <= indice < len(cls.estoque):
            confirmacao = pergunta(f"Confirmar remoção de {cls.estoque[indice]['Placa de Video']}? (s/n): ")
            if confirmacao == "s":
                removido = cls.estoque.pop(indice)
                print(f"{removido['Placa de Video']} removido.")
        else:
            print("Índice inválido.")

    @classmethod
    def Listar(cls):
        if not cls.estoque:
            print("Nenhum computador no estoque.")
            return
            
        for i, comp in enumerate(cls.estoque):
            print(f"{i+1} - Placa de Vídeo: {comp['Placa de Video']}, Placa Mãe: {comp['Placa Mãe']}, Processador: {comp['Processador']}, RAM: {comp['RAM']}, Memória: {comp['Memória']} GB")

        if pergunta("\nDeseja trocar a posição de algum computador? (s/n): ") == "s":
            origem = validacao_de_input("Digite a posição atual do PC: ", int, "Posição inválida.") - 1
            destino = validacao_de_input("Digite a nova posição: ", int, "Posição inválida.") - 1
            
            if 0 <= origem < len(cls.estoque) and 0 <= destino < len(cls.estoque):
                confirmacao = pergunta(f"Confirmar troca da posição {origem+1} com {destino+1}? (s/n): ")
                if confirmacao == "s":
                    pc = cls.estoque.pop(origem)
                    cls.estoque.insert(destino, pc)
                    print("Posição trocada com sucesso!")
            else:
                print("Posições inválidas.")

    @classmethod
    def menu(cls):
        while True:
            print("\n--- Menu dos Computadores ---")
            print("1 = Adicionar")
            print("2 = Remover")
            print("3 = Listar")
            print("4 = Sair")
            
            alternativa = validacao_de_input("Escolha a opção: ", int, "Opção inválida.")

            match alternativa:
                case 1:
                    temp = PcGamer("", "", 0, 0, "")
                    print(temp.Add_Pc())
                case 2:
                    cls.Remover()
                case 3:
                    cls.Listar()
                case 4:
                    print("Saindo...")
                    return
                case _:
                    print("Opção inválida.")