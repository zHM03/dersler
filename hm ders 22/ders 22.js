//1. görev

class FontStyle {
  constructor(size, color, family) {
    this.size = size;
    this.color = color;
    this.family = family;
  }
  print(text) {
    return `<span style="font-size: ${this.size}; color:${this.color};
        font-family: ${this.family};">${text}</span>`;
  }
}

function showText() {
  const font = new FontStyle("20px", "blue", "Arial");
  document.getElementById("textOutput").innerHTML = font.print(
    "Merhaba, bu yazı görev 1'in çıktısıdır."
  );
}
//2.görev tekrarla hiçbir şey anlamadım
class News {
    constructor(title, content, tags, publishDate) {
      this.title = title;
      this.content = content;
      this.tags = tags;
      this.publishDate = new Date(publishDate); 
    }
  
    print() {
      let dateOutput;
      const now = new Date();
      const diffTime = Math.abs(now - this.publishDate);
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
      
      if (diffDays < 1) {
        dateOutput = "bugün";
      } else if (diffDays < 7) {
        dateOutput = `${diffDays} gün önce`;
      } else {
        dateOutput = this.publishDate.toLocaleDateString("tr-TR");
      }
      
      return `<div class="news"><h3>${this.title}</h3><p>${this.content}</p><p>Etiketler: ${this.tags.join(", ")}</p><p>Yayın Tarihi: ${dateOutput}</p></div>`;
    }
  }
  
  function showNews() {
    const newsItem = new News(
      "JavaScript Öğreniyorum",
      "JavaScript ile programlamaya adım atıyorum.",
      ["JavaScript", "Programlama"],
      "2024-10-11"
    );
  
    document.getElementById("newsOutput").innerHTML = newsItem.print();
  }