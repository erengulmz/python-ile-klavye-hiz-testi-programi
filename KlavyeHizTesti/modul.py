from datetime import *
import time
def geri_sayim():
    sure =int(input("başlatmak için lütfen 3'ü tuşlayıp 'enter'e basınız:"))
    while sure != 0:
        print(sure)
        time.sleep(1)
        sure = sure - 1
