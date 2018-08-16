class bird {
  float birdX, birdY, xvelocity, yvelocity, bottomValue, topValue;
  bird() {
    birdX = 120;
    birdY = 100;
    xvelocity = 0;
    yvelocity = 0;
    bottomValue = 600.0;
    topValue = 0.0;
  }
  
  void initialize() {
    birdX = 120;
    birdY = 400;
    xvelocity = 0;
    yvelocity = 0;
    alive = true;
    upflap = loadImage("upflap.png");
    downflap = loadImage("downflap.png");
  }
  
  void refresh() {
    if (birdY > 800) {
      alive = false;
    }
    if (alive == true) {
      birdX = birdX + xvelocity;
      birdY = birdY + yvelocity;
      
      if (yvelocity >= 0) {
        image(upflap, birdX, birdY);
      }
      if (yvelocity < 0) {
        image(downflap, birdX, birdY);
      }
    }
  }
  
  void jump() {
    if (keyPressed == true) {
      if ((keyCode == UP)) {
        xvelocity = 0;
        yvelocity = -3;
      }
      if ((keyCode == DOWN)) {
        xvelocity = 0;
        yvelocity = 3;
      }
      if ((keyCode == LEFT)) {
        yvelocity = 0;
        xvelocity = -3;
      }
      if ((keyCode == RIGHT)) {
        yvelocity = 0;
        xvelocity = 3;
      }
    }
  }
  
  void collisionCheck() {
    if ((birdY + 25 > bottomValue) || (birdY < topValue -25)) {
      alive = false;
    }
    if ((birdX > width + 25) || (birdX < -25)) {
      alive = false;
    }
  }
  
  void restartScreen() {
    background(255);
    textSize(50);
    fill(255, 0, 0);
    textAlign(CENTER);
    text("GAME OVER", 400, 75);
    fill(100);
    rect(275, 585, 250, 100);
    fill(0);
    text("Restart?", 400, 650);
    textSize(30);
    fill(0, 0, 255);
    text("Your score:", 120, 100);
    textSize(40);
    text(score/16, 120, 150);
    fill(0);
    input();
  }
  
  void winScreen() {
    background(255);
    textSize(50);
    fill(255, 0, 0);
    textAlign(CENTER);    
    text("YOU WON!", 400, 75);
    fill(100);
    rect(275, 585, 250, 100);
    fill(0);
    text("Restart?", 400, 650);
    textSize(30);
    fill(0, 0, 255);
    text("Your score:", 120, 100);
    textSize(40);
    text(score/16, 120, 150);
    fill(0);
    input();
  }
  
  void restart() {
    if ((alive == false) && (mousePressed)) {
      if ((mouseY > 585) && (mouseY < 685) && (mouseX > 275) && (mouseX < 525)) {
        music.stop();
        setup();
      }
    }
  }
}

  
    