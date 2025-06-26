from inputs_validation import input_sem_acentos, validacao_de_input, pergunta

class MercadoEstoque:
    estoque = []

    def __init__(self):
        pass

    def att_produto(self):
        if not MercadoEstoque.estoque:
            print("Nenhum produto no estoque.")
            return
        
        print("Produtos disponíveis:")
        for i, produto in enumerate(MercadoEstoque.estoque):
            print(f"{i+1} - {produto['nome']}")

        self.pergunta1 = validacao_de_input("Digite o número do produto que deseja atualizar: ", int, "Número inválido.") - 1
        
        if not 0 <= self.pergunta1 < len(MercadoEstoque.estoque):
            print("Número fora do intervalo.")
            return
            
        produto = MercadoEstoque.estoque[self.pergunta1]
        print(f"Produto selecionado: {produto}")

        novo_nome = input_sem_acentos("Digite o nome que precisa ser atualizado: ")
        novo_preco = validacao_de_input("Novo preço: ", float, "Preço inválido.")
        nova_quantidade = validacao_de_input("Nova quantidade: ", int, "Quantidade inválida.")

        confirmacao = pergunta(f"Confirmar atualização para: Nome: {novo_nome}, Preço: {novo_preco}, Quantidade: {nova_quantidade}? (s/n): ")
        if confirmacao == "s":
            produto.update({
                "nome": novo_nome,
                "preco": novo_preco,
                "quantidade": nova_quantidade
            })
            print("Produto atualizado com sucesso!")

    def add_produto(self):
        produto = {}
        
        while True:
            nome = input_sem_acentos("Digite o nome do produto para adicionar em seu estoque: ")
            
            if any(p["nome"] == nome for p in MercadoEstoque.estoque):
                print("Produto já se encontra no estoque.")
                if pergunta("Deseja tentar outro nome? (s/n): ") == "n":
                    return
                continue
                
            preco = validacao_de_input("Digite o preço do produto: ", float, "O preço deve ser um número positivo.")
            quant = validacao_de_input("Digite a quantidade do produto: ", int, "A quantidade deve ser um número inteiro positivo.")

            confirmacao = pergunta(f"Confirmar produto: {nome} | Preço: {preco} | Quantidade: {quant}? (s/n): ")
            if confirmacao == "s":
                produto = {
                    "nome": nome,
                    "preco": preco,
                    "quantidade": quant
                }
                MercadoEstoque.estoque.append(produto)
                print("Produto adicionado com sucesso!")
                return
            else:
                if pergunta("Deseja tentar novamente? (s/n): ") == "n":
                    return

    def remover_produto(self):
        if not MercadoEstoque.estoque:
            print("Nenhum produto no estoque.")
            return

        print("Produtos disponíveis:")
        for i, produto in enumerate(MercadoEstoque.estoque):
            print(f"{i+1} - {produto['nome']}")

        indice = validacao_de_input("Digite o número do produto que deseja remover: ", int, "Número inválido.") - 1
        
        if not 0 <= indice < len(MercadoEstoque.estoque):
            print("Número fora do intervalo.")
            return

        produto = MercadoEstoque.estoque[indice]
        confirmacao = pergunta(f"Confirmar remoção do produto {produto['nome']}? (s/n): ")
        if confirmacao == "s":
            MercadoEstoque.estoque.pop(indice)
            print("Produto removido com sucesso!")

    def listar_produto(self):
        if not MercadoEstoque.estoque:
            print("Nenhum produto no estoque")
            return
        
        print("Os produtos no estoque são: ")
        for i, produto in enumerate(MercadoEstoque.estoque, 1):
            print(f"{i} - Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']}")

        if pergunta("Deseja atualizar algum item? (s/n): ") == "s":
            self.att_produto()

    def menu(self):
        while True:
            print("\n--- Menu Mercado ---")
            print("1 = Adicionar produto")
            print("2 = Remover produto")
            print("3 = Listar produtos")
            print("4 = Atualizar produto")
            print("5 = Sair")

            alternativa = validacao_de_input("Escolha a opção: ", int, "Opção inválida.")

            match alternativa:
                case 1:
                    self.add_produto()
                case 2:
                    self.remover_produto()
                case 3:
                    self.listar_produto()
                case 4:
                    self.att_produto()
                case 5:
                    print("Saindo do menu Mercado.")
                    return
                case _:
                    print("Opção inválida. Tente novamente.")

mercado = MercadoEstoque()