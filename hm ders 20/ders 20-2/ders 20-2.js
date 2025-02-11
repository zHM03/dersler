let fruits = [];

function createAndSortFruits() {
  fruits = [
    "elma",
    "armut",
    "muz",
    "çilek",
    "portakal",
    "kivi",
    "ananas",
    "nar"
  ];
  fruits.sort((a, b) => a.localeCompare(b));
  displayFruits();
}

function displayFruits() {
  const fruitListDiv = document.getElementById('fruitList');
  fruitListDiv.innerHTML = '<h2>Meyve Listesi:</h2>';
  const ul = document.createElement('ul');
  fruits.forEach(fruit => {
    const li = document.createElement('li');
    li.textContent = fruit;
    ul.appendChild(li);
  });
  fruitListDiv.appendChild(ul);
}

function searchFruit() {
  const searchValue = document
    .getElementById('searchFruit')
    .value.toLowerCase();
  const index = fruits.findIndex(fruit => fruit.toLowerCase() === searchValue); // Corrected this line
  const searchResultDiv = document.getElementById('searchResult');

  if (index !== -1) {
    searchResultDiv.innerText = `Meyve "${searchValue}" bulundu! Dizindeki indeksi: ${index}`;
  } else {
    searchResultDiv.innerText = `Meyve "${searchValue}" bulunamadı`;
  }
}
