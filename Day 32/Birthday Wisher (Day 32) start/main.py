import smtplib    # library used to send emails

my_email = "kavyakilari.info@gmail.com"
my_password = "zuatzcedpofhgxvq"    # App password for birthday_wisher app in Google Account security

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()   # makes the connection secure by encrpypting
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="kksgratitude@gmail.com", msg="Hello Kavya")

connection.close()

import datetime as dt
from datetime import datetime

now = dt.datetime.now()
year = now.year

date_of_birth = dt.datetime(year=1997, month=6, day=5)
print(date_of_birth)


