# SPDX-FileCopyrightText: 2024 ChatGPT
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_pca9685 import PCA9685

class MotorController:
    def __init__(self):
        self.pca = PCA9685(board.I2C())
        # i2c = board.I2C()  # Автоматическое определение SDA/SCL
        # self.pca = PCA9685(i2c)
        speed = 100
        self.speed = speed
        left_ch_a=self.pca.channels[1]  # IN1
        left_ch_b=self.pca.channels[0] # IN2
        right_ch_a=self.pca.channels[3] # IN3
        right_ch_b=self.pca.channels[2] # IN4
        self.left_a = left_ch_a
        self.left_b = left_ch_b
        self.right_a = right_ch_a
        self.right_b = right_ch_b
        
        # Настройка частоты PWM (для моторов лучше 50-100Hz)
        self.pca.frequency = 60
    def _set_motor(self, ch_a, ch_b, speed):
            # Ограничиваем скорость от -100% до 100%
            speed = max(-100, min(100, speed))
            pwm = abs(speed) * 65535 // 100  # Преобразуем в 16-битное значение
            
            if speed > 0:
                ch_a.duty_cycle = pwm
                ch_b.duty_cycle = 0
            elif speed < 0:
                ch_a.duty_cycle = 0
                ch_b.duty_cycle = pwm
            else:
                ch_a.duty_cycle = 0
                ch_b.duty_cycle = 0

    def handle_command(self, command):
        if command == 'forward':
            self._set_motor(self.left_a, self.left_b, self.speed)
            self._set_motor(self.right_a, self.right_b, self.speed)
            # Реализация движения вперед
        elif command == 'backward':
            self._set_motor(self.left_b, self.left_a, self.speed)
            self._set_motor(self.right_b, self.right_a, self.speed)
            # Реализация движения назад
        # ... другие команды
        elif command == 'left':
            self._set_motor(self.left_b, self.left_a, self.speed)
            self._set_motor(self.right_a, self.right_b, self.speed)
        
        elif command == 'right':
            self._set_motor(self.left_a, self.left_b, self.speed)
            self._set_motor(self.right_b, self.right_a, self.speed)
        
        elif command == 'stop':
            self._set_motor(self.left_a, self.left_b, 0)
            self._set_motor(self.right_a, self.right_b,0)

   
    # def move_forward(self, speed):
    #     self._set_motor(self.left_a, self.left_b, speed)
    #     self._set_motor(self.right_a, self.right_b, speed)

    # def move_backward(self, speed):
    #     self.move_forward(-speed)

    # def stop(self):
    #     for ch in [self.left_a, self.left_b, self.right_a, self.right_b]:
    #         ch.duty_cycle = 0

    

# if __name__ == "__main__":
#     # Инициализация PCA9685
#     # i2c = board.I2C()  # Автоматическое определение SDA/SCL
#     # pca = PCA9685(i2c)
    
#     try:
#         # Настройка каналов (пример для L298N драйвера)
#         motor_ctl = MotorController(
#             pca,
#             left_ch_a=pca.channels[1],  # IN1
#             left_ch_b=pca.channels[0],  # IN2
#             right_ch_a=pca.channels[3], # IN3
#             right_ch_b=pca.channels[2] # IN4
#         )
        
#         print("Motor test started...")
#         motor_ctl.move_forward(100)
#         time.sleep(2)
#         motor_ctl.move_backward(100)
#         time.sleep(2)
        
#     finally:
#         motor_ctl.stop()
#         pca.deinit()
#         print("Motors stopped and PCA deinitialized")


