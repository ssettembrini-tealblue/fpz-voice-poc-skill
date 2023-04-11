from mycroft import MycroftSkill, intent_file_handler
import json

class FpzVoicePoc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('poc.voice.fpz.intent')
    def handle_poc_voice_fpz(self, message):
        freq_offset = message.data['freq']
        self.speak_dialog('IncreasedFrequency', {
                'offset': freq_offset})
        time.sleep(1)

def create_skill():
    return FpzVoicePoc() *

