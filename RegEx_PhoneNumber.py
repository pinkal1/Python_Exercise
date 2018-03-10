''' Script that verifies if the string is a phone number with the following formats:
Format 1: (nnn) - nnn - nnnn
Format 2: nnnnnnnnnn
Note: Any format not matching the above 2 should be classified as non-matching.'''

import re

def is_valid_PhoneNumber(PhoneNumber):
    ph_nbr_pattern = '(\(\d{3}\)\s-\s\d{3}\s-\s\d{4})|(\d{10})'
    r1 = re.compile(ph_nbr_pattern)
    matchObj = r1.match(PhoneNumber)
    if matchObj:
        print (PhoneNumber)
    else:
        print ("Non-matching",PhoneNumber)


test_numbers=["(123)  - 123 - 1234",
              "(123) - 1234 - 1234",
              "(123) - 1234 - 123a",
              "123 - 1234 - 1234",
              "1231231234",
              "123123123a",
              "12312312345",
              "(123)1231234",
              "012 345 6789",
              "123-13-1234",
              "123.123.1234",
              "123)123 1234",
              "456-7890",
              "123-45-6789",
              "123 4567890",
              "123/456-7890",
              "(111)-111-1111"]

for PhoneNumber in test_numbers:
    is_valid_PhoneNumber(PhoneNumber)