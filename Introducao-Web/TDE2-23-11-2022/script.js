const btn = document.querySelector(".btn");
const kwhValue = document.querySelector("#kwh");
const input = document.querySelector("#input");
const valorKwh = document.querySelector("#valorKwh");
const total = document.querySelector("#total");
let date = new Date();
var inputActionOne = false;
var kwh = 0;

const calc = () => {
  if (inputActionOne == false) {
    kwh = input.value;
    kwhValue.innerText = kwh + " kWh";
    input.value = "";
    input.setAttribute("placeholder", "Digite o valor do kWh");
    inputActionOne = true;
  } else {
    if (kwh > 100 && kwh < 200) {
      total.innerText =
        "R$ " +
        (kwh * input.value + kwh * input.value * 0.25)
          .toFixed(2)
          .replace(".", ",");
    } else if (kwh > 200) {
      alert(kwh);
      total.innerText =
        "R$ " +
        (kwh * input.value + kwh * input.value * 0.5)
          .toFixed()
          .padStart(2, "0");
    } else {
      total.innerText = "R$ " + (kwh * input.value).toFixed().padStart(2, "0");
    }
    valorKwh.innerText = "R$ " + input.value;
    input.value = "";
    input.setAttribute("placeholder", "Digite o consumo em kWh");
    inputActionOne = false;
  }
};

btn.addEventListener("click", calc);
input.addEventListener("keypress", (e) => {
  if (e.which == 13) {
    calc();
  }
});

document.querySelector("#date span").innerText = date.toLocaleDateString();
