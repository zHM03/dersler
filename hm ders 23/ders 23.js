//görev2
document.getElementById('browserName').textContent = navigator.appName;
document.getElementById('browserVersion').textContent = navigator.appVersion;
document.getElementById('browserLanguage').textContent = navigator.language;
document.getElementById('onlineStatus').textContent = navigator.online ? "çevrim içi": "çevrim dışı";
// görev 3
document.getElementById('screenWidth').textContent = screen.width;
document.getElementById('screenHeight').textContent = screen.height;
document.getElementById('colorDepth').textContent = screen.colorDepth + "bit";
//görev 4
document.getElementById("currentUrl").textContent = location.href;
function goToGoogle() {
    location.assign("https://www.google.com");
}
function goBack() {
    history.back();
}
function goForward() {
    history.forward();
}
//görev 5
function loadInFrame(){
    window.frames[0].location.href = "https://www.geekforgeeks.org";
}
function loadInFrame(){
    window.frames[1].location.href = "https://www.python.org";
}
//görev 6
 let newWindow;
 function openWindow(){
    newWindow = window.open(
        "https://itstep.org","YeniPencere","width=800,height=800"
    );
 }
 function closeWindow() {
    if (newWindow) {
        newWindow.close();
    }
 }
 //görev 7
 const languages = navigator.languages;
 const preferredLanguage = navigator.language;
 const languageList = document.getElementById("languageList");
 
 languages.forEach(lang => {
     const listItem = document.createElement("li");
     if (lang === preferredLanguage) {
         listItem.classList.add("bold");
     }
     listItem.textContent = lang;
     languageList.appendChild(listItem);
 });
//görev 8
function showHistoryLenght(){
    document.getElementById("historyCount").textContent = history.length;
} 