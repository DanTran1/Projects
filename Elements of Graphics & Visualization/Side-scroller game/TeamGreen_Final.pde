import processing.sound.*;

pipe p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16;
ground g;
bird b = new bird();
Enemy1 e1;
Enemy2 e2;
EBird ebird;
SoundFile music;

PImage upflap, downflap;
PFont font;
float gui_x, gui_y;
int level;
ArrayList <pipe> allPipes;
int x = 850;
int d = 150;
int s = 2;  //speed pipes move
int count = 0;
int score = 0;
boolean alive = true;
boolean finished = false;
boolean musicOn = true;

// highscore variables
Table highscores;
String[] lines;
String initials = "";

void setup() {
  size(800, 800);
  count = 0;
  score = 0;
  
  // load scores
  highscores = loadTable("scores.csv", "header");
  lines = loadStrings("scores.csv");
  
  music = new SoundFile(this, "music.mp3");
  music.play();
  
  // creates 32 pipes
  allPipes = new ArrayList <pipe> ();
  for (int i = 0; i < 32; i++) {
    allPipes.add(new pipe(x + d*i));
  }
  g = new ground(0, 600);
  e1 = new Enemy1(random(2000, 6000), random(200,600), 10,10,10,10); //2000, 6000
  e2 = new Enemy2(400,400);
  ebird = new EBird(random(9000,10000), random(300,500), 40, 30, 200, 215); 
  b.initialize();
  font = createFont("Trebuchet MS Bold", 24);
  textFont(font);
  gui_x = 0.0;
  gui_y = 50.0;
  level = 1;
}

void draw() {
  background(35, 206, 235);
  g.display();
  
  // displays all pipes
  for (pipe p : allPipes) {
    p.display();
  }
  if (alive) {
    b.refresh();
    b.jump();
    e1.display();
    ebird.display();
    b.collisionCheck();
    collisionCheck();
    displayGUI();
    score += 1;
    strokeWeight(1);
    e2.display();
    
  } else {
    finished = true;
    b.restartScreen();
    b.restart();
    
  }
    // If past level 3, you win
    if (count > 95) {
      //alive = false;
      finished = true;
      b.winScreen();
      b.restart();
  }
    if (count == 32) {
      level = 2;
    }
    if (count == 64) {
      level = 3;
    }
}

void displayGUI() {
  noStroke();
  fill(0);
  textAlign(LEFT);
  textSize(20);
  rect(gui_x, gui_x, width, gui_y);
  fill(0, 255, 0);
  stroke(255);
  rect(gui_x + 315, gui_y - 38, 25, 25);
  if (!musicOn) {
    line(315, 12, 340, 37);
    line(340, 12, 315, 37);
  }
  
  noStroke();
  text("SOUND", gui_x + 360, gui_y - 17);
  text("'SHIFT' TO PAUSE", gui_x + 600, gui_y - 17);
  text("LEVEL: ", gui_x + 5, gui_y - 15);
  text("SCORE: ", gui_x + 140, gui_y - 15);
  text(level, gui_x + 75, gui_y - 15);
  text(score/16, gui_x + 220, gui_y - 15);
}

// pause game when SHIFT is pressed
void keyPressed() {
  if ((keyPressed == true && key == CODED)) {
    if (keyCode == SHIFT && !finished) {
      noLoop();
      fill(0); 
      text("~~ P A U S E D ~~", 400, 400);
    } 
  }
    if (!alive) {
      if (Character.isLetter(key) || Character.isDigit(key)) {
        if (initials.length() < 3) {
          initials += key;
        }
      }
      if (keyCode == ENTER || keyCode == RETURN) {
        String front = "";
        String end = "";
        String[] newLines;
        for (int i = 1; i < lines.length; i++) {
          int comma = lines[i].indexOf(",");
          int current = Integer.parseInt(lines[i].substring(comma + 1, lines[i].length()));
          String newRow = initials + "," + Integer.toString(score / 16) + "\n";
          if (score / 16 >= current) {
            for (int j = i; j < lines.length; j++) {
              end = end + lines[j] + "\n";
            }
            // Remember to add in the player, score columns we skipped by starting at i = 1;
            String newCSV = lines[0] + "\n" + front + newRow + end;
            newLines = newCSV.split("\n");
            saveStrings("scores.csv", newLines);
            break;
          }
          else {
            if (i == lines.length - 1) {
              front += lines[i] + "\n";
              String newCSV = lines[0] + "\n" + front + newRow;
              newLines = newCSV.split("\n");
              saveStrings("scores.csv", newLines);
            }
            else {
              front += lines[i] + "\n";
            }
          }
        }
        initials = "";
        highscores = loadTable("scores.csv", "header");
      }
      else if (keyCode == BACKSPACE && (initials.length() > 0)) {
        initials = initials.substring(0, initials.length() - 1);
      }
    }
  }
  
void input(){
  show_scores();
  textSize(30);
  textAlign(CENTER);
  text("Enter your initials:", 400, 125);
  fill(255);
  rect(350, 140, 100, 50);
  fill(0);
  text(initials, 400, 175);
}

void show_scores(){
  textAlign(CENTER);
  textSize(30);
  text("HIGHSCORES", 400, 250);
  int count = 0;
  float display = 300;
  for (TableRow row: highscores.rows()){
    if (count < 5){
      int highscore = row.getInt("score");
      String name = row.getString("name");
      text(name, 350, display);
      text(highscore, 450, display);
      display += 50;
      count += 1;
    }
  }
}

