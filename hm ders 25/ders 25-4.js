document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const remember = document.getElementById("remember").checked;
    console.log(`Kullanıcı Adı: ${username} + Şifre: ${password}`);
    console.log(`Beni Hatırla: ${remember ? "Evet" : "Hayır"}`);
});
