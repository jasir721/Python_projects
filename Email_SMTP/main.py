import smtplib
#We have to lower the security of the email account so that we can send using pythonn
#And we have to turn on Access to less secure apps in chrome
import datetime as dt
import random
MY_EMAIL="jasirkadarsha721091@gmail.com"
MY_PASSWORD="abcd1234()"
now=dt.datetime.now()
weekday=now.weekday()
if weekday==6:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #For encryption and security purpoeses
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n{quote}")


