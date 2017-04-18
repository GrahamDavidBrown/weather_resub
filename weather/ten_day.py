import requests


class Ten_Day():
    def __init__(self, weather_current):
        ten_day = requests.get("http://api.wunderground.com/api/cb2c431de61398f4/forecast10day/q/{}/{}.json".format(weather_current.state, weather_current.city))
        ten_day = ten_day.json()
        ten_day = ten_day['forecast']['txt_forecast']['forecastday']
        days = []
        for twelve_hour in ten_day:
            days.append(Day(twelve_hour))
        self.days = days


class Day():
    def __init__(self, twelve_hour):
        self.title = twelve_hour['title']
        self.forecast = twelve_hour['fcttext']
