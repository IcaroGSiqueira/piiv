int ledPin1 = 6;
int ledPin2 = 7;
int in1 = 0;
int in2 = 0;

//configurando os pinos (executado apenas uma vez)
void setup(){
 Serial.begin(9600);
 pinMode(ledPin1, OUTPUT);
 pinMode(ledPin2, OUTPUT);
}
 
//laço principal (executado infinitamente)
void loop() {
  if(Serial.available()){
    in1 = Serial.read();
  }
  if(Serial.available()){
    in2 = Serial.read();
  }  
  if(in1 == 1){
    if(in2 == 1){
      digitalWrite(ledPin1,HIGH);  
      delay(500);  
    }else{
      digitalWrite(ledPin1,LOW);
    }
  }else{
    if(in2 == 1){
      digitalWrite(ledPin2,HIGH);  
      delay(500);  
    }else{
        digitalWrite(ledPin2,LOW);
    }
  }
}
