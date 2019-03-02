#include <CapacitiveSensor.h>

CapacitiveSensor   cs_4_8 = CapacitiveSensor(4,8); // 1M resistor between pins 4 & 8, pin 8 is sensor pin, add a wire and or foil
CapacitiveSensor   cs_10_12 = CapacitiveSensor(10,12);
void setup()                    
{
   cs_4_8.set_CS_AutocaL_Millis(0xFFFFFFFF);// turn off autocalibrate on channel 1 - just as an example
   Serial.begin(9600);
   pinMode(7,OUTPUT);

   cs_10_12.set_CS_AutocaL_Millis(0xFFFFFFFF);// turn off autocalibrate on channel 1 - just as an example
   Serial.begin(9600);
   pinMode(13,OUTPUT);
}

void loop()                    
{
 long sensor1 =  cs_4_8.capacitiveSensor(50);
 long sensor2 =  cs_10_12.capacitiveSensor(50);

   //3Serial.println(sensor1);  // print sensor output 
//   Serial.println(sensor2);
   if(sensor1 >= 50){
    digitalWrite(7,HIGH);
    Serial.println("1");
    delay(500);
   }
//   else{
//    digitalWrite(7,LOW);
//    Serial.println("0");
//   }

   else if(sensor2 >= 50){
    digitalWrite(13,HIGH);
    Serial.println("2");
    delay(500);
   }
   else{
    digitalWrite(13,LOW);
    Serial.println("0");
    delay(500);
   } 
  
}
