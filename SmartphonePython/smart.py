class Smartphone():
    def __init__(self, nome, modelo, imei, memoria):
        self.nome = nome
        self.modelo = modelo
        self.imei = imei
        self.memoria = memoria

    def ligar(self):
        return 'Ligando...'

    def receber_ligacao(self):
        return 'Recebendo Ligação...'
    
    def instalar_aplicativo(self, nome_app):
        pass   
    
class Nokia(Smartphone):
    def __init__(self, nome, modelo, imei, memoria):
        super().__init__(nome, modelo, imei, memoria) 
      
    def instalar_aplicativo(self, nome_app):
        return 'Instalando o aplicativo {}'.format(nome_app)

class Iphone(Smartphone):
    def __init__(self, nome, modelo, imei, memoria):
        super().__init__(nome, modelo, imei, memoria)
    
    def instalar_aplicativo(self, nome_app):
        return 'Instalando o aplicativo {}'.format(nome_app)


nokia_phone = Nokia("Nokia", "N123", "123456", "16GB")
print(nokia_phone.imei)
print(nokia_phone.ligar())
print(nokia_phone.receber_ligacao())
print(nokia_phone.instalar_aplicativo("WhatsApp"))

iphone = Iphone("iPhone", "X", "789012", "64GB")
print(iphone.ligar())
print(iphone.receber_ligacao())
print(iphone.instalar_aplicativo("Instagram"))