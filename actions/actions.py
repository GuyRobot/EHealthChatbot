# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import List, Dict, Text, Any

from rasa_sdk import Action, Tracker
import requests

URL = "https://guysmedchatt.serveo.net/webhook/chat"


class ActionUtter(Action):
    def name(self) -> Text:
        return "action_utter_healthcare"

    async def run(self, dispatcher, tracker: Tracker, domain) -> List[Dict[Text, Any]]:
        message = tracker.latest_message["text"]
        response = requests.post(URL, json={"message": message})
        dispatcher.utter_message(text=response.json()["message"])
        return []
