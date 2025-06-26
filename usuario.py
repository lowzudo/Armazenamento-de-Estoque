def validar_senha_forte(senha):
    maiuscula = any(c.isupper() for c in senha)  
    minuscula = any(c.islower() for c in senha)  
    numero = any(c.isdigit() for c in senha)     
    tamanho = len(senha) >= 8     

    return maiuscula and minuscula and numero and tamanho                

class UserValidation:
    userlist = []
    def _init_(self):
        self.usuario = None
        self.senha = None
        self.userlist = []

    def criar_usuario(self):
        self.usuario = input("Insira seu usuário (Requisitos: 5 caracteres ou mais): ").lower()
        while len(self.usuario) < 5:
            self.usuario = input("Usuário inválido, Re-insira: ")
        return self

    def criar_senha(self):
        print("A senha deve conter: Letra maiúscula e minúscula, 8+ caracteres, letras e números")
        print("")
        self.senha = input("Digite sua senha: ")

        while not validar_senha_forte(self.senha):
            print("")
            print("❌ Senha inválida: deve conter pelo menos 8 caracteres, uma letra maiúscula, uma minúscula e um número")
            self.senha = input("\nDigite sua senha novamente: ")
        
        confirmacao = input("Confirme sua senha: ")

        while confirmacao != self.senha:
            print("As senhas não coincidem!")
            confirmacao = input("Confirme sua senha: ")
        return self

    def criar_conta(self):
        self.criar_usuario()
        self.criar_senha()
        self.userlist.append(self.usuario)
        print("")
        print(f"✅ Conta criada com sucesso {self.usuario} !")
        print("")
        return self

