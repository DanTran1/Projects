PImage starfield;
Cat Cat1;
Dog Dog1;
spaceTeapot tp;

void setup() {

  size(800, 800, P3D);
  noStroke();
  starfield = loadImage("starfield.jpg");
  tp = new spaceTeapot(0.0, 0.0, 2.0, 2.0, true);
  Cat1 = new Cat(100, 100, 0);
  Dog1 = new Dog(0, 0, 0);
}

void draw() {
  background(0);
  hint(DISABLE_DEPTH_MASK);
  image(starfield, 0, 0, width, height);
  hint(ENABLE_DEPTH_MASK);
  tp.display();
  tp.move();
  Cat1.display();
  Cat1.move();
  Dog1.display();
}