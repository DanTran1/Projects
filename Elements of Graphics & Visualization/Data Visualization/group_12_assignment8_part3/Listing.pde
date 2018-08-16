
class Listing{
  String sellerName;
  String shippingInfo;
  String auctionInfo;
  String description;
  
  Listing(String s, String sh, String a, String d){
    this.sellerName = s;
    this.shippingInfo = sh;
    this.auctionInfo = a;
    this.description = d;
  }
  
  void display(){
    textSize(20);
    fill(0);
    text(sellerName, 10,20);
    text(shippingInfo, 10, 50);
    text(auctionInfo, 10, 80);
  }
}