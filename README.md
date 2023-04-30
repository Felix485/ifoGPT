# ifo Institute Twitter Bot

## Introduction
This project is a proof of concept for a Twitter bot that automatically generates tweets based on press releases from the ifo Institute. It is targeted to communications staff and helps them share news and press releases on Twitter.

### Capabilities
- users supply ifo webpage they want to tweet about
- our product will
  - summarize the news into tweet length, using the GPT 3.5 API language model
  - propose webscraped images and citations to illustrate the tweet
  - let you edit everything
  - navigate to Twitter with the post


## Getting Started
To get started with this project, you will need to have a GPT-3.5 API key, as well as a pexels API key. You can sign up for the keys at OpenAI and Pexels respectively.
@Jury: if necessary, we can supply both keys 

- create or save a key.txt file containing your GPT key in the ifoGPT folder
- create or save a pexels.txt file containing your Pexels key in the ifoGPT folder
- open a command prompt from folder ifoGPT
- pip install -r requirements.txt


## Usage
- open a command prompt from folder ifoGPT
- run: streamlit run frontend.py

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
This project was developed as part of a hackathon by Team ifoGPT. We would like to thank the organizers of the hackathon, the ifo Institute, as well as the creators of the GPT-3.5 API and Twitter, for their support and resources.
