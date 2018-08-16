class Enemy2 {
  float x, y;
  boolean dir;
  Enemy2(float x, float y) { 
    this.x = x;
    this.y = y;
    this.dir = true;
  }
  
  void display() {
    
    fill(255,50,50);
    PShape e2 = createShape(GROUP);
    PShape body = createShape(RECT, x, y, 50, 50);
    fill(0);
    PShape spike1 = createShape(TRIANGLE, x, y+50, x+50, y+50, x+25, y+75);
    PShape spike2 = createShape(TRIANGLE, x, y, x+50, y, x+25, y-25);
    e2.addChild(body);
    e2.addChild(spike1);
    e2.addChild(spike2);
    
    shape(e2);
    
    if (this.dir == true) {
      this.y += 2;
      if (this.y >= 500) {
        this.dir = false;
      }
    } else {
      this.y -= 2;
      if (this.y <= 150) {
        this.dir = true;
      }
    }
  }
}