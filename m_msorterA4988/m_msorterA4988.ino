#include <AccelStepper.h>
#include <Servo.h>

#define dirPin 11
#define stepPin 12
#define motorInterfaceType 1
#define enableStepper 10
AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);
Servo myServo;
int servoPin = 9;

String myCmd;
int dt = 150;

void moveServoToContainer(String color){
  if (color == "purple"){
    myServo.write(180);
  }
    else if (color == "orange"){
    myServo.write(26);
  }
    else if (color == "green"){
    myServo.write(51);
  }
    else if (color == "yellow"){
    myServo.write(78);
  }
    else if (color == "red"){
    myServo.write(106);
  }
    else if (color == "brown"){
    myServo.write(134);
  }
    else if (color == "pink"){
    myServo.write(156);
  } 
    else if (color == "purple"){
    myServo.write(180);
  }    
    else if (color == "empty") {
    myServo.write(3);
  }
}



void setup() {
  // put your setup code here, to run once:
pinMode(enableStepper,1);
digitalWrite(enableStepper,1);
Serial.begin(115200);
myServo.attach(servoPin);
stepper.setMaxSpeed(12000);
stepper.setAcceleration(4000);
pinMode(dirPin,1);
pinMode(stepPin,1);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(enableStepper,0);
while(Serial.available()==0){
  delay(1);
}
myCmd = Serial.readStringUntil('\r');
moveServoToContainer(myCmd);
delay(150);
stepper.setCurrentPosition(0);
stepper.moveTo(320);
stepper.runToPosition();
delay(200);
Serial.println("1");

}
