/*
Voltage sensor, serial out to be read by python script
 */
const int analogInPin = A0;   // Analog input pin that battery is attached to

float analogValue = 0;        // value read from the battery
float rawVoltage = 0;
float newVoltage = 0;         // start out assuming battery is full
float prevVoltage = 12;
float avgVoltage = 0;
float voltageThresh = 8;

int voltageLight = 4;
int voltageSound = 3;
int voltageFreq = 440;

/*
Software sensors, via serial in from python script
 */
// sensors
// total backhaul light also on this wire
int backhaulOn = 0;
int backhaulLight = 13;
int backhaulSound = 12;
int backhaulFreq = 494;
char backhaulCode = 'b';
boolean received_b = false;

// total signal light
int signalOn = 0;
int signalLight = 2;
int signalSound = 11;
int signalFreq = 523;
char signalCode = 's';
boolean received_s = false;

// sub signal lights

// signal prob 2
int memoryOn = 0;
int memoryLight = 10;
char memoryCode = 'm';
boolean received_m = false;

// signal prob 3
int temperatureOn = 0;
int temperatureLight = 9;
char temperatureCode = 't';
boolean received_t = false;

// sub signal lights
// signal prob 1
int pingOn = 0;
int pingLight = 8;
char pingCode = 'p';
boolean received_p = false;

// signal prob 4
int antennaOn = 0;
int antennaLight = 7;
char antennaCode = 'a';
boolean received_a = false;

int soundLength = 500;

// received signal
const int MaxChars = 2;
char strValue[MaxChars+1];
int index = 0;


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(backhaulLight, OUTPUT);
  pinMode(signalLight, OUTPUT);
  pinMode(memoryLight, OUTPUT);
  pinMode(temperatureLight, OUTPUT);
  pinMode(pingLight, OUTPUT);
  pinMode(antennaLight, OUTPUT);
  pinMode(voltageLight, OUTPUT);
}

void loop() {
  if (received_b) {
    if (backhaulOn > 0) {
      digitalWrite(backhaulLight, HIGH);
      noTone(signalSound);
      noTone(voltageSound);
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
    }
    else {
      digitalWrite(memoryLight, LOW);
    }
    received_m = false;
  }
  if (received_t) {
    if (temperatureOn > 0) {
      digitalWrite(temperatureLight, HIGH);
    }
    else {
      digitalWrite(temperatureLight, LOW);
    }
    received_t = false;
  }
  if (received_p) {
    if (pingOn > 0) {
      digitalWrite(pingLight, HIGH);
    }
    else {
      digitalWrite(pingLight, LOW);
    }
    received_p = false;
  }
  if (received_a) {
    if (antennaOn > 0) {
      digitalWrite(antennaLight, HIGH);
    }
    else {
      digitalWrite(antennaLight, LOW);
    }
    received_a = false;
  }
  
  signalOn = (memoryOn || temperatureOn || pingOn || antennaOn);
  if (signalOn > 0) {
    digitalWrite(signalLight, HIGH);
    noTone(backhaulSound);
    noTone(voltageSound);
    tone(signalSound, signalFreq, soundLength);
    delay(soundLength);
  }
  else {
    digitalWrite(signalLight, LOW);
  }
  
  // Voltage sensor. Read the analog in voltage value:
  
  analogValue = analogRead(analogInPin);
  rawVoltage = analogValue*5/1023;                 // arduino A0 is 0-5 V
  newVoltage = rawVoltage*11;                      // voltage divider divides by 11
  avgVoltage = 0.5*prevVoltage + 0.5*newVoltage;
  Serial.println(avgVoltage, 1);
  prevVoltage = avgVoltage;

  if (avgVoltage < voltageThresh) {
//    Serial.println(avgVoltage, 1);
    digitalWrite(voltageLight, HIGH);
    noTone(backhaulSound);
    noTone(signalSound);
    tone(voltageSound, voltageFreq, soundLength);
    delay(soundLength);
  }
  else {
    digitalWrite(voltageLight, LOW);
  }

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
      else if (ch == pingCode) {
        strValue[index] = 0;
        pingOn = atoi(strValue);
        index = 0;
        received_p = true;
        Serial.println(pingOn, 1);
      }
      else if (ch == antennaCode) {
        strValue[index] = 0;
        antennaOn = atoi(strValue);
        index = 0;
        received_a = true;
        Serial.println(antennaOn, 1);
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
