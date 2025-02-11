let randomArray =[];

function generateRandomArray() {
    randomArray = Array.from ({length: 10 }, () => Math.floor(Math.random()* 100));
    document.getElementById('output').innerText = `Dizi oluşturuldu: [${randomArray.join(', ')}]`;
}

function printArray() {
    document.getElementById('output').innerText = `Dizi: [${randomArray.join(', ')}]`;
}

function printEvenNumbers() {
    const evenNumbers = randomArray.filter(num => num % 2 === 0);
    document.getElementById('output').innerText = `Çift sayılar: [${evenNumbers.join(',')}]`;
}

function sumOfArray() {
    const sum = randomArray.reduce((acc, num) => acc + num, 0);
    document.getElementById('output').innerText = `Dizinin toplamı: ${sum}`;
}

function maxOfArray(){
    const max = Math.max(...randomArray);
    document.getElementById('output').innerText = `dizinin maksimum elemanı: ${max}`;
}

function addNumber() {
    const newNumber = parseInt(document.getElementById('newNumber').value);
    if(!isNaN(newNumber)) {
        randomArray.push(newNumber);
        document.getElementById('output').innerText = `yeni dizi: [${randomArray.join(', ')}]`;
        document.getElementById('newNumber').value = '';
    } else {
        alert('lütfen geçerli bir sayı girin');
    }
}

function removeNumber() {
    const removeNumber = parseInt(document.getElementById('removeNumber').value);
    const index = randomArray.indexOf(removeNumber);
    if (index > -1) {
        randomArray.splice(index, 1);
        document.getElementById('output').innerText = `yeni dizi: [${randomArray.join(', ')}]`;
        document.getElementById('removeNumber').value = '';
    } else {
        alert('Dizide böyle bir sayı yok');
    }
}