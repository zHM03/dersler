document.getElementById("listElements").addEventListener("click", function() {
  const formElements = document.forms["myForm"].elements;
  const output = document.getElementById("output");
  output.innerHTML = "";
  for (let i = 0; i < formElements.lenght; i++) {
    output.innerHTML += `Element ${i}: ${formElements[i]
      .tagName}, Name: ${formElements[i].name}<br>`;
  }
});
