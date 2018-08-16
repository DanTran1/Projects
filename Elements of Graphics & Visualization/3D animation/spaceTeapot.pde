PShape spaceTeapot;
PShape droplet;
class spaceTeapot {

  float a, b, xval, yval;
  boolean dir;

  spaceTeapot(float a, float b, float xval, float yval, boolean dir) {
    this.a = a;
    this.b = b;
    this.xval = xval;
    this.yval = yval;
    this.dir = dir;
  }

  void display() {
    spaceTeapot = loadShape("teapot.obj");
    spaceTeapot.setFill(color(#D8944F));
    spaceTeapot.scale(75, 100, 75);
    translate(width/xval, height/yval, 0);

    droplet = createShape(SPHERE, 15);
    droplet.setFill(color(0, 0, 200));

    rotateZ(PI);
    rotateY(a);
    rotateX(b);

    b += .005;
    a += .01;
  }

  void move() {

    shape(spaceTeapot);
    translate(0, 0, 100);
    shape(droplet);

    if (dir == true) {
      xval += .01;
      yval += .01;
      if (xval >= 4) {
        dir = false;
      }
    } else {
      xval -= .01;
      yval -= .01;
      if (xval <= 1.5) {
        dir = true;
      }
    }
  }
}