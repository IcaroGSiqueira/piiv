#include <SoftwareSerial.h>

void setup() {
Serial.begin(9600);
}

void loop()
{
 int val = analogRead(0);  //Read in analog input #0 (0-1023)
 val = map(val, 0, 1023, 0, 255);  //Scales 0-1023 to 0-255 (or whatever you want)
 Serial.println(val,DEC); //Prints as decimal, with line feed
}
