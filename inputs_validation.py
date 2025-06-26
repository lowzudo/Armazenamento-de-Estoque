import unicodedata

def validacao_de_input(prompt, data_type, error_message="Entrada inválida. Tente novamente."):
    while True:
        try:
            valor = data_type(input(prompt))
            if valor <= 0:
                raise ValueError("O valor não pode ser menor ou igual a zero.")
            return valor
        except ValueError:
            print(error_message)

def input_sem_acentos(prompt=""):
    texto = input(prompt)
    texto = texto.lower().strip()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto


def pergunta(prompt, error_message="Opção inválida. Tente novamente."):
    while True:
        resposta = input_sem_acentos(prompt)
        if resposta in ["s", "n"]:
            return resposta
        print(error_message)