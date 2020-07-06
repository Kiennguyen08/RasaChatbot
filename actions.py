# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from urllib.request import urlopen


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return 'action_get_weather'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&apikey=2fee25a8c056372e89e9d9a73c7e9b73'
        json_url = urlopen(url)
        data = json.loads(json_url.read())
        return_msg = 'Temperature: '+str(data['main']['temp']) + '\n' + 'Weather: '+ str(data['weather'][0]['main'])
        # Tra ve cho nguoi dungz
        dispatcher.utter_message(return_msg)

        return []



# import json
# from urllib.request import urlopen


# class action_get_weather(Action):
#     def name(self):
#             # Doan nay khai bao giong het ten ham ben tren la okie
#             return 'action_get_weather'
#     def run(self, dispatcher, tracker, domain):
#             # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
#             url = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&apikey=2fee25a8c056372e89e9d9a73c7e9b73'
#             json_url = urlopen(url)
#             data = json.loads(json_url.read())
#             return_msg = 'Temperature: '+str(data['main']['temp']) + '\n' + 'Weather: '+ str(data['weather'][0]['main'])
#             # Tra ve cho nguoi dungz
#             dispatcher.utter_message(return_msg)
#             return []

