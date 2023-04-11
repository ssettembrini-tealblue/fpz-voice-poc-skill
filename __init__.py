from mycroft import MycroftSkill, intent_file_handler
import json
from mycroft.util.parse import extract_number

class FpzVoicePoc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('SetFrequency.intent')
    def set_frequency(self, message):
        freq_offset = int(extract_number(message.data['freq']))
        self.speak_dialog('IncreasedFrequency', {
                'offset': freq_offset})
        time.sleep(1)

def create_skill():
    return FpzVoicePoc() *

