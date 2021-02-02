#define Sclk 13 //--- connect this to the display module CLK pin (Serial Clock)
#define Mosi 11 //--- connect this to the display module DIN pin (Serial Data)
#define Rst  9 //--- connect this to the display module RES pin (Reset)
#define Dc   8 //--- connect this to the display module D/C  pin (Data or Command)
#define Cs   10 //--- connect this to the display module CS  pin (Chip Select)

// Color definitions
#define BLACK           0x0000
#define BLUE            0x0006
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0  
#define WHITE           0xFFFF
#define BACKGROUND      0x0000

#include <Adafruit_SSD1331.h>

Adafruit_SSD1331 display = Adafruit_SSD1331(Cs, Dc, Mosi, Sclk, Rst);

const int qtiPin = 2;
int countBlack = 0;
byte last_color_state = LOW;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  display.begin();
  tftPrintTest();
  delay(2000);  
  display.fillScreen(BACKGROUND);
  display.setCursor(0,0);
}

void loop() {
  
  // charge up the capacitor
  pinMode(qtiPin, OUTPUT);
  digitalWrite(qtiPin, HIGH);
  delayMicroseconds(1000);

  // prepare to read the voltage
  pinMode(qtiPin, INPUT);
  digitalWrite(qtiPin, LOW);
  delayMicroseconds(1000);

  byte black_or_white = digitalRead(qtiPin);

  if (black_or_white == HIGH){
     display.fillScreen(YELLOW);
     display.setTextColor(BLACK);  
     display.setTextSize(3);
     display.setCursor(5, 5);
     display.println(countBlack);
  }
  else if (black_or_white == LOW && last_color_state == HIGH){
      countBlack+=1;
      display.fillScreen(YELLOW);
      display.setTextColor(BLACK);  
      display.setTextSize(3);
      display.setCursor(5, 5);
      display.println(countBlack);
    
  }
  last_color_state = black_or_white;

  delay(100);
  
}

void tftPrintTest() {
  display.fillScreen(MAGENTA);
  display.setCursor(15, 5);
  display.setTextColor(BLACK);  
  display.setTextSize(2);
  display.println("LYJ");
  display.setCursor(0, 25);
  display.setTextColor(BLUE);
  display.setTextSize(2);
  display.println("LAB1-4");
  display.setCursor(15, 50);
  delay(1500);

}
