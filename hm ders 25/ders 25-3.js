document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    const fileInput = document.getElementById("file");
    if (fileInput.files.length > 0) {
        console.log(`Yüklenen dosya: ${fileInput.files[0].name}`); // Burada düzeltme yapıldı
    } else {
        console.log("Dosya yüklenemedi");
    }
});
