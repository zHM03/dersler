const resultText = document.getElementById("result");
document.getElementById("alert-btn").addEventListener("click", function(){
    alert("Bu bir uyarı mesajı");
});
document.getElementById("prompt-btn").addEventListener("click", function () {
    const name = prompt("Adınızı Girin:");
    if (name) {
        resultText.innerHTML = "Sonuç: Merhaba, " + name + "!";
    } else {
        resultText.innerHTML = "Sonuç: Bir isim girmediniz.";
    }
});
document.getElementById("confirm-btn").addEventListener("click", function() {
    const isConfirmed = confirm("Emin misiniz?");
    if (isConfirmed) {
        resultText.innerHTML = "Sonuç: Evet'e bastınız";
    } else {
        resultText.innerHTML = "Sonuç: Hayıra bastınız";
    }
});