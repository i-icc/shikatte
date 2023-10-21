
/* 
 * 圧力センサーの値をシリアル通信で送るプログラム
 */


const int vol_pin = 0;//感圧センサアナログピン番号
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int sensorValue = analogRead(vol_pin);
  Serial.println(sensorValue);
}