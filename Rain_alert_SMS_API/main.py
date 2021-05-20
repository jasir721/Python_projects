#API endpoints and API parameters we have checked
#Previously what ever we used were from free API's
#Many will cange bcause it is difficult to collect those data's
#For free service there is a API key

import requests
from twilio.rest import Client
End_point="https://api.openweathermap.org/data/2.5/onecall"
api_key="#####"
LAT="28.066700"
LON="95.327500"
account_sid = "ACfe1520255d2898e4951a9a528e49ea49"
auth_token ="#####"
weather_params = {
    "lat":LAT,
    "lon":LON,
    "exclude":"current,minutely,daily",
    "appid":api_key,
}
response=requests.get(End_point,params=weather_params)
response.raise_for_status()
weather_data=response.json()["hourly"]
# print(weather_data)
will_rain=False
for i in range(12):
    hour=weather_data[i]
    weather=hour["weather"][0]
    print(weather)
    weather_id=weather["id"]
    if weather_id <600:
        will_rain= True
        print("rain")
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to take umbrella",
        from_='+18036536998',
        to='+918802607303'
    )
    print(message.status)

