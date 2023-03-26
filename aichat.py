import config
import azure.cognitiveservices.speech as speechsdk
import openai
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from termcolor import colored

# Setup the Azure OpenAI Sevice
openai.api_key = config.openai_api_key 
openai.api_base = config.openai_api_base  
openai.api_type = config.openai_api_type 
openai.api_version = config.openai_api_version 

# Setup the Azure Speech cognative serivce, used for both recognition and synthesis.
speech_config = speechsdk.SpeechConfig(config.speech_key, config.speech_region)
audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

# Setup the speech recognizer.
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_output_config)

# Load the openai persona config, which includes the synthesis voice and AI character.
persona = config.personas[config.persona_name]
voice = persona["voice"]

# is a voice style is provided get the value
voice_style = ''
if 'style' in persona: 
    voice_style = persona["style"]

# Set the AI's initial system message, giving it some context for the conversation
system_message = persona["system_message"]

# Setup speech synthesis.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config = speech_config, audio_config = audio_config)

# Setup sentiment analysis.
text_analytics_client = TextAnalyticsClient(config.endpoint, AzureKeyCredential(config.key))

# Prompts Azure OpenAI with a request and synthesizes the response.
def ask_openai(prompt):

    # Ask Azure OpenAI Service
    response = openai.ChatCompletion.create(
        engine=config.openai_deployment_id,
        messages = prompt, 
        temperature=1,
        max_tokens=400,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    # extract the ai text response, and clean up the text.
    aitext = response['choices'][0]['message']['content']
    
    print(colored('Azure OpenAI response\t[' + aitext + ']',"blue"))
    print("Tokens [p/t/c]\t\t[{}/{}/{}]".format(response['usage']['prompt_tokens'],response['usage']['total_tokens'], response['usage']['completion_tokens']))
    
    # Get the sentiment method.
    result = text_analytics_client.analyze_sentiment(documents=[aitext])[0]
    print("Sentiment Score\t\t[{}]".format(result.sentiment))

    # Create SSML for the speech synthesizer by replacing tokens in the XML template
    ssml = config.ssml.replace('$text$',aitext)
    ssml = ssml.replace('$voice$',voice)
    ssml = ssml.replace('$style$',voice_style)

    # Speak
    speech_synthesizer.speak_ssml_async(ssml).get()

    # Return the text so that it can be added to the AI prompt.
    return aitext

# Continuously listens for speech input to recognize and send as text to Azure OpenAI
def chat_with_open_ai():

    # Setup the ai with the initial system message, describing the how the model shall behave.
    response = [{"role":"system","content":system_message}]

    print("Persona:\t\t[{}]".format(config.persona_name))

    while True:
        print(colored("Azure OpenAI is listening. Say 'Stop', 'Exit' or press Ctrl-Z to end the conversation.", 'red'))
        try:

            # Get audio from the microphone and then send it to the TTS service.
            speech_recognition_result = speech_recognizer.recognize_once_async().get()

            # If speech is recognized, send it to Azure OpenAI and listen for the response.
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                if speech_recognition_result.text == "Stop." or speech_recognition_result.text == "Exit.":
                    print("Conversation ended.")
                    break

                print(colored("Recognized speech\t[{}]".format(speech_recognition_result.text),"green"))

                response.append({"role":"user","content":"" + speech_recognition_result.text + ""})
                ai_reposonse = ask_openai(response)
                response.append({"role":"assistant","content":"" + ai_reposonse + ""})

            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
                break
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
        except EOFError:
            break

# Main
try:
    chat_with_open_ai()
except Exception as err:
    print("Encountered exception. {}".format(err))