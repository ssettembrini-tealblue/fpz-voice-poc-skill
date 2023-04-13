from mycroft import MycroftSkill, intent_file_handler
import json
import time
from mycroft.util.parse import extract_number
from mycroft.messagebus import Message


def send_bus(self,type_function, value):  
    self.bus.emit(Message(type_function,
                          {'utterances': [value],  
                            'lang': 'en-us'}))

class FpzVoicePoc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
  
    @intent_file_handler('SetFrequency.intent')
    def set_frequency(self, message):
        self.speak_dialog('OperationDone')
        targetvalue = int(extract_number(message.data.get('freq')))
        self.speak_dialog('ChangedFrequency', {'value': targetvalue})
        send_bus(self,"set",targetvalue);
    
    @intent_file_handler('IncreaseFrequency.intent')
    def handle_increase_frequency(self, message):
        self.speak_dialog('OperationDone')
        offsetincrease = int(extract_number(message.data.get('freq')))
        self.speak_dialog('IncreasedFrequency', 
                          {'offsetincrease': offsetincrease})
        send_bus(self,"increase",offsetincrease);
    
    @intent_file_handler('DecreaseFrequency.intent')
    def handle_decrease_frequency(self, message):
        self.speak_dialog('OperationDone')
        offsetvalue = int(extract_number(message.data.get('freq')))
        self.speak_dialog('DecreasedFrequency', {'offset': offsetvalue})
        send_bus(self,"decrease",offsetvalue);
    
    @intent_file_handler('StartBlower.intent')
    def handle_start_blower(self, message):
        self.speak_dialog('OperationDone')       
        self.speak_dialog('StartedBlower')
        send_bus(self,"start",1);

    
    @intent_file_handler('StopBlower.intent')
    def handle_stop_blower(self, message):
        self.speak_dialog('OperationDone')       
        self.speak_dialog('StoppedBlower')
        send_bus(self,"stop",0);
    
def create_skill():
    return FpzVoicePoc()

