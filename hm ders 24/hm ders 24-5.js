const result = document.getElementById("result");
document.getElementById("set-local").addEventListener("click", function (){
    localStorage.setItem("name", "HM");
    result.innerText = "Local Storage: 'name' değeri eklendi";
});
document.getElementById("get-local").addEventListener("click", function (){
    const name = localStorage.getItem("name");
    result.innerText = "local Storage'tan alınan veri" + name ;
}),
document.getElementById("clear-local").addEventListener("click", function() {
    localStorage.clear();
    result.innerText = "Local Storage Temizlendi.";
});
document.getElementById("set-session").addEventListener("click", function(){
    sessionStorage.setItem("sessionName", "HMSession");
    result.innerText = "Session Storage: 'sessionName' değeri eklendi";
});
document.getElementById("get-session").addEventListener("click", function(){
    const sessionName = sessionStorage.getItem("sessionName");
    result.innerText = "Session Storage'tan alınan veri:" + sessionName;
});
document.getElementById("clear-session").addEventListener("click",function(){
    sessionStorage.clear();
    result.innerText = "Session Storage temizlendi"
});