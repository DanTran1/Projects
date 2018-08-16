PFont verdana;
float yearx = 80.0;
int year2 = 2000;
int bill = 0;
int yearClicker = 0;
ArrayList<JulyBar> julybars;


void setup() {
  Table data = loadTable("AverageKWHBills.csv", "header");
  size(800, 500);
  background(0);
  verdana = createFont("Verdana", 12);
  textFont(verdana);

  julybars = new ArrayList<JulyBar>();

  //Getting Data from CSV
  for (int i = 1; i<data.getRowCount(); i++) {
    TableRow row = data.getRow(i);
    String date = row.getString("Date");
    float kwh = row.getFloat("Average kWh");
    float price = row.getFloat("Average Bill");
    if (date.startsWith("7")) {   
      julybars.add(new JulyBar(yearx, kwh, price));
      yearx = yearx + 45;
    }
  }

  stroke(255);
  strokeWeight(3);
  line(50, 450, 800, 450);
  line(50, 0, 50, 450);

  //Creating the chart outline
  for (int r = 60; r+25<width; r = r+46) {
    text(year2, r, 475);
    year2++;
  }

  if (bill < 161) {
    for (int q = 450; q-25>0; q = q-40) {
      text(bill, 20, q);
      bill = bill+20;
    }
  }

  textSize(20);
  text("Average Austin household electricity bill in July of each year", 135, 25);
  textSize(12);
  text("Y E A R S", 375, 490);

  //All this just to rotate the y axis label
  float x = 30;
  float y = 150;
  textAlign(CENTER, BOTTOM);
  pushMatrix();
  translate(x, y);
  rotate(-HALF_PI);
  text("Average Bill", -100, -15);
  popMatrix();
}

void draw() { 
  for (int i = 0; i < julybars.size(); i++) {
    JulyBar jb = julybars.get(i);
    jb.display();
  }
  
  // Displays a third datapoint, KWH, for each year graphed. INTERACTIVITY
  if (mousePressed == true) {
    fill(0);
    rect(75, 75, 240, 35);
    fill(200,0,0);
    JulyBar k = julybars.get(yearClicker);
    text("Average KWH for year " + yearClicker + ":" , 160, 100);
    text(k.kwh, 275, 100);
    yearClicker++;

    if (yearClicker >= 16) {
      yearClicker = 0;
    }
  }
}