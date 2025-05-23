let rad;
const PI = 3.14;
let cir;
document.getElementById("mysubmit").onclick = function () {
  rad = document.getElementById("mytext").value;
  rad = Number(rad);
  cir = 2 * PI * rad;
  document.getElementById("h1").textContent = cir + "cm";
};
