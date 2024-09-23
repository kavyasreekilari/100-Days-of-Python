import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "kavyakilari.info@gmail.com"
MY_PASSWORD = "zuatzcedpofhgxvq"
MY_LAT = 41.784850
MY_LONG = -88.186280

def is_iss_pverhead():
# iss-now api

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # if response.status_code == 404:
    #     raise Exception("That resource does not exist.")
    # elif response.status_code == 401:
    #     raise Exception("You are not authorized to access this data.")

    response.raise_for_status() # handles http errors
    data = response.json()

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)
    print(iss_position)

    if MY_LAT-5 < iss_position < MY_LAT+5 and MY_LONG-5 < iss_position < MY_LONG+5:
        return True

def is_night():
# sunrise-sunset api

    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_pverhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )