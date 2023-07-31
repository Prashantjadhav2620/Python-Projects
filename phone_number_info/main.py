import  phonenumbers 
from test import number

# main.py
import phonenumbers
from phonenumbers import geocoder

ch_num = phonenumbers.parse(number, None)
print(geocoder.description_for_number(ch_num, "en"))


from phonenumbers import carrier 

service_number = phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_number,None))

from phonenumbers import carrierdata

carrier_number = phonenumbers.parse(number,None)
carrier_info = carrier.name_for_number(carrier_number, None)
print("Carrier information:", carrier_info)
 


