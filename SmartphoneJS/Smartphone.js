export class Smartphone {
    nome;
    _modelo;
    _imei;
    _memoria

    constructor(nome, modelo, imei, memoria){
        this.nome = nome;
        this._modelo = modelo;
        this._imei = imei;
        this._memoria = memoria;
    }

    ligar(){
        return 'Ligando...' ;  
    }

    receberLigacao(){
        return 'Recebendo Ligação...';
    }

    instalarAplicativo(nomeApp){
        return `Instalando o aplicativo ${nomeApp}`;
    }
}

export class Iphone extends Smartphone{
    constructor(numero, modelo, imei, memoria){
        super(numero, modelo, imei, memoria)
    }

    instalarAplicativo(nomeApp){
    return `Baixando o aplicativo ${nomeApp}.`
   } 
}

export class Nokia extends Smartphone{
    constructor(numero, modelo, imei, memoria){
        super(numero, modelo, imei, memoria)
    }

    instalarAplicativo(nomeApp){
    return `Baixando o aplicativo ${nomeApp}.`
   } 
}