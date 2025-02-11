let array1 = [];
let array2 = [];

function generateArrays() {
array1 = Array.from({ length: 5}, () => Math.floor(Math.random() * 100));
array2 = Array.from({ length: 5}, () => Math.floor(Math.random() * 100));
document.getElementById('output').innerText = `Diziler Oluşturuldu:\nDizi1:
[${array1.join(', ')}]\nDizi2: [${array2.join(', ')}]`;
}

function mergeArrays() {
    const merged = [...new Set([...array1, ...array2])];
    document.getElementById('output').innerText = `Birleştirilmiş Dizi:
    [${merged.join(', ')}]`;
}

function commonElements() {
const common = array1.filter(value => array2.includes(value));
document.getElementById('output').innerText = `Ortak Öğeler: [${common.join(', ')}]`;
}

function uniqueToFirstArray () {
const unique = array1.filter(value => !array2.includes(value));
document.getElementById('output').innerText = `İkinci Dizi Olmayanlar:
[${unique.join(', ')}]`;
}