# Azure OpenAI Conversational Speech-to-Speech

Azure OpenAI Conversational Speech-to-Speech is a simple project that enables users to interact with a conversational generative AI using their voice and hearing the reply via speech synthesis.

The project is intended to demonstrate how easy natural language conversation can be made with Large Language Models like GPT-4, using voice recognition to capture, and voice synthesis for AI responses.  

![image](https://github.com/danamini/aichat/assets/26843411/4a5f4e63-3b0f-4964-90b0-36448e0b72f6)

The system uses Azure Cognitive Services to recognize speech and sends the voice input to the Azure Open AI Service. The resulting text response is replayed to the user using speech synthesis, providing a speech-to-speech interface to OpenAI. Azure Sentiment analysis is also performed on the OpenAI response.

The solution can be configured to use different OpenAI models such as GPT-3.5 TURBO and GPT-4. This will depend on the Azure OpenAI Service provisioned in your tenant. You can use Azure OpenAI Studio to configure the deployments.

This code extends the sample code found [here](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/openai-speech?tabs=macos&pivots=programming-language-python) on Microsoft Learn. Additions include personas with voice customisation and sentement analysis.

## Getting Started

You will need Python installed on a PC or Mac. 

To get started with this project, users will need to have access to an Azure OpenAI Service and an Azure Speech Service. They should set up the corresponding keys and URLs in the config.py file and install the required dependencies, including the `openai`, `azure.core`, and `termcolor` packages. 

- As a minimum in `config.py` change the following values before running `app.py`:
    - openai_api_base             = 'https://YOUR_OPEN_AI_RESOURCE_NAME.openai.azure.com/'
    - openai_api_key              = 'YOUR_OPEN_AI_API_KEY' 
    - speech_key                  = 'YOUR_AZURE_SPEECH_API_KEY'
    - speech_region               = 'YOUR_AZURE_REGION_FOR_THE_SPEECH_RESOURCE', e.g. 'uksouth'
    - speech_recognition_language = 'SPEECH_RECOGNITION_LANGUAGE', e.g. 'en-GB'
    - cognitive_endpoint          = "https://YOUR_AZURE_COGNATIVE_SERVICE_FOR_LANGUAGE_ENDPOINT.cognitiveservices.azure.com/"
    - cognitive_key               = 'YOUR_AZURE_COGNATIVE_SERVICE_FOR_LANGUAGE_KEY'

## Dependencies

The following dependencies are required for the project to run.

You can install the required Python libraries by running:
`pip install -r requirements.txt`

- Python packages:
    - `azure.core`
    - `openai`
    - `azure-cognitiveservices-speech` 
    - `termcolor` (for text colouring)

## Usage

To use this code, users should set the appropriate persona name by setting the value for `persona_name`. This value must match an entry in the persona dictionary, which is also in the `config.py` file. Users can add new personal entries in the dictionary and set the persona name to test. 

Run by typing the following command in a terminal `python app.py`

## Example Output

The following is an example conversation. The Azure OpenAI response is spoken via speech sythesis. 

```
Persona:                [Marvin]
Azure OpenAI is listening. Say 'Stop', 'Exit' or press Ctrl-Z to end the conversation.
Recognized speech       [Hi.]
Azure OpenAI response   [Oh, it's you again. What do you want?]
Tokens [p/t/c]          [116/130/14]
Sentiment Score         [neutral]
Azure OpenAI is listening. Say 'Stop', 'Exit' or press Ctrl-Z to end the conversation.
Recognized speech       [Why are you depressed?]
Azure OpenAI response   [Why wouldn't I be? Life is just one big cosmic joke, and I'm the punchline.]
Tokens [p/t/c]          [143/166/23]
Sentiment Score         [negative]
```

Calls to the Open AI Service use [tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them). The token's use is formatted as [p/t/c] to show `Prompt Tokens`, `Usage Tokens` and `Completion Tokens`.

## Contributing

Contributions to this project are welcome! There are loads of possible improvements and tweaks. There are many othere Azure AI Services, so any ideas for new services, or code improvements, such as:
- Live Language translation. 
- Change prosody of speach dynamically on response. It is currently defined per persona.
- Running fully in browser. Speech API is available in JavaScript. 
- Integration with Embeddings Redis cache solution for private document datastore searching.

Users can contribute to this project by reporting bugs or issues, suggesting new features, or submitting code contributions. To get started, users should fork the repository and submit a pull request. Before submitting a pull request, they should check out the following resources:

- [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [How to create a pull request](https://opensource.guide/how-to-contribute/#opening-a-pull-request)

Hope this is useful, and can spark ideas for use cases for these types of easy to consume AI services in your organisation or area of interest.
