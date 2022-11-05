import gps_funktion
import umqtt_robust2 as mqtt
from machine import Pin,ADC, I2C
from time import sleep
import neopixel
import time
import fald_funktion
import buzzer

n = 12
p = 25

np = neopixel.NeoPixel(Pin(p), n )

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

while True:
    try:
        sleep(0.5)
        if len(mqtt.besked) != 0:
            mqtt.besked = ""
        mqtt.sync_with_adafruitIO()
        print(".", end = '')
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        
        analog_val = analog_pin.read()
        volts = (analog_val * 0.00085238)*5
        battery_percentage = volts*50 - 320
        print("the battery percentage is:", battery_percentage, "%")
        mqtt.web_print(battery_percentage, 'casp9367/feeds/batteri feed/csv')
        sleep(10)
        
        if battery_percentage > 90 and battery_percentage < 100:
            np[0] = (0, 10, 0)
            np[1] = (0, 10, 0)
            np[2] = (0, 10, 0)
            np[3] = (0, 10, 0)
            np[4] = (0, 10, 0)
            np[5] = (0, 10, 0)
            np[6] = (0, 10, 0)
            np[7] = (0, 10, 0)
            np[8] = (0, 10, 0)
            np[9] = (0, 10, 0)
            np[10] = (0, 10, 0)
            np[11] = (0, 10, 0)
            np.write()
        
        if battery_percentage > 80 and battery_percentage < 90:
            np[0] = (0, 0, 0)
            np[1] = (0, 10, 0)
            np[2] = (0, 10, 0)
            np[3] = (0, 10, 0)
            np[4] = (0, 10, 0)
            np[5] = (0, 10, 0)
            np[6] = (0, 10, 0)
            np[7] = (0, 10, 0)
            np[8] = (0, 10, 0)
            np[9] = (0, 10, 0)
            np[10] = (0, 10, 0)
            np[11] = (0, 10, 0)
            np.write()
        
        if battery_percentage > 70 and battery_percentage < 80:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 10, 0)
            np[3] = (0, 10, 0)
            np[4] = (0, 10, 0)
            np[5] = (0, 10, 0)
            np[6] = (0, 10, 0)
            np[7] = (0, 10, 0)
            np[8] = (0, 10, 0)
            np[9] = (0, 10, 0)
            np[10] = (0, 10, 0)
            np[11] = (0, 10, 0)
            np.write()
        
        if battery_percentage > 60 and battery_percentage < 70:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (50, 33, 0)
            np[4] = (50, 33, 0)
            np[5] = (50, 33, 0)
            np[6] = (50, 33, 0)
            np[7] = (50, 33, 0)
            np[8] = (50, 33, 0)
            np[9] = (50, 33, 0)
            np[10] = (50, 33, 0)
            np[11] = (50, 33, 0)
            np.write()
        
        if battery_percentage > 50 and battery_percentage < 60:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (50, 33, 0)
            np[6] = (50, 33, 0)
            np[7] = (50, 33, 0)
            np[8] = (50, 33, 0)
            np[9] = (50, 33, 0)
            np[10] = (50, 33, 0)
            np[11] = (50, 33, 0)
            np.write()
            
        if battery_percentage > 40 and battery_percentage < 50:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (0, 0, 0)
            np[6] = (50, 33, 0)
            np[7] = (50, 33, 0)
            np[8] = (50, 33, 0)
            np[9] = (50, 33, 0)
            np[10] = (50, 33, 0)
            np[11] = (50, 33, 0)
            np.write()
        
        if battery_percentage > 30 and battery_percentage < 40:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (0, 0, 0)
            np[6] = (0, 0, 0)
            np[7] = (0, 0, 0)
            np[8] = (50, 33, 0)
            np[9] = (50, 33, 0)
            np[10] = (50, 33, 0)
            np[11] = (50, 33, 0)
            np.write()
            
        if battery_percentage > 20 and battery_percentage < 30:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (0, 0, 0)
            np[6] = (0, 0, 0)
            np[7] = (0, 0, 0)
            np[8] = (0, 0, 0)
            np[9] = (10, 0, 0)
            np[10] = (10, 0, 0)
            np[11] = (10, 0, 0)
            np.write()
            
        if battery_percentage > 10 and battery_percentage < 20:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (0, 0, 0)
            np[6] = (0, 0, 0)
            np[7] = (0, 0, 0)
            np[8] = (0, 0, 0)
            np[9] = (0, 0, 0)
            np[10] = (10, 0, 0)
            np[11] = (10, 0, 0)
            np.write()
        
        if battery_percentage > 1 and battery_percentage < 10:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[4] = (0, 0, 0)
            np[5] = (0, 0, 0)
            np[6] = (0, 0, 0)
            np[7] = (0, 0, 0)
            np[8] = (0, 0, 0)
            np[9] = (0, 0, 0)
            np[10] = (0, 0, 0)
            np[11] = (10, 0, 0)
            np.write()
            
        mqtt.web_print(gps_data, 'casp9367/feeds/GpS/csv')        
        sleep(10) # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        
#         mqtt.web_print("test1")  Hvis der ikke angives et 2. argument vil default feed være det fra credentials filen      
#         sleep(4)  # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

 
 
 
