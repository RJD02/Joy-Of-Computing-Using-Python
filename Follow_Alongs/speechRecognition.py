def run():
    import speech_recognition as sr
    # Can change "back-in-black-official-video.wav" to any .wav file on your computer
    AUDIO_FILE = ("back-in-black-official-video.wav")
    #User audio
    r = sr.Recognizer() # Initialize the recognizer
    
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
    # Reads the audio file
    
    try:
        print("Audio file contains ", r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech could not understand audio")
    except sr.RequestError:
        print("Couldn't get result from Google Speech Recogniztion")
    

