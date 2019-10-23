int ledPin1 = 6;
int ledPin2 = 7;
int in1 = 0;
int in2 = 0;
int brightness1 = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by
int brightness2 = 255;    // how bright the LED is
int fadeAmount2 = 5;    // how many points to fade the LED by

//configurando os pinos (executado apenas uma vez)
void setup(){
 Serial.begin(9600);
 pinMode(ledPin1, OUTPUT);
 pinMode(ledPin2, OUTPUT);
}
 
//laço principal (executado infinitamente)
void loop() {
  analogWrite(ledPin1, brightness1);
  analogWrite(ledPin2, brightness2);
  
  brightness1 = brightness1 + fadeAmount;
  brightness2 = brightness2 - fadeAmount2;

  if (brightness1 <= 0 || brightness1 >= 255) {
    fadeAmount = -fadeAmount;
  }

  if (brightness2 <= 0 || brightness2 >= 255) {
    fadeAmount = +fadeAmount;
  }

  if (brightness1 <= 0 || brightness1 >= 255) {
    fadeAmount2 = -fadeAmount2;
  }

  if (brightness2 <= 0 || brightness2 >= 255) {
    fadeAmount2 = +fadeAmount2;
  }
  delay(15);
}
