let numberOne = prompt("Digite o primeiro número");
let numberTwo = prompt("Digite o segundo número");
let operation = prompt("Digite a operação desejada");

let result = 0;

switch (operation) {
  case "+":
    result = Number(numberOne) + Number(numberTwo);
    break;
  case "-":
    result = Number(numberOne) - Number(numberTwo);
    break;
  case "*":
    result = Number(numberOne) * Number(numberTwo);
    break;
  case "/":
    result = Number(numberOne) / Number(numberTwo);
    break;
  default:
    result = "Operação inválida";
    break;
}

alert("O resuldado da operação é: " + result);
