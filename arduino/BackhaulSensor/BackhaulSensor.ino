/*
Voltage sensor, serial out to be read by python script
 */
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
//const int analogOutPin = 9; // Analog output pin that the LED is attached to

float analogValue = 0;        // value read from the pot
//int outputValue = 0;        // value output to the PWM (analog out)
float rawVoltage = 0;
float newVoltage = 0;             // start out assuming battery is full
float prevVoltage = 12;
float avgVoltage = 0;

/*
Software sensors, via serial in from python script
 */
// sensors
int backhaulOn = 0;
int backhaulLight = 13;
int backhaulSound = 12;
int backhaulFreq = 440;
char backhaulCode = 'b';
boolean received_b = false;

int signalOn = 0;
int signalLight = 4;
int signalSound = 3;
int signalFreq = 494;
char signalCode = 's';
boolean received_s = false;

int memoryOn = 0;
int memoryLight = 10;
//int memorySound = 10;
int memoryFreq = 494;
char memoryCode = 'm';
boolean received_m = false;

int temperatureOn = 0;
int temperatureLight = 9;
//int temperatureSound = 6;
int temperatureFreq = 523;
char temperatureCode = 't';
boolean received_t = false;

// insert 2 more problems here

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
  // read the analog in voltage value:
  analogValue = analogRead(analogInPin);
  rawVoltage = analogValue*5/1023;                 // arduino A0 is 0-5 V
  newVoltage = rawVoltage*11;                      // voltage divider divides by 11
  avgVoltage = 0.5*prevVoltage + 0.5*newVoltage;
  Serial.println(avgVoltage, 1);
  prevVoltage = avgVoltage;

  // wait 1 second before the next loop- is this too much?
  delay(1000);
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
