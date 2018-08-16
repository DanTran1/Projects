class EBird {
  float x, y, wide, tall, tflap, bflap;
  boolean dir = true;
  
  EBird(float x, float y, float wide, float tall, float tflap, float bflap) {
    this.x = x;
    this.y = y;
    this.wide = wide;
    this.tall = tall;
    this.tflap = tflap;
    this.bflap = bflap;
  }
  
  void display() {
    
    fill(200,0,25);
    PShape ebird = createShape(GROUP);
    PShape bwing = createShape(LINE, x, y + 7, x + 40, bflap);
    PShape twing = createShape(LINE, x, y - 7, x + 40, tflap);
    PShape body = createShape(ELLIPSE, x, y, wide + 30, tall);
    PShape head = createShape(ELLIPSE, x - 20, y - 10, wide, tall);
    PShape beak = createShape(TRIANGLE, x - 33, y - 5, x - 40, y - 10, x - 30, y - 13);
    PShape eye = createShape(ELLIPSE, x - 20, y - 15, wide/5, tall/5);
    
    ebird.addChild(body);
    ebird.addChild(head);
    ebird.addChild(twing);
    ebird.addChild(bwing);
    ebird.addChild(beak);
    ebird.addChild(eye);
    shape(ebird);
    
    strokeWeight(3);
    
    x -= 3;
    y += sin(x/16);
    
    if (x <= 0) {
      x = 4000;
    }
    
    if (dir == true) {
      tflap -= 1;
      bflap -= 1;
      if (tflap <= y - 35) {
        dir = false;
      }
    } else {
      tflap += 1;
      bflap += 1;
      if (tflap >= y + 15) {
        dir = true;
      }
    }
  }
}