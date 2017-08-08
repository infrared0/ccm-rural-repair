/*
VBTS voltage sensor, serial out to be read by python script
 */

const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
//const int analogOutPin = 9; // Analog output pin that the LED is attached to

float analogValue = 0;        // value read from the pot
//int outputValue = 0;        // value output to the PWM (analog out)
float rawVoltage = 0;
float newVoltage = 0;             // start out assuming battery is full
float prevVoltage = 12;
float avgVoltage = 0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  // read the analog in value:
  analogValue = analogRead(analogInPin);
  rawVoltage = analogValue*5/1023;                 // arduino A0 is 0-5 V
  newVoltage = rawVoltage*11;                      // voltage divider divides by 11
  avgVoltage = 0.5*prevVoltage + 0.5*newVoltage;
  Serial.println(avgVoltage, 1);
  prevVoltage = avgVoltage;

  // wait 1 second before the next loop
  delay(1000);
}
