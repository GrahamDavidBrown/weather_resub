import requests


class Weather_Current:
    def __init__(self):
        zipcode = input("Zip: ")
        response = requests.get("http://api.wunderground.com/api/cb2c431de61398f4/geolookup/q/{}.json".format(zipcode))
        sun_activity = requests.get("http://api.wunderground.com/api/cb2c431de61398f4/astronomy/q/{}.json".format(zipcode))
        sun_activity = sun_activity.json()
        sunrise = {"hour": sun_activity['sun_phase']['sunrise']['hour'], "minute": sun_activity['sun_phase']['sunrise']['minute']}
        sunset = {"hour": sun_activity['sun_phase']['sunset']['hour'], "minute": sun_activity['sun_phase']['sunset']['minute']}
        json_dict = response.json()
        city = json_dict['location']['city']
        state = json_dict['location']['state']
        print(city)
        print(state + "\n")
        response = requests.get('http://api.wunderground.com/api/cb2c431de61398f4/conditions/q/{}/{}.json'.format(state, city))
        json_dict = response.json()
        self.zipcode = zipcode
        self.sunrise = sunrise
        self.sunset = sunset
        self.city = city
        self.state = state
        self.temperature_string = json_dict['current_observation']['temperature_string']
        self.weather = json_dict['current_observation']['weather']
