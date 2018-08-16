class Cat {
  PShape cat;
  float rotation;
  float x, y, z;

  Cat(float x, float y, float z) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.rotation = 0;
    this.cat = loadShape("cat.obj");
    this.cat.scale(4);
  }

  void display() {

    pushMatrix();
    translate(this.x + 200, this.y + 200, this.z);
    rotateZ(PI);
    shape(this.cat, 0, 0, this.cat.width, this.cat.height);
    popMatrix();
    displaySphere();
  }

  void displaySphere() {
    pushMatrix();
    translate(this.x + 200, this.y + 140, this.z);
    rotateY(this.rotation);
    pointLight(250, 250, 250, 305, 150, 0);
    fill(200, 0, 0, 70);
    this.rotation += .01;
    noStroke();
    sphere(40);
    popMatrix();
  }

  void move() {
    this.x += 1;
    this.z -= 1;

    if (this.x > 700) {
      this.x = 100;
    }
    if (this.z < -700) {
      this.z = 100;
    }
  }
}