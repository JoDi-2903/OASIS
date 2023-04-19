# OASIS

OASIS (Online Assistant for Support, Information and Services) is a proactive, voice-driven software agent that integrates various services to assist users with their daily planning and tasks. 

## Implemented APIs and Services
* [OpenWeather API](https://openweathermap.org/api)
* [Google Calendar API](https://developers.google.com/calendar/api/guides/overview)
* [Tankerkönig API](https://creativecommons.tankerkoenig.de/)
* [ZenQuotes](https://zenquotes.io/)
* [Yoga API](https://github.com/alexcumplido/yoga-api)
* [Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/)
* [Travel Advisor API](https://rapidapi.com/apidojo/api/travel-advisor)
* [Spoonacular API](https://spoonacular.com/food-api/docs)
* [Spotify API](https://developer.spotify.com/documentation/web-api)
* [Tagesschau API](https://tagesschau.api.bund.dev/)
* [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
* [TheCocktailDB](https://www.thecocktaildb.com/api.php)

## Build and run

### Requirements

For linux you have to install additional packages

```bash
sudo apt install portaudio19-dev espeak ffmpeg libespeak1
```

To install the required Python modules, the following command must be executed

```bash
pip install -r requirements.txt
```

In addition, VLC must be installed on the PC.

### Run

```bash
python main.py [args]
```

| Argument          | Default | Description     |
| ----------------- | ------- | --------------- |
| `-v`, `--verbose` | not set | Further logging |

### Tests

#### With coverage

```bash
# Run tests
coverage run -m pytest
# Generate report
coverage report
```

## Customization with config.json

The config file stores several parameters such as the name of the user as well as the credentials to the various services. The user can also customize the individual services. The available elements for the parameters of the services are shown below.

### Tankerkoenig

Supported options for "gas":
- e5
- e10
- diesel
- all

### Recipes

Supported options for "diet"[^1]:
- gluten free
- ketogenic
- vegetarian
- lacto-vegetarian
- ovo-vegetarian
- vegan
- pescetarian
- paleo
- primal
- whole30

### The Movie Database

Supported options for "watch_providers"[^1]:
- Amazon Prime Video
- Apple TV Plus
- Disney Plus
- Paramount Plus
- Netflix

## Project structure

![Bild2](https://user-images.githubusercontent.com/88625959/233072761-560f099d-7b1f-4fab-adf9-3535b21e2484.svg)

## Architecture Pattern

![Bild1](https://user-images.githubusercontent.com/88625959/233072883-620d991b-8e61-4b1f-adda-c23163224a90.png)

## Google Calendar

In order to use the google calendar, the email must first be activated in the OASIS project. 
At the first start the email is requested in the browser. 
If the login is successful, a token.json file with the tokens is created locally. 
These have an expiration date and must be renewed after a time.

## SpechRecognition Model

We are using the "vosk-model-small-en-us-0.15" modell for the recognition of speech. The model is licensed under the Apache 2.0 license.


[^1]: Several elements can be selected by separating them with ", ".
