#define BuzzerPin2 2

void setup()
{

}

void loop()
{
  if (analogRead(A0) < 500) {
    tone(BuzzerPin2,1300);
    delay(500);
    tone(BuzzerPin2,1300);
    delay(500);
    noTone(BuzzerPin2);

  }

}
