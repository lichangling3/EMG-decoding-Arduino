void setup() {
  // put your setup code here, to run once:
  Serial.begin(230400);
}

unsigned int capteurs[6]; //2 bytes per unsigned int
unsigned char byteArray[24]; //12*2

const long interval = 1000; //Pour avoir une fréquence de 1000Hz ---> 1000us

void loop() {
  static unsigned long lastRead;
  if (micros() - lastRead  >= interval) {
  lastRead += interval;
  capteurs[0] = analogRead(A0);
  capteurs[1] = analogRead(A1);
  capteurs[2] = analogRead(A2);
  capteurs[3] = analogRead(A3);
  capteurs[4] = analogRead(A4);
  capteurs[5] = analogRead(A5);
  capteurs[6] = analogRead(A6);
  capteurs[7] = analogRead(A7);
  capteurs[8] = analogRead(A8);
  capteurs[9] = analogRead(A9);
  capteurs[10] = analogRead(A10);
  capteurs[11] = analogRead(A11);

  byteArray[0] = (unsigned char)((capteurs[0] >> 8) & 0xFF);
  byteArray[1] = (unsigned char)(capteurs[0] & 0xFF);

  byteArray[2] = (unsigned char)((capteurs[1] >> 8) & 0xFF);
  byteArray[3] = (unsigned char)(capteurs[1] & 0xFF);

  byteArray[4] = (unsigned char)((capteurs[2] >> 8) & 0xFF);
  byteArray[5] = (unsigned char)(capteurs[2] & 0xFF);

  byteArray[6] = (unsigned char)((capteurs[3] >> 8) & 0xFF);
  byteArray[7] = (unsigned char)(capteurs[3] & 0xFF);

  byteArray[8] = (unsigned char)((capteurs[4] >> 8) & 0xFF);  
  byteArray[9] = (unsigned char)(capteurs[4] & 0xFF);

  byteArray[10] = (unsigned char)((capteurs[5] >> 8) & 0xFF);
  byteArray[11] = (unsigned char)(capteurs[5] & 0xFF);

  byteArray[12] = (unsigned char)((capteurs[6] >> 8) & 0xFF);
  byteArray[13] = (unsigned char)(capteurs[6] & 0xFF);

  byteArray[14] = (unsigned char)((capteurs[7] >> 8) & 0xFF);
  byteArray[15] = (unsigned char)(capteurs[7] & 0xFF);

  byteArray[16] = (unsigned char)((capteurs[8] >> 8) & 0xFF);
  byteArray[17] = (unsigned char)(capteurs[8] & 0xFF);

  byteArray[18] = (unsigned char)((capteurs[9] >> 8) & 0xFF);
  byteArray[19] = (unsigned char)(capteurs[9] & 0xFF);

  byteArray[20] = (unsigned char)((capteurs[10] >> 8) & 0xFF);  
  byteArray[21] = (unsigned char)(capteurs[10] & 0xFF);

  byteArray[22] = (unsigned char)((capteurs[11] >> 8) & 0xFF);
  byteArray[23] = (unsigned char)(capteurs[11] & 0xFF);
  
  Serial.write(byteArray, 24);
  
  };
}
