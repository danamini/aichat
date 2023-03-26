# Azure Open AI Conversational Speech-to-Speech

This project uses Azure Cognative Serivces to recognise speech, sending voice input to the Azure Open AI Service. The resulting text response is replayed to the user using speech synthesis. This provides a speech-to-speech interface to Open AI.

To aid the conversational flow persona's can be defined. These provide Open AI with the context of the conversation and a voice and style for the speech sythnesis. 

To use this code you'll need to have deployed an Azure Open AI Service with a model, as well have provisioned an Azure Cognative Service for speech. 

The original code was created from snippets from https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/openai-speech

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Ensure the dependencies are installed using pip3.
Set the values in the config.py file, you need details of the Azure Open AI and Speech services.
Run aichat.py

### Prerequisites

You need to have access to Azure Open AI Service. See this link for details: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal

You need to have access to Azure Speech Service : https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/

Install the Python dependences. 

### Installation

Setup Azure Open AI Service, and Azure Speech Service.
Setup coresponding keys and URLs in config.py
Run python aichat.py at start a conversation!

## Usage

Set the approrate persona name, by setting the value for persona_name. This must match an entry in the persona dictionary, also in the config.py file.

You can add new personal entries in the dictionary, and set the persona name to test,

Can you play with the Speech Services here: https://speech.microsoft.com/portal/speechtotexttool

## Dependencies

The following dependencies required for the project to run:

- Python packages:
    - `openai`: `pip3 install openai`
    - `azure.ai.textanalytics`: `pip3 install azure.ai.textanalytics`
    - `azure.core.credentials`:`pip3 install azure.core.credentials`
    - `termcolor`:`pip3 install termcolor`

## Contributing

Contributions are welcome! Here are some ways you can contribute to this project:

- **Bug reports**: If you find any bugs or issues with the project, please open a new issue on the [issue tracker](https://github.com/danamini/aichat/issues).

- **Feature requests**: If you have an idea for a new feature or improvement, please open a new issue on the [issue tracker](https://github.com/danamini/aichat/issues).

- **Code contributions**: If you would like to contribute code to the project, please fork the repository and submit a pull request. Before submitting a pull request.

By contributing to this project, you agree to abide by the [code of conduct](link to your project's code of conduct).

### Getting Started

If you're new to contributing to open source projects, check out the following resources:

- [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [How to create a pull request](https://opensource.guide/how-to-contribute/#opening-a-pull-request)

Thank you for your interest in contributing to this project.

## License

Information about the license for the project. 

