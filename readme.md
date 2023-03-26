# Azure Open AI Conversational Speech-to-Speech

Azure Open AI Conversational Speech-to-Speech is a GitHub project that enables users to interact with a conversational system using their voice. The system uses Azure Cognitive Services to recognize speech and sends the voice input to the Azure Open AI Service. The resulting text response is replayed to the user using speech synthesis, providing a speech-to-speech interface to Open AI. Azure Sentiment analysis is also performed on the Open AI response. 

## Getting Started

To get started with this project, users will need to have access to an Azure Open AI Service and an Azure Speech Service. They should set up the corresponding keys and URLs in the config.py file and install the required dependencies, including the `openai`, `azure.ai.textanalytics`, `azure.core.credentials`, and `termcolor` packages. 

## Usage

To use this code, users should set the appropriate persona name by setting the value for `persona_name`. This value must match an entry in the persona dictionary, which is also in the `config.py` file. Users can add new personal entries in the dictionary and set the persona name to test. 

## Dependencies

The following dependencies are required for the project to run:

- Python packages:
    - `openai`: `pip3 install openai`
    - `azure.ai.textanalytics`: `pip3 install azure.ai.textanalytics`
    - `azure.core.credentials`:`pip3 install azure.core.credentials`
    - `termcolor`:`pip3 install termcolor`

## Contributing

Contributions to this project are welcome! Users can contribute to this project by reporting bugs or issues, suggesting new features, or submitting code contributions. To get started, users should fork the repository and submit a pull request. Before submitting a pull request, they should check out the following resources:

- [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [How to create a pull request](https://opensource.guide/how-to-contribute/#opening-a-pull-request)

Thank you for your interest in contributing to this project!
