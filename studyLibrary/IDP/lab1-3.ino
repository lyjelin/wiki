#define echoPin 12
#define trigPin 11

unsigned long start_time = 0;
int done = 1;
long distance_in_cm;

void setup() {
 Serial.begin (9600);
 pinMode(echoPin, INPUT);
 pinMode(trigPin, OUTPUT);
}

void loop() {
  measure_distance();
  Serial.print(distance_in_cm);
  Serial.println("");

  if (distance_in_cm < 10){
    if (distance_in_cm <= 4){
      tone(7, 1000, 1000);
    }
    else {
      tone(7, 1000, 10);
    }
  }
  delay(1000);
}

void measure_distance() {
  long duration;
  
  if (done) {     
    // reset start_time only if the distance has been measured 
    // in the last invocation of the method
    done = 0;
    start_time = millis();
    digitalWrite(trigPin, LOW);
  }
  
  if (millis() > start_time + 2) { 
    digitalWrite(trigPin, HIGH);
  }
  
  if (millis() > start_time + 10) {
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    distance_in_cm = (duration / 2.0) / 29.1;
    done = 1;
  }
  
}
