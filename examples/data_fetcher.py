open_meteo_obj = OpenMeteo(35.69,51.42)
temp = open_meteo_obj.get_current_temperature()
print(temp)

open_weather_obj = OpenWeather(35.69,51.42, api_token="dc24061ced1507a4174c8107527499a6")
temp = open_weather_obj.get_current_temperature()
print(temp)