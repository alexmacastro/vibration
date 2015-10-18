void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  int valVib = analogRead(0);
  float mV = (valVib / 1024.0) * 3300;
  float vib = (mV - 1500)  / 300;

  Serial.print(vib);
  Serial.print("\n");

  delay(1);
}