void mousePressed() {
    if (mouseX >= 315 && mouseX <= 340 && mouseY >= 12 && mouseY <= 37) {
      if (musicOn) {
        music.amp(0);
        musicOn = false;
      } else {
        music.amp(1);
        musicOn = true;
      }
    }
  }
    

// plays game when SHIFT is released
void keyReleased() {
  if (key == CODED  && keyCode == SHIFT) {
    loop();
  }
}

void collisionCheck() {
  if ((ebird.x < 800) && (ebird.x > 0)) {
    if ((b.birdX >= ebird.x-50) && (b.birdX <= ebird.x + 25) && ((b.birdY >= ebird.y - 40) && b.birdY < ebird.y + 30)) {
      alive = false;
    }
  }
  if ((e2.x < 800) && (e2.x > 0)) {
    if ((b.birdX >= e2.x-25) && (b.birdX <= e2.x + 50) && ((b.birdY >= e2.y - 25) && b.birdY < e2.y + 75)) {
      alive = false;
    }
  }
  if ((e1.x < 800) && (e1.x > 0)) {
    if ((b.birdX >= e1.x - 65) && (b.birdX <= e1.x + 65) && ((b.birdY >= e1.y - 65) && b.birdY < e1.y + 65)) {
      alive = false;
    }
  }
  if (((b.birdX >= allPipes.get(0).x - 32) && (b.birdX < allPipes.get(0).x + 32)) && (b.birdY < allPipes.get(0).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(1).x - 32) && (b.birdX < allPipes.get(1).x + 32)) && (b.birdY < allPipes.get(1).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(2).x - 32) && (b.birdX < allPipes.get(2).x + 32)) && (b.birdY < allPipes.get(2).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(3).x - 32) && (b.birdX < allPipes.get(3).x + 32)) && (b.birdY < allPipes.get(3).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(4).x - 32) && (b.birdX < allPipes.get(4).x + 32)) && (b.birdY < allPipes.get(4).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(5).x - 32) && (b.birdX < allPipes.get(5).x + 32)) && (b.birdY < allPipes.get(5).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(6).x - 32) && (b.birdX < allPipes.get(6).x + 32)) && (b.birdY < allPipes.get(6).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(7).x - 32) && (b.birdX < allPipes.get(7).x + 32)) && (b.birdY < allPipes.get(7).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(8).x - 32) && (b.birdX < allPipes.get(8).x + 32)) && (b.birdY < allPipes.get(8).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(9).x - 32) && (b.birdX < allPipes.get(9).x + 32)) && (b.birdY < allPipes.get(9).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(10).x - 32) && (b.birdX < allPipes.get(10).x + 32)) && (b.birdY < allPipes.get(10).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(11).x - 32) && (b.birdX < allPipes.get(11).x + 32)) && (b.birdY < allPipes.get(11).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(12).x - 32) && (b.birdX < allPipes.get(12).x + 32)) && (b.birdY < allPipes.get(12).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(13).x - 32) && (b.birdX < allPipes.get(13).x + 32)) && (b.birdY < allPipes.get(13).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(14).x - 32) && (b.birdX < allPipes.get(14).x + 32)) && (b.birdY < allPipes.get(14).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(15).x - 32) && (b.birdX < allPipes.get(15).x + 32)) && (b.birdY < allPipes.get(15).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(16).x - 32) && (b.birdX < allPipes.get(16).x + 32)) && (b.birdY < allPipes.get(16).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(17).x - 32) && (b.birdX < allPipes.get(17).x + 32)) && (b.birdY < allPipes.get(17).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(18).x - 32) && (b.birdX < allPipes.get(18).x + 32)) && (b.birdY < allPipes.get(18).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(19).x - 32) && (b.birdX < allPipes.get(19).x + 32)) && (b.birdY < allPipes.get(19).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(20).x - 32) && (b.birdX < allPipes.get(20).x + 32)) && (b.birdY < allPipes.get(20).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(21).x - 32) && (b.birdX < allPipes.get(21).x + 32)) && (b.birdY < allPipes.get(21).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(22).x - 32) && (b.birdX < allPipes.get(22).x + 32)) && (b.birdY < allPipes.get(22).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(23).x - 32) && (b.birdX < allPipes.get(23).x + 32)) && (b.birdY < allPipes.get(23).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(24).x - 32) && (b.birdX < allPipes.get(24).x + 32)) && (b.birdY < allPipes.get(24).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(25).x - 32) && (b.birdX < allPipes.get(25).x + 32)) && (b.birdY < allPipes.get(25).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(26).x - 32) && (b.birdX < allPipes.get(26).x + 32)) && (b.birdY < allPipes.get(26).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(27).x - 32) && (b.birdX < allPipes.get(27).x + 32)) && (b.birdY < allPipes.get(27).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(28).x - 32) && (b.birdX < allPipes.get(28).x + 32)) && (b.birdY < allPipes.get(28).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(29).x - 32) && (b.birdX < allPipes.get(29).x + 32)) && (b.birdY < allPipes.get(29).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(30).x - 32) && (b.birdX < allPipes.get(30).x + 32)) && (b.birdY < allPipes.get(30).y + 50)) {
    alive = false;
  }
  if (((b.birdX >= allPipes.get(31).x - 32) && (b.birdX < allPipes.get(31).x + 32)) && (b.birdY < allPipes.get(31).y + 50)) {
    alive = false;
  }
  
}