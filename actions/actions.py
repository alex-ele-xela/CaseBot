from typing import Any, Text, Dict, List
from . import utils

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        city = tracker.get_slot("city")
        phone = tracker.get_slot("phone")
        utils.write_human(True, name, city, phone)

        dispatcher.utter_message(text=f"Thank you {name}!. The following details have been saved:\n\
                                 City: {city}\nPhone number: {phone}")

        return []

