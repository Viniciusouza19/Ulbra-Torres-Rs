document.querySelector("#maiorIdade").style.display = "none";
document.querySelector(".maiorNumeroDeVarios").style.display = "block";
const entry = document.querySelector("#input");
const respMaiorNumero = document.querySelector("#respMaiorNumero");
const respMenorIdade = document.querySelector("#respMenorIdade");
const respMaiorIdade = document.querySelector("#respMaiorIdade");
const opc1 = document.querySelector(".opc1");
const opc2 = document.querySelector(".opc2");
const btn2 = document.querySelector("#btn2");

const debounce = (func, wait) => {
  let timeout;

  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };

    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};
var returnedFunction = debounce(function () {
  if (opc1.hasAttribute("selected")) {
    selectedOpc1(entry.value);
  }
}, 300);

entry.addEventListener("keyup", returnedFunction);

document.querySelector("#select").addEventListener("change", function () {
  opc1.hasAttribute("selected")
    ? opc1.removeAttribute("selected")
    : opc1.setAttribute("selected", "");
  opc2.hasAttribute("selected")
    ? opc2.removeAttribute("selected")
    : opc2.setAttribute("selected", "");

  if (opc1.hasAttribute("selected")) {
    entry.value = "";
    document.querySelector("#maiorIdade").style.display = "none";
    btn2.style.display = "none";
    document.querySelector(".maiorNumeroDeVarios").style.display = "block";
  } else {
    document.querySelector("#maiorIdade").style.display = "block";
    btn2.style.display = "block";
    entry.value = "";
    document.querySelector(".maiorNumeroDeVarios").style.display = "none";
  }
});

document.querySelector("#btn").addEventListener("click", () => {
  entry.value = "";
  if (opc1.hasAttribute("selected")) {
    respMaiorNumero.innerHTML = "0";
  }
  if (opc2.hasAttribute("selected")) {
    respMaiorIdade.innerHTML = "0";
    respMenorIdade.innerHTML = "0";
    maiorIdade = [];
    menorIdade = [];
  }
});

function selectedOpc1(arr) {
  const inputArray = arr.includes(".")
    ? (arr = arr.split("."))
    : (arr = arr.split(","));
  const maiorNumero = Math.max(...inputArray);
  if (typeof maiorNumero === "number") {
    respMaiorNumero.innerHTML = maiorNumero;
  }
  if (isNaN(maiorNumero)) {
    respMaiorNumero.innerHTML = "Invalido";
  }
}

btn2.addEventListener("click", () => {
  menorIdade = [];
  maiorIdade = [];
  const inputArray = entry.value.split(",");
  inputArray.forEach((element) => {
    if (element < 18) {
      menorIdade.push(element);
    } else {
      maiorIdade.push(element);
    }
  });
  respMaiorIdade.innerHTML = maiorIdade.length;
  respMenorIdade.innerHTML = menorIdade.length;
});
// 25,36,15,25,66,45
