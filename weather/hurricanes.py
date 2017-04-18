import requests


class Hurricanes():
    def __init__(self, zipcode):
        self.canes = requests.get("http://api.wunderground.com/api/cb2c431de61398f4/currenthurricane/q/{}.json".format(zipcode))
