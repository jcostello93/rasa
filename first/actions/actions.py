from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecomendarPlato(Action):

    def name(self) -> Text:
        return "action_recomendar_plato"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('RUNNING')
        ingredientes = tracker.get_slot("ingrediente") or []
        ingredientes = [i.lower() for i in ingredientes]

        tiene_tomate = "tomate" in ingredientes
        tiene_queso = "queso" in ingredientes
        tiene_pan = "pan" in ingredientes

        if tiene_tomate and tiene_queso and tiene_pan:
            recomendacion = "Puedes preparar un bocadillo."
        elif tiene_queso and tiene_pan:
            recomendacion = "Puedes preparar un montadito."
        elif tiene_tomate and tiene_pan:
            recomendacion = "Puedes preparar una tostada."
        elif tiene_tomate and tiene_queso:
            recomendacion = "Puedes preparar una ensalada capresa."
        else:
            recomendacion = "No tienes suficientes ingredientes, te recomiendo ir a un restaurante."

        dispatcher.utter_message(text=recomendacion)
        return []
