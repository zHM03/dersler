document.querySelector("form").addEventListener("submit", function(event){
    event.preventDefault();
    const feedback = document.getElementById("feedback").value;
    console.log(`Geri Bildirim: ${feedback}`);
})