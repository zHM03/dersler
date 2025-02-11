//görev 1
class Button {
  constructor(width, height, text) {
    this.width = width;
    this.height = height;
    this.text = text;
  }

  showBtn() {
    document.write(
      `<button style="width: ${this.width}; height: ${this.height};">${this
        .text}</button>`
    );
  }
}

class BootstrapButton extends Button {
  constructor(width, height, text, color) {
    super(width, height, text);
    this.color = color;
  }

  showBtn() {
    document.write(
      `<button style="width: ${this.width}; height: ${this
        .height}; background-color: ${this.color}; color: white;">${this
        .text}</button>`
    );
  }
}

function createButtons() {
  const btn1 = new Button("100px", "50px", "Standart Düğme");
  const btn2 = new BootstrapButton("100px", "50px", "Bootstrap Düğme", "blue");
  btn1.showBtn();
  btn2.showBtn();
}
//görev 2
class Shape {
  constructor(name) {
    this.name = name;
  }
  get getName() {
    return `Şekil: ${this.name}`;
  }
  area() {
    return 0;
  }
  perimeter() {
    return 0;
  }
}
class Square extends Shape {
  constructor(side) {
    super("Kare");
    this.side = side;
  }
  printInfo() {
    return `${super.getName} - Kenar: ${this.side}`;
  }
  area() {
    return this.side * this.side;
  }
  perimeter() {
    return this.side * 4;
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super("Diktdörtgen");
    this.width = width;
    this.height = height;
  }
  printInfo() {
    return `${super.printInfo()} - Genişlik: ${this.width}, Yükseklik: ${this
      .height}`;
  }
  area() {
    return this.width * this.height;
  }
  perimeter() {
    return 2 * (this.width + this.height);
  }
}
class Triangle extends Shape {
  constructor(a, b, c) {
    super("Üçgen");
    this.a = a;
    this.b = b;
    this.c = c;
  }
  printInfo() {
    return `${super.printInfo()} - Kenarlar: ${this.a}, ${this.b}, ${this.c},`;
  }
  area() {
    const s = (this.a + this.b + this.c) / 2;
    return Math.sqrt(s * (s - this.a) * (s - this.b) * (s - this.c));
  }
  perimeter() {
    return this.a + this.b + this.c;
  }
}
function createShapes() {
  const shapes = [new Square(4), new Rectangle(4, 5), new Triangle(3, 4, 5)];
  let output = "";
  shapes.forEach(shape => {
    output += `<div class="shape-info">${shape.printInfo()}<br>Alan:
        ${shape.area()}<br>Çevre: ${shape.perimeter()}</div>`;
  });
  document.getElementById("shapeOutPut").innerHTML = output;
}
