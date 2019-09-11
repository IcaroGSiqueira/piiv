int analogPin = 0; 
int ledPin = 2;
int val=0;
float tensao=0;
 
//configurando os pinos (executado apenas uma vez)
void setup(){
 Serial.begin(9600);
 pinMode(ledPin, OUTPUT);
}
 
//laço principal (executado infinitamente)
void loop() {
  
  val = analogRead(analogPin);   // lê o pino de entrada
  tensao = ((5.0 * val)/1023);
  Serial.println(tensao); // imprime o valor na porta serial
  if(tensao >= "2.5"){
    pinMode(ledPin,HIGH);    
  }else{
    pinMode(ledPin,LOW);
  }
}
