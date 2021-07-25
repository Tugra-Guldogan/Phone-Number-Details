# Get Phone Number Details
# github.com/Tugra-Guldogan

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata
import time 

# Enter Phone Number Here  :

phoneNumber = phonenumbers.parse("PHONE_NUMBER_HERE")

time.sleep(0.3)
print(geocoder.description_for_number(phoneNumber, 'en'))
time.sleep(0.3)
print(carrier.name_for_number(phoneNumber, 'en'))
time.sleep(0.3)
print(phonemetadata.NumberFormat(phoneNumber, 'en'))

time.sleep(3)
print("Thanks for using") 
