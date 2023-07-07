from datetime import *
import time
import random
print()
print("uygulama başlıyor!")
print()
random_metin = ["ben klavye hız testi yapıyorum", "klavye parmak hızımı öğrenmeye çalışıyorum","kalvyede hızlı olup olmadığımı öğrenmeye çalışıyorum", "on parmak hızımı bulmaya çalışıyorum","hızlı bir şekilde yazıp yazamadığımı öğreniyorum", "klavyede ne kadar hızlıyım bilmek istiyorum","bu test bana ne kadar hızlı yazdığımı gösterecek","verilen paragrafı ne kadar hızlı yazabilirim"]
metin =(random.choice(random_metin))
time.sleep(2.5)
print("Aynısını Yazınız: {}".format(metin))
before = datetime.now()

if metin == input(": "):
    after = datetime.now()
    speed= after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(metin) / seconds, 1)

    print("Tebrikler!",len(metin),"Karakter zunluğundaki metin için;")
    print("Skorunuz: {} saniye.".format(seconds))
    print("Saniyede {} harf yazdınız ".format(letter_per_second))
else:
    print("Metini Yanlış Yazdınız!")