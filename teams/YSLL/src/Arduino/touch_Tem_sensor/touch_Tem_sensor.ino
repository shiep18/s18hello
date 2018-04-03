#include <Microduino_Tem_Hum.h>
Tem_D1  termo;

#define BuzzerPin6 6

void setup()
{
  termo.begin();

  Serial.begin(9600);
}

void loop()
{
  if (!digitalRead(4)) 
  {
    Serial.println(termo.getTemperature());
    if (termo.getTemperature() > 25) {
      tone(BuzzerPin6,200);
      delay(1000);
      noTone(BuzzerPin6);

    }

  }

}
