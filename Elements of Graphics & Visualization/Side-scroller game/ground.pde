class ground {
  
  int x,y;
  
  ground(int x, int y) {
    this.x = x;
    this.y = y;
  }
  
  void display() {
    fill(139,69,19);
    rect(this.x, this.y, 800, 800);
  }
}