import controlP5.*;
ControlP5 cp5;
int i;
int ci=-8;
int lim=430;
ArrayList<Listing> myListings;
PImage next=new PImage();
XML rss,rssw;
void setup(){
  size(700,500);
  background(155);
  textAlign(LEFT, TOP);
  textSize(15);
  textLeading(20);
  stroke(1);
  rss = loadXML("http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk");
  cp5 = new ControlP5(this);
  cp5.addButton("previous")
     .setValue(-1)
     .setPosition(500,20)
     .setSize(50,25)
     ;
  cp5.addButton("next")
     .setValue(1)
     .setPosition(580,20)
     .setSize(50,25)
     ;
  i=0;
  cp5.addButton("business")
     .setValue(1)
     .setPosition(650,350)
     .setSize(40,25)
     ;
  cp5.addButton("education")
     .setValue(1)
     .setPosition(650,300)
     .setSize(40,25)
     ;
  cp5.addButton("health")
     .setValue(1)
     .setPosition(650,250)
     .setSize(40,25)
     ;
  cp5.addButton("tech")
     .setValue(1)
     .setPosition(650,200)
     .setSize(40,25)
     ;
  cp5.addButton("world")
     .setValue(1)
     .setPosition(650,150)
     .setSize(40,25)
     ;
}
  public void controlEvent(ControlEvent theEvent) {
    //println(theEvent.getController().getName());
  
}
  public void previous() {
    if (ci>0){
    ci-=8;
    lim=430;
    }
}
  public void next() {
    if (ci+8<rss.getChildren("channel/item/title").length){
      lim=430;
      ci+=8;
      if (ci+8>rss.getChildren("channel/item/title").length){
        lim=50*(rss.getChildren("channel/item/title").length-ci)+30;
      }
    }
}
  public void business() {
    rssw = loadXML("http://feeds.bbci.co.uk/news/business/rss.xml?edition=uk"); 
    ci=0;
    lim=430;
  }
  public void education() {
    rssw = loadXML("http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk");  
    ci=0;
    lim=430;
  }
  public void health() {
    rssw = loadXML("http://feeds.bbci.co.uk/news/health/rss.xml?edition=uk"); 
    ci=0;
    lim=430;
  }
  public void tech() {
    rssw = loadXML("http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk"); 
    ci=0;
    lim=430;
  }
  public void world() {
    rssw = loadXML("http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk");
    ci=0;
    lim=430;
  }

void draw(){
  color a =color(250, 23, 23);
  color b =color(169, 66, 198);
  color c =color(28,95,234); 
  color d =color(28, 234, 198);
  color e =color(234, 142, 28);
  noStroke();
  fill(155);
  rect(0,0,700,500);
  fill(195);
  rect(0,430,700,70);
  fill(0);
  i=0;
  i=ci;
  rss = rssw;
  XML[] channeltitle = rss.getChildren("channel/title"); 
  XML[] channeldata = rss.getChildren("channel/lastBuildDate"); 
  text(channeltitle[0].getContent(), 10,10);
  text(channeldata[0].getContent(), 10+textWidth(channeltitle[0].getContent())+20,10);
  XML[] titleXML = rss.getChildren("channel/item/title"); 
  int posx=50;
  int posy=50;
  for ( posy = 50; posy < lim; posy++) {
    //int rc = int(random(5));
    if (i%5==0){
          fill(a);}
    if (i%5==1){
          fill(b);} 
    if (i%5==2){
          fill(c);}
    if (i%5==3){
          fill(d);} 
    if (i%5==4){
          fill(e);}
    if (i<titleXML.length){
      String title = titleXML[i].getContent();
      text(title,posx,posy);
    }
    if (mouseX>50&&mouseX<50+textWidth(titleXML[i].getContent())&&mouseY<posy+15&&mouseY>posy-5){
        String[] deslist = rss.getChildren("channel/item/description")[i].getContent().split(" ");
        int ix=50;
        int iy=440;
        fill(0);
        for (int j = 0; j<deslist.length; j++){
          if (ix+textWidth(deslist[j])<700){
            text(deslist[j],ix,iy);
            ix+=textWidth(deslist[j])+8;
          }
          if (ix+textWidth(deslist[j])>680){
            ix=50;
            iy+=20;
            text(deslist[j],ix,iy);
            ix+=textWidth(deslist[j])+8;
          }
        }
        if (mousePressed == true) { 
          link(rss.getChildren("channel/item/link")[i].getContent());
        }
      }
    posy+=50;
    i+=1;   
  }

}