let num1Input = document.getElementById("num1");
let num2Input = document.getElementById("num2");
let resultInput = document.getElementById("result");

function insert(number) {
  if (document.activeElement === num1Input || document.activeElement === num2Input) {
    document.activeElement.value += number;
  }
}

function calculate(op) {
  let n1 = parseFloat(num1Input.value);
  let n2 = parseFloat(num2Input.value);
  let result = "";

  if (isNaN(n1) || isNaN(n2)) {
    result = "Enter valid numbers";
  } else {
    switch(op) {
      case "+": result = n1 + n2; break;
      case "-": result = n1 - n2; break;
      case "*": result = n1 * n2; break;
      case "/": result = n2 !== 0 ? (n1 / n2).toFixed(2) : "Cannot divide by 0"; break;
    }
  }

  resultInput.value = result;
}
