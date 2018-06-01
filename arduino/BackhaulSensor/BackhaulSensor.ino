/*
CCN backhaul sensor, serial in from python script
 */

// sensors
int backhaulOn = 0;
int backhaulLight = 13;
int backhaulSound = 8;
int backhaulFreq = 440;
char backhaulCode = 'b';
boolean received_b = false;

int memoryOn = 0;
int memoryLight = 12;
int memorySound = 7;
int memoryFreq = 494;
char memoryCode = 'm';
boolean received_m = false;

int temperatureOn = 0;
int temperatureLight = 8;
int temperatureSound = 6;
int temperatureFreq = 523;
char temperatureCode = 't';
boolean received_t = false;

int soundLength = 500;

// received signal
const int MaxChars = 2;
char strValue[MaxChars+1];
int index = 0;


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(backhaulLight, OUTPUT);
  pinMode(memoryLight, OUTPUT);
  pinMode(temperatureLight, OUTPUT);

  // Add another pin for sound output
}

void loop() {
  if (received_b) {
    if (backhaulOn > 0) {
      digitalWrite(backhaulLight, HIGH);
      noTone(memorySound);
      noTone(temperatureSound);
      tone(backhaulSound, backhaulFreq, soundLength);
      delay(soundLength);
    }
    else {
      digitalWrite(backhaulLight, LOW);
    }
    received_b = false;
  }
  if (received_m) {
    if (memoryOn > 0) {
      digitalWrite(memoryLight, HIGH);
      noTone(backhaulSound);
      noTone(temperatureSound);
      tone(memorySound, memoryFreq, soundLength);
      delay(soundLength);
    }
    else {
      digitalWrite(memoryLight, LOW);
    }
    received_m = false;
  }
  if (received_t) {
    if (temperatureOn > 0) {
      digitalWrite(temperatureLight, HIGH);
      noTone(backhaulSound);
      noTone(memorySound);
      tone(temperatureSound, temperatureFreq, soundLength);
      delay(soundLength);
    }
    else {
      digitalWrite(temperatureLight, LOW);
    }
    received_t = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char ch = Serial.read();
    //Serial.println("written \n");
    Serial.write(ch);
    if (index < MaxChars && isDigit(ch)) {
      strValue[index++] = ch;
    }
    else if (isAlpha(ch)) {
      if (ch == backhaulCode) {
        strValue[index] = 0;
        backhaulOn = atoi(strValue);
        index = 0;
        received_b = true;
        Serial.println(backhaulOn, 1);
      }
      else if (ch == memoryCode) {
        strValue[index] = 0;
        memoryOn = atoi(strValue);
        index = 0;
        received_m = true;
        Serial.println(memoryOn, 1);
      }
      else if (ch == temperatureCode) {
        strValue[index] = 0;
        temperatureOn = atoi(strValue);
        index = 0;
        received_t = true;
        Serial.println(temperatureOn, 1);
      }
      else {
        Serial.write("Undefined input \n");
      }
    }
    else {
      Serial.write("Undefined input \n");
    }
  }
}
