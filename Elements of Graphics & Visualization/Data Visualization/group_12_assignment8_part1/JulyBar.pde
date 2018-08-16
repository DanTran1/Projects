//Objects for every July in the range 2000-2015
class JulyBar {
  float price;
  float year;
  float kwh;
  
  JulyBar(float year, float kwh, float price) {
    this.year = year;
    this.kwh = kwh;
    this.price = price;
  }
  
  void display() {
    strokeWeight(1);
    fill(200,0,0);
    rect(this.year, 450, this.year/40, 2*-price);
  }
}