from Adafruit_CharLCD import Adafruit_CharLCD
import ScrollLCD

lcd = Adafruit_CharLCD()
lcd.begin(16,1)

# Some code here ...

text = "This text has more than 16 characters, but it will print pretty fine in the LCD!"
scroll(lcd, text)
