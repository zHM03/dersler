const urlInfo = document.getElementById("url-info")
urlInfo.innerHTML = `
URL: ${location.href} <br>
Hostname: ${location.hostname} <br>
Pathname: ${location.protocol}
`;
document.getElementById("reload-btn").addEventListener("click", function() {
    location.reload();
    });
    document.getElementById("redirect-btn").addEventListener("click", function() {
        window.open("https://www.google.com", "_blank");
    })