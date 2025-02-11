function capitalizeFirst() {
    const inputString = document.getElementById('inputString').value
    if (inputString.length === 0) return

    const firstChar = inputString[0].toUpperCase()
    const lastChar = inputString [inputString.length -1].toUpperCase()
    const yeni = firstChar + inputString.slice(1, -1) + lastChar

    document.getElementById('result').textContent = yeni
}

function countVowles () {
    const inputString = document
    .getElementById("inputString")
    .value.toLowerCase();
    const Vowles = ["a","e","i","o", "u", "ü", "ö", "ı"];
    let count = 0;
    for (let char of inputString) {
        if (!Vowles.includes(char)) {
            count++;
        }
    }
    document.getElementById("result").textContent = `Number of vowels: ${count}`;
}