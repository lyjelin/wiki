const int grnLedPin = 13;
const int redLedPin = 9;
const int buttonPin = 2;

int grnLedToggle = LOW;
int redLedToggle = HIGH;
int lastButtonState = HIGH;
int buttonState;

void setup() {
  pinMode(grnLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  digitalWrite(redLedPin, redLedToggle);
  pinMode(buttonPin, INPUT_PULLUP);

}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW && lastButtonState == HIGH) {
    grnLedToggle = !grnLedToggle;
    redLedToggle = !redLedToggle;
    
    digitalWrite(grnLedPin, grnLedToggle);
    digitalWrite(redLedPin, redLedToggle);
  }
  
  lastButtonState = buttonState;
  delay(100);

}
