from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
from mycroft.messagebus import Message
from mycroft.configuration import LocalConf
from mycroft.configuration.locations import (
    DEFAULT_CONFIG,
    OLD_USER_CONFIG,
    SYSTEM_CONFIG,
    USER_CONFIG
)
import json
import time

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
        
    @intent_file_handler('SwitchLanguage.intent')
    def handle_switch_language(self, message):
    
        from mycroft.configuration.config import (
            LocalConf, USER_CONFIG, Configuration
        )
        
        inputlang=message.data.get('lang')
        
        if inputlang == 'italian':
            lang='it-it' 
        elif inputlang == 'inglese':
            lang='en-us'
        else:
            lang='en-us'
        
        new_config = {
            'lang': lang
        }
        
        user_config = LocalConf(USER_CONFIG)
        user_config.merge(new_config)
        user_config.store()
        
        self.speak_dialog('OperationDone')       
        self.speak_dialog('SwitchedLanguage', {'value': inputlang})

    
def create_skill():
    return FpzVoicePoc()

