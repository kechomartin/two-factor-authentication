import time
import pyotp

key = ""

totp = pyotp.TOTP(key)

print(totp.now())

time.sleep(30)

print(totp.now())

input_code = input("Enter 2FA Code:")

print(totp.verify(input_code))

