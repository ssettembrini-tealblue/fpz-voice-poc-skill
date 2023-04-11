from mycroft import MycroftSkill, intent_file_handler


class FpzVoicePoc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('poc.voice.fpz.intent')
    def handle_poc_voice_fpz(self, message):
        self.speak_dialog('poc.voice.fpz')


def create_skill():
    return FpzVoicePoc()

