const sizeInfo = document.getElementById("size-info");
const scrolllInfo = document.getElementById("scoll-info");
window.addEventListener("resize", function() {
    sizeInfo.innerText = `Pencere Boyutu: ${window.innerWidth}x${window.innerHeight}`;
});
window.addEventListener("scroll", function () {
    scrolllInfo.innerText = `Sayfa ${window.scrolly}px kadar kaydırıldı`;
});