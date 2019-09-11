int analogPin = 0; 
int val=0;
float tensao=0;
 
//configurando os pinos (executado apenas uma vez)
void setup(){
 Serial.begin(9600); 
}
 
//laço principal (executado infinitamente)
void loop() {
  
  val = analogRead(analogPin);   // lê o pino de entrada
  tensao = ((5.0 * val)/1023);
  Serial.println(tensao); // imprime o valor na porta serial
 
}
