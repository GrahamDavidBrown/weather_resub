import requests
from weather_current import Weather_Current
from ten_day import Ten_Day
from hurricanes import Hurricanes


def main():
    try:
        weather_current = Weather_Current()
        ten_day = Ten_Day(weather_current)
        hurricanes = Hurricanes(weather_current.zipcode)
        print("Current Hurricanes!!!")
        for cane in hurricanes.canes.json()['currenthurricane']:
            print(cane['stormInfo']['stormName'])
        print("\n")
        print("Today's Sunrise: " + weather_current.sunrise['hour'] + ":" + weather_current.sunrise['minute'])
        print("Today's Sunset: " + weather_current.sunset['hour'] + ":" + weather_current.sunset['minute'], end ="\n\n")
        print("FORECAST:")
        for day in ten_day.days:
            print(day.title, end=": ")
            print(day.forecast, end="\n\n")
    except:
        main()



main()
