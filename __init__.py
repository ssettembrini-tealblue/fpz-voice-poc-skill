from mycroft import MycroftSkill, intent_file_handler
import json
import time
from mycroft.util.parse import extract_number

class FpzVoicePoc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('SetFrequency.intent')
    def set_frequency(self, message):
        self.speak_dialog('OperationDone')
        targetvalue = int(extract_number(message.data.get('freq')))
        self.speak_dialog('ChangedFrequency', {
                'value': targetvalue})
        time.sleep(1)
            
    @intent_file_handler('IncreaseFrequency.intent')
    def set_frequency(self, message):
        self.speak_dialog('OperationDone')
        offsetvalue = int(extract_number(message.data.get('freq')))
        self.speak_dialog('IncreasedFrequency', {
                'offset': offsetvalue})
        time.sleep(1)
    
    @intent_file_handler('DecreaseFrequency.intent')
    def set_frequency(self, message):
        self.speak_dialog('OperationDone')
        offsetvalue = int(extract_number(message.data.get('freq')))
        self.speak_dialog('DecreasedFrequency', {
                'offset': offsetvalue})
        time.sleep(1)
        
    @intent_file_handler('poc.voice.fpz.intent')
    def handle_poc_voice_fpz(self, message):
        self.speak_dialog('poc.voice.fpz')
        
def create_skill():
    return FpzVoicePoc()

