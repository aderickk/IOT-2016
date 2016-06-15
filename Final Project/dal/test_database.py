from dal_tsl2591 import tsl2591Dal
from dal_bmp183 import bmp183Dal
from dal_dht11 import dht11Dal

# TSL 2591
test1 = tsl2591Dal()
new1 = test1.add(13, 13, 313)
print (new1)
new2 = test1.add(8, 88, 888)
print (new2)
result = test1.read_All()
for res in result:
        print(res)

# BMP 183
test2 = bmp183Dal()
new1 = test2.add(10, 20, 30, 400)
print (new1)
new2 = test2.add(90, 80, 70, 600)
print (new2)
result = test2.read_All()
for res in result:
        print(res)

# DHT 11
test3 = dht11Dal()
new1 = test3.add(69, 6)
print (new1)
new2 = test3.add(96, 9)
print (new2)
result = test3.read_All()
for res in result:
        print(res)


