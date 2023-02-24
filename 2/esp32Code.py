from machine import Pin, ADC
from machine import Pin, SoftI2C
import ssd1306
from time import sleep


# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

solar_panel = ADC(Pin(34))
solar_panel.atten(ADC.ATTN_11DB)       #Full range: 3.3v


# oled.text('Hello, World 1!', 0, 0)
# oled.text('Hello, World 2!', 0, 10)
# 
#         
# oled.show()


while True:
  solar_panel_value = solar_panel.read() 
  print(solar_panel_value)
  oled.fill(0)
  oled.text('Hello, World 1!', 0, 0)
  
  oled.text("", 0, 10)
  sleep(0.1)
  oled.text(str(solar_panel_value), 0, 10)
  oled.show()


  sleep(1)
  

