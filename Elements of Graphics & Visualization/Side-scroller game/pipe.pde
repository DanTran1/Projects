class pipe {
  
  int x, y, startPos;
  int speed = 2;
  
  pipe(int x) {   
    this.startPos = x;
    this.x = x;
    this.y = int(random(50, 425));
  }
  
  void display() {
    fill(0,255,0);
    stroke(0);
    PShape pipe = createShape(GROUP);
    PShape tube = createShape(RECT, this.x, 0, 70, this.y);
    PShape lip = createShape(RECT, this.x - 15, this.y,  100, 50);
    pipe.addChild(tube);
    pipe.addChild(lip);
    shape(pipe);
    move();
  }
  
  void move() {
    this.x -= speed;
    if (this.startPos - 4800 >= this.x) {
      this.x = this.startPos;
      // ups the speed after every pipe has
      // displayed
      count += 1;
      speed *= 1.5;
      this.y = int(random(50, 425));
    }
  }
    
}