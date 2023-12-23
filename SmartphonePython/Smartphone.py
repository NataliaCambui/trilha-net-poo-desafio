
class Smartphone():
    def __init__(self, nome, modelo, imei, memoria):
        self.nome = nome
        self.modelo = modelo
        self.imei = imei
        self.memoria = memoria

    def ligar(self):
        return 'Lingado...'

    def receber_ligacao(self):
        return 'Recebendo Ligação...'
    
    def instalar_aplicativo(nome_app):
        pass   

       
class Nokia(Smartphone):
    def __init__(self, nome, modelo, imei, memoria):
        super().__init__(nome, modelo, imei, memoria)
        self.nome_app = ""

    def ligar():
        return 'Lingado...'

    def receber_ligacao():
        return 'Recebendo Ligação...'  
      
    def instalar_aplicativo(nome_app):
        return 'Instalando o aplicativo {}'.format(nome_app)


class Iphone(Smartphone):
    def __init__(self, nome, modelo, imei, memoria):
        super().__init__(nome, modelo, imei, memoria)
        self.nome_app = ""

    def ligar():
        return 'Lingado...'

    def receber_ligacao():
        return 'Recebendo Ligação...' 
    
    def instalar_aplicativo(nome_app):
        return 'Instalando o aplicativo {}'.format(nome_app)

# Esses são os exemplos de testes para colocar no terminal do python

# nokia = Nokia(nome="Nokia 3310", modelo="Antigo", imei="123456789", memoria="2GB")
# Nokia.ligar()
# Nokia.receber_ligacao()
# Nokia.instalar_aplicativo("Whatsapp")

# iphone = Iphone(nome="iPhone X", modelo="Novo", imei="987654321", memoria="64GB")
# Iphone.ligar()
# Iphone.receber_ligacao()
# Iphone.instalar_aplicativo("Telegram")
