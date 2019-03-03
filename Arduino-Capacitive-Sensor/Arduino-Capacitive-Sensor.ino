#include <CapacitiveSensor.h>

CapacitiveSensor   cs_1_2 = CapacitiveSensor(A5,A4);
CapacitiveSensor   cs_3_4 = CapacitiveSensor(3,4);
CapacitiveSensor   cs_5_6 = CapacitiveSensor(5,6);
CapacitiveSensor   cs_7_8 = CapacitiveSensor(7,8);
CapacitiveSensor   cs_9_10 = CapacitiveSensor(9,10);
CapacitiveSensor   cs_11_12 = CapacitiveSensor(11,12);
const int buttonPin = 0; 
int buttonState=0;
void setup()                    
{
   cs_1_2.set_CS_AutocaL_Millis(0xFFFFFFFF);
  Serial.begin(9600);

   cs_3_4.set_CS_AutocaL_Millis(0xFFFFFFFF);
  Serial.begin(9600);

   cs_5_6.set_CS_AutocaL_Millis(0xFFFFFFFF);
   Serial.begin(9600);

   cs_7_8.set_CS_AutocaL_Millis(0xFFFFFFFF);
   Serial.begin(9600);

   cs_9_10.set_CS_AutocaL_Millis(0xFFFFFFFF);
   Serial.begin(9600);

   cs_11_12.set_CS_AutocaL_Millis(0xFFFFFFFF);
   Serial.begin(9600);

   pinMode(buttonPin, INPUT);
   Serial.begin(9600);
}

void loop()                    
{
 long sensor1 =  cs_1_2.capacitiveSensor(50);
 long sensor2 =  cs_3_4.capacitiveSensor(50);
 long sensor3 =  cs_5_6.capacitiveSensor(50);
 long sensor4 =  cs_7_8.capacitiveSensor(50);
 long sensor5 =  cs_9_10.capacitiveSensor(50);
 long sensor6 =  cs_11_12.capacitiveSensor(50);
 buttonState = digitalRead(buttonPin);
 //Serial.println(sensor1);
   if (buttonState==LOW){
     Serial.println("change");
     delay(100);
    }
   if(sensor1 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("1");
    delay(100);
   }

   else if(sensor2 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("2");
    delay(100);
   }

   else if(sensor3 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("3");
    delay(100);
   }

   else if(sensor4 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("4");
    delay(100);
   }

   else if(sensor5 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("5");
    delay(100);
   }

   else if(sensor6 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("6");
    delay(100);
   }
   else{
    digitalWrite(13,LOW);
    Serial.println("0");
    delay(100);
   } 
  
}
