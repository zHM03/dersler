let fieldCounter = 1;
document.getElementById("addField").addEventListener("click", function() {
  fieldCounter++;
  const newField = document.createElement("input");
  newField.type = "text";
  newField.name = `field${fieldCounter}`;
  newField.placeholder = `Alan ${fieldCounter}`;
  document.getElementById("dynamicForm").appendChild(newField);
  document
    .getElementById("dynamicForm")
    .appendChild(document.createElement("br"));
});
