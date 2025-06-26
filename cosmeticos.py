from inputs_validation import input_sem_acentos, validacao_de_input, pergunta

class Cosmeticos:
    estoque = []
    
    def __init__(self, nome, preco, quant):
        self.nome = nome
        self.preco = preco
        self.quant = quant

    def add_cosmeticos(self):
        self.nome = input_sem_acentos("Digite o nome do cosmético: ")
        self.preco = validacao_de_input("Digite o preço do cosmético: ", float, "O preço deve ser um número positivo.")
        self.quant = validacao_de_input("Digite a quantidade do cosmético: ", int, "A quantidade deve ser um número inteiro positivo.")

        produto = {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quant
        }

        print(f"\nProduto a adicionar: {produto}")

        resposta = pergunta("Deseja adicionar este produto? (s/n): ")
        if resposta == "s":
            Cosmeticos.estoque.append(produto)
            print("Produto adicionado com sucesso!")
        else:
            print("Produto não adicionado.")
            resposta_repetir = pergunta("Deseja tentar adicionar outro produto? (s/n): ")
            if resposta_repetir == "s":
                self.add_cosmeticos()

    def remover_cosmeticos(self):
        if not Cosmeticos.estoque:
            print("Nenhum produto no estoque.")
            return

        print("\nEstoque atual:")
        self.listar_cosmeticos()

        resposta = pergunta("Deseja remover um produto? (s/n): ")
        if resposta == "n":
            return

        numero = validacao_de_input("Digite o número do cosmético que deseja remover: ", int, "Número inválido.")
        if numero < 1 or numero > len(Cosmeticos.estoque):
            print("Número fora do intervalo.")
            return

        produto = Cosmeticos.estoque[numero-1]
        print(f"\nProduto selecionado: {produto['nome']}")

        confirmacao = pergunta("Confirmar remoção? (s/n): ")
        if confirmacao == "s":
            Cosmeticos.estoque.pop(numero-1)
            print("Produto removido com sucesso!")

    def att_produto(self):
        if not Cosmeticos.estoque:
            print("Nenhum produto no estoque.")
            return

        print("\nEstoque atual:")
        self.listar_cosmeticos()

        resposta = pergunta("Deseja atualizar um produto? (s/n): ")
        if resposta == "n":
            return

        numero = validacao_de_input("Digite o número do produto a atualizar: ", int, "Número inválido.")
        if numero < 1 or numero > len(Cosmeticos.estoque):
            print("Número fora do intervalo.")
            return

        produto = Cosmeticos.estoque[numero-1]
        print(f"\nEditando: {produto['nome']}")

        novo_nome = input_sem_acentos("Novo nome: ")
        novo_preco = validacao_de_input("Novo preço: ", float, "Preço inválido.")
        nova_quant = validacao_de_input("Nova quantidade: ", int, "Quantidade inválida.") 

        confirmacao = pergunta(f"Confirmar atualização para: Nome: {novo_nome}, Preço: {novo_preco}, Quantidade: {nova_quant}? (s/n): ")
        if confirmacao == "s":
            produto.update({
                "nome": novo_nome,
                "preco": novo_preco,
                "quantidade": nova_quant
            })
            print("Produto atualizado com sucesso!")

    def listar_cosmeticos(self):
        if not Cosmeticos.estoque:
            print("Nenhum produto no estoque.")
            return

        for i, produto in enumerate(Cosmeticos.estoque, 1):
            print(f"{i}. {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']}")

    def menu(self):
        while True:
            print("\nMenu de Cosméticos:")
            print("1. Adicionar Cosmético")
            print("2. Remover Cosmético")
            print("3. Atualizar Cosmético")
            print("4. Listar Cosméticos")
            print("5. Sair")

            opcao = validacao_de_input("Escolha uma opção: ", int, "Opção inválida.")

            match opcao:
                case 1:
                    self.add_cosmeticos()
                case 2:
                    self.remover_cosmeticos()
                case 3:
                    self.att_produto()
                case 4:
                    self.listar_cosmeticos()
                case 5:
                    print("Saindo do menu de cosméticos.")
                    return
                case _:
                    print("Opção inválida. Tente novamente.")

