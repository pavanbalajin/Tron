# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
import os
import openai
from rasa_sdk.events import SessionStarted, ActionExecuted
from rasa_sdk.events import ConversationPaused

class action_setclaimnumber(Action):
    def name(self) -> Text:
        return "action_setclaimnumber"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            clid = tracker.get_slot("clid")
            SlotSet("clid", clid)
            button_resp=[
                  {
                      "title": "Queries",
                      "payload": "great_queries"
                  },
                  {
                      "title": "Process",
                      "payload": "greet_process"
                  },
                  {
                      "title": "chit-chat",
                      "payload": "great_chit-chat"
                  }
              ]
            dispatcher.utter_message(text="Thank you! please select your preference:", buttons=button_resp)
            #dispatcher.utter_message(image="test.jpg")
            return []

class action_fetchdata(Action):
    def name(self) -> Text:
        return "action_fetchdata"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"totalcost") 
            dispatcher.utter_message(f"Total Vehicle repair cost is : {test}")
           #SlotSet("clid", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your claim number")

        return []

class action_fetchlabourcost(Action):
    def name(self) -> Text:
        return "action_fetchlabourcost"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"labourcost") 
            dispatcher.utter_message(f"Total labour cost for Vehicle repair cost is : {test}")
            #SlotSet("clnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your labour claim number")

        return []

class action_fetchpartscost(Action):
    def name(self) -> Text:
        return "action_fetchpartscost"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"partscost") 
            dispatcher.utter_message(f"Total parts cost for Vehicle repair cost is : {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your claim number")

        return []

class action_fetchdamagesummary(Action):
    def name(self) -> Text:
        return "action_fetchdamagesummary"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"remark") 
            dispatcher.utter_message(f"Vehicle damage summary : {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your claim number")

        return []

class action_imagecount(Action):
    def name(self) -> Text:
        return "action_imagecount"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"IMGNO") 
            dispatcher.utter_message(f"Number of images in the docket is : {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your docket number")

        return []

class action_missingimages(Action):
    def name(self) -> Text:
        return "action_missingimages"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"MISIMG") 
            dispatcher.utter_message(f"My Answer is : {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your docket number")

        return []

class action_imagequality(Action):
    def name(self) -> Text:
        return "action_imagequality"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"IMGQ") 
            dispatcher.utter_message(f"Image Quality is : {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your docket number")

        return []

class action_imagevisibility(Action):
    def name(self) -> Text:
        return "action_imagevisibility"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"CVIMG") 
            dispatcher.utter_message(f"Car is {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your docket number")

        return []

class action_VIN(Action):
    def name(self) -> Text:
        return "action_VIN"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        clid = tracker.get_slot("clid")
        print(clid)
        if clid: # user_phone is not None
            test = DataFetch(clid,"VIMG") 
            dispatcher.utter_message(f"VIN image is {test}")
            #SlotSet("pclnum", None)
        else: # user_phone is None
            dispatcher.utter_message("Please share your docket number")

        return []

class action_resetdata(Action):
    def name(self) -> Text:
        return "action_resetdata"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            SlotSet("clid", None)
            dispatcher.utter_message("You're welcome")
            return []

class action_default_fallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            import os
            openai_key  = os.getenv('OPENAI_API_KEY')
            msg =  tracker.latest_message['text'] 
            response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            max_tokens=10,
            temperature=0.5,
            messages=[
                    {"role": "user", "content": str(msg)}
                ]
            )
            dispatcher.utter_message(response.choices[0].message.content.strip())
            SlotSet("called", "done")
        # pause the tracker so that the bot stops responding to user input
            return [UserUtteranceReverted()]

def DataFetch(dnum,col):
    cnx = sqlite3.connect('resourceDB.db')
    cursor = cnx.cursor()
    MY_SQL ="SELECT " + col + " FROM inspection WHERE claimid =?"
    df = pd.read_sql(MY_SQL, con=cnx, params=[dnum])
    return df.values[0][0]

class ActionDeactivateLoop(Action):
    def name(self) -> Text:
        return "action_deactivate_loop"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Logic to deactivate the loop
        dispatcher.utter_message("Loop deactivated.")
        return []
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
