import sys
sys.path.append('/home/pi/lcd')
import lcd
lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("MY NAME IS", 2)
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string("VIVEK", 2)
lcd.GPIO.cleanup()
