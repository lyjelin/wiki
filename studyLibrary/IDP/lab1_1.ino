const int greenPin = 13;
const int redPin = 9;

void setup() {
 pinMode(greenPin, OUTPUT);
 pinMode(redPin, OUTPUT);

}

void loop() {
  digitalWrite(greenPin, HIGH);
  digitalWrite(redPin, LOW);
  delay(1000);
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, HIGH);
  delay(1000);

}
