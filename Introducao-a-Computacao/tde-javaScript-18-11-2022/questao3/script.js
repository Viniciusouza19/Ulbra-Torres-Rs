const resultado = document.querySelector(".resultado");
var phoneCadaster = {};
var clonePhoneCadaster = phoneCadaster;
var cont = 1;

const addFone = () => {
  let fones = prompt("Digite o número do telefone");
  if (fones == null || fones == "") {
    alert("Digite um número válido");
  } else {
    if (cont == 1) {
      if (cont) {
        phoneCadaster[`Fone - ${cont}`] = fones;
        cont += 1;
      }
    } else {
      for (key in phoneCadaster) {
        if (phoneCadaster[key] == fones) {
          alert("Número já cadastrado");
          return;
        }
      }

      phoneCadaster[`Fone - ${cont}`] = fones;
      cont += 1;
    }
    showFone();
  }
};
const showFone = () => {
  resultado.innerHTML = "";
  for (let fone in phoneCadaster) {
    resultado.innerHTML += `<p>${fone}: ${phoneCadaster[fone]}</p> `;
  }
};
const deleteFone = () => {
  let fones = prompt("Digite o número do telefone");
  if (fones == null || fones == "") {
    alert("Digite um número válido");
  } else {
    for (let fone in phoneCadaster) {
      if (phoneCadaster[fone] == fones) {
        delete phoneCadaster[fone];
        cont -= 1;
        alert(cont);
        showFone();
      }
    }
  }
};
document.querySelector(".btn").addEventListener("click", addFone);
document.querySelector(".btn2").addEventListener("click", () => {
  if (cont > 1) {
    deleteFone();
  } else {
    alert("Não há números para deletar");
  }
});
