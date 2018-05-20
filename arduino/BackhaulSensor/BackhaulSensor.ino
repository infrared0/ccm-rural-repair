/*
CCN backhaul sensor, serial in from python script
 */

//const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

// sensors
int backhaulLight = 0;
int backhaulPin = 13;
char backhaulCode = 'b';
boolean received_b = false;

int memoryLight = 0;
int memoryPin = 12;
char memoryCode = 'm';
boolean received_m = false;

int temperatureLight = 0;
int temperaturePin = 8;
char temperatureCode = 't';
boolean received_t = false;

// received signal
const int MaxChars = 2;
char strValue[MaxChars+1];
int index = 0;


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(backhaulPin, OUTPUT);
  pinMode(memoryPin, OUTPUT);
  pinMode(temperaturePin, OUTPUT);

  // Add another pin for sound output
}

void loop() {
  if (received_b) {
    if (backhaulLight > 0) {
      digitalWrite(backhaulPin, HIGH);
    }
    else {
      digitalWrite(backhaulPin, LOW);
    }
    received_b = false;
  }
  if (received_m) {
    if (memoryLight > 0) {
      digitalWrite(memoryPin, HIGH);
    }
    else {
      digitalWrite(memoryPin, LOW);
    }
    received_m = false;
  }
  if (received_t) {
    if (temperatureLight > 0) {
      digitalWrite(temperaturePin, HIGH);
    }
    else {
      digitalWrite(temperaturePin, LOW);
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
        backhaulLight = atoi(strValue);
        index = 0;
        received_b = true;
        Serial.println(backhaulLight, 1);
      }
      else if (ch == memoryCode) {
        strValue[index] = 0;
        memoryLight = atoi(strValue);
        index = 0;
        received_m = true;
        Serial.println(memoryLight, 1);
      }
      else if (ch == temperatureCode) {
        strValue[index] = 0;
        temperatureLight = atoi(strValue);
        index = 0;
        received_t = true;
        Serial.println(temperatureLight, 1);
      }
      else {
        Serial.write("Undefined input \n");
      }
    }
    else {
      Serial.write("Undefined input \n");
    }
    //Serial.println("final \n");
  }
}
