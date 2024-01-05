import{ Smartphone, Iphone, Nokia } from './Smartphone.js';

const nokia = new Smartphone( "Nokia", 'Nokia 3310', 123456789, '256GB');

console.log(nokia);
console.log(nokia.ligar());
console.log(nokia.receberLigacao());
console.log(nokia.instalarAplicativo("Whatsapp"));

const iphone = new Smartphone( 'Iphone', "Iphone13", 22222222, "12GB8");

console.log('-------------------------------')

console.log(iphone)
console.log(iphone.ligar());
console.log(iphone.receberLigacao())
console.log(iphone.instalarAplicativo("Telegram"))