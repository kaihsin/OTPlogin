import os
import pyotp
import getpass


#ssh User@Host
OTPKey= <Your OTPKey>
Host  = <Host address>
User  = <User ID>
Passwd = getpass.getpass("passwd:")




totp = pyotp.TOTP(OTPKey)
print("OTP  : ",totp.now())
print("login...")
os.system('sshpass -p %s ssh %s@%s'%(Passwd+totp.now(), User, Host))


