const form = document.getElementById("userForm");
const agreeCheckbox = document.getElementById("agree");
const submitButton = form.querySelector('input[type="submit"]');
submitButton.disabled = true;
agreeCheckbox.addEventListener("change", function() {
    submitButton.disabled = !this.checked;
});
form.addEventListener("submit", function(event) {
    event.preventDefault();
    this.innerText=("Form başarıyla gönerildi");
});