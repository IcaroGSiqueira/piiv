
int pwm = 3;
int out = A0;
int val = 0;
int j = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int i = 5 ; i <= 255; i += 50) {
    //Serial.println(i);
    while (j < 60) {
      // escreve o valor no pino pwm
      analogWrite(pwm, i);
      // le o valor do pino pwm
      val = analogRead(out);
      // ajusta o valor analogico para o range de 0 a 5 volts (por 1023 ocorrem interferencias)
      val = (val/ 1000)*5;
      Serial.println(val); // imprime o valor na porta serial
      delay(125);
      j++;
    }
    j = 0;
  }

  for (int i = 255 ; i >= 5; i -= 50) {
    //Serial.println(i);
    while (j < 60) {
      analogWrite(pwm, i);
      val = analogRead(out);
      val = (val * 5) / 1000;
      Serial.println(val);
      delay(125);
      j++;
    }
    j = 0;
  }
}
