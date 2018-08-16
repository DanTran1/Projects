PFont georgia;
ArrayList<Porsche> fleet;
int x = 100;
int y = 50;
int pNum = 0;

void setup() {
  
  size(800,600);
  Table data = loadTable("Porsche.csv", "header");
  background(0);
  georgia = createFont("Georgia", 24);
  textFont(georgia);
  
  fleet = new ArrayList<Porsche>(); 
  
  for (int i = 1; i<data.getRowCount(); i++) {
    TableRow row = data.getRow(i);
    int age = row.getInt("Age");
    int price = row.getInt("Price");
    int mileage = row.getInt("Mileage");
    fleet.add(new Porsche(age, price, mileage));
  }

  for (int i = 0; i <fleet.size(); i++ ) {
    Porsche f = fleet.get(i);
    f.display();
  } 
  textSize(16);
  text("P O R S C H E S", 200, 425);
  text("Number in Circle: Age. The darker the red, the older the car!", 200, 445);
  text("Width: Price", 200, 460);
  text("Height: Mileage", 200, 475);
}

void draw() { //Cycles through the prices of all the Porsches
  if (mousePressed == true) {
    fill(0);
    rect(100,510, 300, 35);
    fill(200,0,0);
    Porsche p = fleet.get(pNum);
    text("Price for Porsche number " + pNum + ":" , 110, 530);
    text(p.price, 325, 530);
    pNum++;

    if (pNum >= 29) {
      pNum = 0;
    }
  }
}