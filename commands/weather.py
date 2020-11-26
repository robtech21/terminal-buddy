import requests, json

def get_weather():
    location = input("Enter yourlocation or a keyword to search it: ")
    api_key = "xxxx"
    baseurl = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"

    weather_file = requests.get(baseurl)
    weather_json = weather_file.json()
    country = weather_json['request']['query']
    condition = weather_json['current']['weather_descriptions']
    temperature_c = weather_json['current']['temperature']
    humidity = weather_json['current']['humidity']
    wind_mph = weather_json['current']['wind_speed']
    response_raw = f"""Now is {condition} in {country} at this moment. The temperature is {temperature_c} degrees, the humidity is {humidity}% and the wind speed is {wind_mph} mph."""
    final_weather = response_raw.translate({ord(i): None for i in '\[\'\]'})


    print(final_weather)
