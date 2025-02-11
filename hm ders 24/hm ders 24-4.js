const result = document.getElementById("cookie-result");
document.getElementById("set-cookie").addEventListener("click", function() {
    document.cookie = 
    "username=HM; expires= Fri, 31 Dec 2024 12:00:00 UTC; path=/";
    result.innerText = "Bilgiler alındı: username=HM";
});
document.getElementById("show-cookie").addEventListener("click", function() {
    result.innerText= "Mevcut Kurban: " + document.cookie;
});
document.getElementById("delete-cookie").addEventListener("click", function() {
    document.cookie = "username=; expires=Thu, 01 jan 1970 00:00:00 UTC; path=/;";
    result.innerText="Çerez deletelendi.";
})