# import smtplib
# sender_email = "raselsumon51@gmail.com"
# rec_email = "raselsumon5151@gmail.com"
# password = input(str("Please enter your password : "))
# message = "Hey, this was sent using python"
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(sender_email, password)
# print("Login success")
# server.sendmail(sender_email, rec_email, message)hi


# print("Email has been sent to ", rec_email)


import pyautogui
import time
time.sleep(3)
while True:

    pyautogui.typewrite('hi')
    pyautogui.press('enter')
