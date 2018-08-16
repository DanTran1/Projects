PImage img1;
PImage img2;
PImage img3;
PImage img4;
PImage img5;
PImage img6;
PImage img;
void setup() {
  
  surface.setResizable(true);
  img1 = loadImage("foo.png");
  img2 = loadImage("foo.png");
  img3 = loadImage("foo.png");
  img4 = loadImage("foo.png");
  img5 = loadImage("foo.png");
  img6 = loadImage("foo.png");
  img = img1;
  surface.setSize(img1.width, img1.height);
  }
  
void draw() {
  image(img, 0,0);
}
void grayscale(PImage img) {
  
  img.loadPixels();
  colorMode(RGB, 255,255,255);
  for (int x = 0; x < img.width; x++) {
    for (int y = 0; y < img.height; y++) {
      int index = x + y*img.width;
      float red = red(img.pixels[index]);
      float blue = blue(img.pixels[index]);
      float green = green(img.pixels[index]);
      
      float colorAvg = (red + blue + green) / 3;
      img.pixels[index] = color(colorAvg);
    }
  }
  img.updatePixels();
}

void contrast(PImage img) {
  img.loadPixels();
  colorMode(HSB, 360,100,100);
    for (int x = 0; x < img.width; x++) {
      for (int y = 0; y < img.height; y++) {
        int index = x +y*img.width;
        float brightness = brightness(img.pixels[index]);
        float hue = hue(img.pixels[index]);
        float saturation = saturation(img.pixels[index]);
        colorMode(HSB, 360, 100, 100);
          
        if (brightness >= 40 && brightness < 90) {
          img.pixels[index] = color(hue, saturation, brightness + 10);
        }
        
        else if (brightness < 40 && brightness > 2) {
          img.pixels[index] = color(hue, saturation, brightness - 2);
        }
      }
    }
    img.updatePixels();
}
          
        
void gaussian(PImage img) {
  
  float [][] matrix = {{.0625,.125,.0625},
                        {.125,.250,.125},
                       {.0625,.125,.0625}};
                      
  colorMode(RGB, 255, 255, 255);
  img.loadPixels();

  for (int x = 1; x < img.width - 1; x++) {
    for (int y = 1; y < img.height - 1; y++) {
      int index = x + y*img.width;
      float red = 0;
      float blue = 0;
      float green = 0;
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          int k_index = (x + i - 1) + img.width*(y + j - 1);
          red += red(img.pixels[k_index]) * matrix[i][j];
          blue += blue(img.pixels[k_index]) * matrix[i][j];
          green += green(img.pixels[k_index]) * matrix[i][j];
          
          }
       }
       red = constrain(abs(red), 0, 255);
       blue = constrain(abs(blue), 0, 255);
       green = constrain(abs(green), 0, 255); 
       img.pixels[index] = color(red, green, blue);
    }
  }
  img.updatePixels();

}

void sobel(PImage img) {
  
  float [][] xMatrix = {{-1,0,1},
                        {-2,0,2},
                        {-1,0,2}};
                        
  float [][] yMatrix = {{-1,-2,-1},
                          {0,0,0},
                          {1,2,1}};
  
  colorMode(HSB, 360, 100, 100);
  img.loadPixels();
  for (int x = 1; x < img.width - 1; x++) {
    for (int y = 1; y < img.height - 1; y++) {
      int index = x + y*img.width;
      float xBrightness = 0;   
      float yBrightness = 0;
      
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          int k_index = (x + i - 1) + img.width*(y + j - 1);
          xBrightness += brightness(img.pixels[k_index]) * xMatrix[i][j];
          yBrightness += brightness(img.pixels[k_index]) * yMatrix[i][j];
        }
      }
      
      float brightness = sqrt((xBrightness * xBrightness) + (yBrightness * yBrightness));
      brightness = constrain(brightness, 0, 100);
      img.pixels[index] = color(0, 0, brightness);
    }
  }
  img.updatePixels();
}

void moreRed(PImage img) {
  img.loadPixels();
  colorMode(RGB,255,255,255);
  for (int x = 0; x < img.width; x++) {
    for (int y = 0; y < img.height; y++) {
      int index = x + y*img.width;
      float red = red(img.pixels[index]) + 30;
      float green = green(img.pixels[index]);
      float blue = blue(img.pixels[index]);
      red = constrain(red, 0, 255);
      
      img.pixels[index] = color(red, green, blue);
    }
  }
  img.updatePixels();
}
      
void keyPressed() {
  if (key == '0') {
    image(img1,0,0);
    img = img1;
  }
  else if (key == '1') {
    grayscale(img2);
    image(img2,0,0);
    img = img2;
  }
  
  else if (key == '2') {
    contrast(img3);
    image(img3,0,0);
    img = img3;
  }
  
  else if (key == '3') {
    gaussian(img4);
    image(img4,0,0);
    img = img4;
  }
  
  else if (key == '4') {
    sobel(img5);
    image(img5,0,0);
    img = img5;
  }
  
  else if (key == '5') {
    moreRed(img6);
    image(img6,0,0);
    img = img6;
  }
}