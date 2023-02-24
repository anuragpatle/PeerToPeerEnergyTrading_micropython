from machine import Pin, ADC
from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import freesans20
import writer
import framebuf
import utime

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
  solar_panel_value = solar_panel.read() / 10
  print(solar_panel_value)
  oled.fill(0)
  
  sleep(0.1)

  # Data 1
  oled.text("Production Rate ",5,0)
  font_writer = writer.Writer(oled, freesans20)
  font_writer.set_textpos(5, 10)
  font_writer.printstring(str(solar_panel_value))
  font_writer.set_textpos(80, 10)
  font_writer.printstring("KWh")
  
  
  # Data 2
  oled.text("Capacity ",5,32)
  font_writer = writer.Writer(oled, freesans20)
  font_writer.set_textpos(5, 42)
  font_writer.printstring('108')
  font_writer.set_textpos(80, 42)
  font_writer.printstring("KW")
#   oled.text("Capacity ",10,30)
#   oled.text('108',50,30)
#   oled.text("Watt",90,30)

    
  oled.show()
  


  sleep(1)
  
