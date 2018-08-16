class Dog {
  PShape dog;
  float x, y, z, wide, tall, deep;
  color c;
  PVector speed;
  float a;
  float i = 200;
  float j = 4;
  float tongue_length = 0.6;
  float tongue_change = 0.01;

  Dog(float x, float y, float z) {
    this.x = x;
    this.y = y;
    this.z = z;
    //this.wide = wide;
    //this.tall = tall;
    //this.c = c;
    //this.speed = speed;
    this.dog = loadShape("dog.obj");
  }

  void display() {
    ambientLight(120,120,120,400,400,0);
    translate(i, 300, 0);
    i += 1;
    if (i > width + 200) {
      i = 200;
    }
    scale(30, 30, 30);
    rotateZ(PI);
    a += 0.01;
    shape(dog);
    translate(-.75, 6.75);
    fill(255, 20, 147);
    //box(tongue_length, 0.15, 0.6);
    tongue_length += tongue_change;
    if (tongue_length > 1.2) {
      tongue_change = -tongue_change;
    }
    if (tongue_length < 0.6) {
      tongue_change = -tongue_change;
    }
    fill(255, 204, 0);
    noStroke();
    translate(5.75, j-6.75);
    j -= .01;
    if (j < 1) {
      j = 4;
    }
    box(0.3, 0.6, 0.2);
  }
}