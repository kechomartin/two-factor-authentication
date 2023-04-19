import time
import pyotp
import qrcode

key = "SecureThisCode"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter code:")))
# uri = pyotp.totp.TOTP(key).provisioning_uri(name="Smith123",
#                                              issuer_name="Paypal")

# print(uri)
# qrcode.make(uri).save("totp.png")