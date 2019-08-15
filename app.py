import pyttsx3

# Voice Ids
en_us_voice_id = 'com.apple.speech.synthesis.voice.Alex'
en_us_female_voice_id = 'com.apple.speech.synthesis.voice.samantha'
en_us_female_voice_id_2 = 'com.apple.speech.synthesis.voice.Victoria'
en_gb_voice_id = 'com.apple.speech.synthesis.voice.daniel'
tr_voice_id = 'com.apple.speech.synthesis.voice.yelda'


def speak(text):
    engine_io.say(text)
    engine_io.runAndWait()


def voice_speechrate_starttext():
    # voices = engine_io.getProperty('voices')

    speech_rate = int(input("Speech Rate:(10-200):"))
    language = int(input("Language:"
                         "\n[1] EN"
                         "\n[2] TR:"))

    if language not in [1, 2]:
        print("Incorrect Language")
        exit(1)

    if language == 2:
        start_text = "Ne söylememi istiyorsun?"
        voice_id = tr_voice_id
    elif language == 1:
        start_text = "What do you want me to say?"
        gender = int(input("Gender:"
                           "\n[1] Male"
                           "\n[2] Female:"))

        if gender not in [1, 2]:
            print("Incorrect Gender")
            exit(1)
        if gender == 1:
            voice_id = en_us_voice_id
        else:
            voice_id = en_us_female_voice_id
    else:
        start_text = "What do you want me to say?"
        voice_id = en_us_voice_id

    return voice_id, speech_rate, start_text


if __name__ == '__main__':
    voice_id, speech_rate, start_text = voice_speechrate_starttext()

    # Start
    engine_io = pyttsx3.init()
    engine_io.setProperty('rate', speech_rate)
    engine_io.setProperty('voice', voice_id)

    speak(start_text)
    while True:
        phrase = input("--> ")
        if phrase == "exit":
            exit(0)

        speak(phrase)
