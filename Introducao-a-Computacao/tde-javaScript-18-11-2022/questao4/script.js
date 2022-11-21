let binario = [];

let binEnter = prompt("Digite um número binário: ");

for (let i = 0; i < binEnter.length; i++) {
  binario.push(binEnter[i]);
}

let decimal = 0;

for (let i = 0; i < binario.length; i++) {
  if (binario[i] == 1) {
    decimal += Math.pow(2, i);
  }
}

alert("O número binário " + binEnter + " em decimal é: " + decimal);
