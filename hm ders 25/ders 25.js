document.querySelector("form").addEventListener("submit", function(event){
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const age = document.getElementById("age").valye;
    const password = document.getElementById("password").value;
    console.log(`Ad:${name}, E-posta:${email}, Yaş:${age}, Şifre${password}`);
    alert("Form başarıyla Gönderildi")
})