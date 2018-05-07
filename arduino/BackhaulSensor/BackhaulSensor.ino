/*
CCN backhaul sensor, serial in from python script
 */

//const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int statusLight = 0;
const int MaxChars = 2;
char strValue[MaxChars+1];
int index = 0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
}

void serialEvent() {

  while (Serial.available()) {
    char ch = Serial.read();
    //Serial.println("written \n");
    Serial.write(ch);
    if (index < MaxChars && isDigit(ch)) {
      strValue[index++] = ch;
    }
    else {
      strValue[index] = 0;
      statusLight = atoi(strValue);
      index = 0;
    }
    //Serial.println("final \n");
    //Serial.println(statusLight, 1);
  }
}

