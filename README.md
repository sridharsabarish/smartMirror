# Smart Mirror
- A prototype for smart mirror, currently tested on Raspberry Pi 4 and Touch display.


# Quick Start

- Clone the repo 
    - `git clone https://github.com/sridharsabarish/SLMagic.git`
- Start the inventory app
    - `python3 -m simpleAPIClient.py`


# Testing

- Run Test Cases using `python3 -m pytest` 


# Weather API
- Note an API key might be needed if you decide to play around with the weather API instead of the weather widget. 
- Please follow the instructions from OpenWeatherAPI to generate API key.
- Once Generated this can be stored in a `.env` file, using ```API_KEY="Your generated API Key"```


# Future Work
1. Sensors For home
- ESP32 based humiditity/Temperature/Pressure monitoring.