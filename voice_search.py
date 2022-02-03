import speech_recognition
import pywhatkit as playonyoutube
import webbrowser

def audio_input():
    choose = str(input('Do you want to search in Youtube or Google? :')).lower()
    print('Listening.......\n')

    # call the speech_recognition
    audio_input = speech_recognition.Recognizer()

    # uses microphone as source
    with speech_recognition.Microphone() as source:

        #listen for audio input
        audio = audio_input.listen(source)
        # result voice -- text
        input_said = ''

        # use try to make sure the audio is decting if not raise except://
        try:
            # using google api convert audio to text
            input_said = audio_input.recognize_google(audio)
            print('You said:  {}'.format(input_said))

            if choose == 'youtube':
                playonyoutube.playonyt('https://www.youtube.com/results?search_query={}'.format(input_said))
            else:
                webbrowser.open('https://www.google.com/search?q={}'.format(input_said))


        except Exception:
            print('No input Detected')


audio_input()




# pip install pipwin
# pipwin install pyaudio
