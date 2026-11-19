from abc import ABC, abstractmethod


class Sensor(ABC): #parent abstract class
  
  @abstractmethod
  def get_reading(self): #needed method of child classes
    pass

class PHsensor(Sensor): #child class
  def get_reading(self):
    print("[pH Sensor] Reading: 7.2 pH (Neutral)") #own way to use parent method



class TempSensor(Sensor): #child class
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C") #own way to use parent method


print("--- Lab Inventory System ---") #printing everything

ph = PHsensor()
temp = TempSensor()

ph.get_reading()
temp.get_reading()

print("----------------------------")
print("Zian da goat")