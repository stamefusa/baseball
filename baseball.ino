#include <Servo.h>

Servo ser_p, ser_m, ser_b;
int state = -1;

void setup() {
  ser_m.attach(7);
  ser_p.attach(8);
  ser_b.attach(9);

  ser_m.write(50);
  ser_p.write(60);
  ser_b.write(20);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    state = Serial.read() - 48;
    Serial.println(state); 

    if (state == 1) {
      // ピッチャー
      ser_p.write(20);
    } else if (state == 2) {
      // 魔球
      ser_m.write(90);
      // ピッチャー
      ser_p.write(20);
    } else if (state == 3) {
      // バッター
      ser_b.write(150);
    } else if (state == 0) {
      // リセット
      ser_m.write(50);
      ser_p.write(60);
      ser_b.write(20);
    }
  }
  delay(100);
}
