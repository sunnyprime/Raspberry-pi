import sys
sys.path.append('/home/pi/lcd')
import lcd

lcd.lcd_init()
for i in range (10):
    j="My name is "+str(i)
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string(j, 2)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string("VIVEK", 2)
lcd.GPIO.cleanup()
print("Done")
