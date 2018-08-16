class Porsche {
  int age, price, mileage;
  
  Porsche (int age, int price, int mileage) {
    this.age = age;
    this.price = price;
    this.mileage = mileage;
  }
 
 void display() {
   stroke(255);
   float aprice = constrain(price/500, 50, 100);
   float aage = constrain(age*20, 25,255);
   float amileage = constrain(mileage/500, 50, 100);
   fill(aage, 50, 50);
   ellipse(x,y,aprice, amileage);
   fill(255);
   text(age, x-10,y+5);
   
   x = x + 100;
   if (x + 85 > width) {
     x = 100;
     y = y + 100;
   }
 }
}