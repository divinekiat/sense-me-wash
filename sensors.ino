

const int sensor1=5;
const int sensor2=6;
const int sensor3=7;

int count1=0;
int count2=0;
int count3=0;

int prev_state1=HIGH;
int prev_state2=HIGH;
int prev_state3=HIGH;

String to_print=String(count1)+","+String(count2)+","+String(count3);;

void setup() {
  pinMode(sensor1,INPUT);
  pinMode(sensor2,INPUT);
  pinMode(sensor3,INPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(sensor1)==HIGH && prev_state1==LOW){
    prev_state1=HIGH;
    count1++;
    to_print=String(count1)+","+String(count2)+","+String(count3);
    delay(200);
  }
  else if (digitalRead(sensor1)==LOW) prev_state1=LOW; 
  
  if(digitalRead(sensor2)==HIGH && prev_state2==LOW){
    prev_state2=HIGH;
    count2++;
    to_print=String(count1)+","+String(count2)+","+String(count3);
    delay(200);
  }
  else if (digitalRead(sensor2)==LOW) prev_state2=LOW; 
  
  if(digitalRead(sensor3)==HIGH && prev_state3==LOW){
   prev_state3=HIGH;
   count3++;
   to_print=String(count1)+","+String(count2)+","+String(count3);
   delay(200);
  }
  else if (digitalRead(sensor3)==LOW) prev_state3=LOW; 
  
   Serial.println(to_print);
   Serial.flush();

}
