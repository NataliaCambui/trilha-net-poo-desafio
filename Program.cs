using System.ComponentModel;
using DesafioPOO.Models;

// TODO: Realizar os testes com as classes Nokia e Iphone
Console.WriteLine("Smartphone Nokia");
Smartphone Nokia = new Nokia(numero:"9999999", modelo:"Modelo1", imei:"11111111", memoria: "64");
Nokia.Ligar();
Nokia.ReceberLigacao();
Nokia.InstalarAplicativo("Whatsapp");

Console.WriteLine("Smartphone Iphone");
Smartphone Iphone = new Iphone(numero: "888888880", modelo:"Modelo2", imei: "22222222", memoria: "128");
Iphone.Ligar();
Iphone.ReceberLigacao();
Iphone.InstalarAplicativo("Telegram");