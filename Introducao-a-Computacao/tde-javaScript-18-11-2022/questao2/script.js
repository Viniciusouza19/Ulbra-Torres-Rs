let numberTable = prompt("Digite um numero para ver sua tabuada");
const resultado = document.querySelector(".resultado");
for (let i = 1; i <= 10; i++) {
  resultado.innerHTML += `${numberTable} x ${i} = ${numberTable * i} <br>`;
}
