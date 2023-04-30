# ifo Institute Twitter Bot

## Introduction
This project is a proof of concept for a Twitter bot that automatically generates tweets based on press releases from the ifo Institute. It is targeted to communications staff and helps them share news and press releases on Twitter.

### Capabilities
- users supply ifo webpage they want to tweet about
- our product will
  - summarize the news into tweet length, using the GPT language model
  - propose webscraped images and citations to illustrate the tweet
  - everything is editable
  - navigate to Twitter with the post

The bot uses the GPT-3.5 API to generate tailored text for each tweet, and also includes an image related to the content of the press release.

## Getting Started
To get started with this project, you will need to have a GPT-3.5 API key. You can sign up for a GPT-3.5 API key from OpenAI.
@Jury: if necessary, we can supply a key

- create or save a ifoGPT/key.txt file containing your GPT key
- open a command prompt from folder ifoGPT
- pip install -r requirements.txt


## Usage
- open a command prompt from folder ifoGPT
- run: streamlit run frontend.py

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
This project was developed as part of a hackathon by Team ifoGPT. We would like to thank the organizers of the hackathon, the ifo Institute, as well as the creators of the GPT-3.5 API and Twitter, for their support and resources.
