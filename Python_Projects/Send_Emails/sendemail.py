import os

import random
import smtplib


def send_email():
    user = input("Enter Your Name :- ")
    email = input("Enter Your Email Address :- ")
    
    msg = (f"Dear{user}, \n Welcome To Prashant World!!! ")
    s = smtplib.SMTP('smpt.gmail.com',587)
    # s = smtplib.SMTP('prashantjadhav6@gmail.com',)
    s.starttls()
    s.login("Your Gmail Account ", "Your App password")
    s.sendmail('&&&&&&&&&&&',email,msg)
    print("Email Send!")
    


send_email()    



