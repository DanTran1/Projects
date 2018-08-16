class Enemy1 {
  float x, y;
  int counter;
  int spike1X, spike2X, spike3Y, spike4Y;
  int spike1Xchange = 1; 
  int spike2Xchange = 1;
  int spike3Ychange = 1;
  int spike4Ychange = 1;
  Enemy1(float x, float y, int spike1X, int spike2X, int spike3Y, int spike4Y) { 
    this.x = x;
    this.y = y;
    this.spike1X = spike1X;
    this.spike2X = spike2X;
    this.spike3Y = spike3Y;
    this.spike4Y = spike4Y;
  }

  void display() {

    fill(255, 0, 0);
    PShape e1 = createShape(GROUP);
    PShape body = createShape(ELLIPSE, x, y, 50, 50);
    fill(0);
    PShape spike1 = createShape(TRIANGLE, x+25, y-10, x+25, y+10, x+45+spike1X, y);
    PShape spike2 = createShape(TRIANGLE, x-25, y-10, x-25, y+10, x-45-spike2X, y);
    PShape spike3 = createShape(TRIANGLE, x+10, y+25, x-10, y+25, x, y+45+spike3Y);
    PShape spike4 = createShape(TRIANGLE, x-10, y-25, x+10, y-25, x, y-45-spike4Y);
    e1.addChild(body);
    e1.addChild(spike1);
    e1.addChild(spike2);
    e1.addChild(spike3);
    e1.addChild(spike4);

    shape(e1);
    this.x -= 3;
    counter += 1;
    spike1X += spike1Xchange;
    spike2X += spike2Xchange;
    spike3Y += spike3Ychange;
    spike4Y += spike4Ychange;
    
    if (this.x <= 0) {
      x = 4000;
    }
    
    if (counter % 10 == 0) {
      this.spike1Xchange = -1 * this.spike1Xchange;
      this.spike2Xchange = -1 * this.spike2Xchange;
      this.spike3Ychange = -1 * this.spike3Ychange;
      this.spike4Ychange = -1 * this.spike4Ychange;
    }
  }
}