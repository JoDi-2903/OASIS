# OASIS

## Build and run it

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

## SpechRecognition Model

We are using the "vosk-model-small-en-us-0.15" modell for the recognition of speech. The model is licensed under the Apache 2.0 license.

## Google Calendar
In order to use the google calendar, the email must first be activated in the OASIS project. 
At the first start the email is requested in the browser. 
If the login is successful, a token.json file with the tokens is created locally. 
These have an expiration date and must be renewed after a time.

## Config

### Recipes

Supported options for "diet" (please note that you can use multiple by seperating with ", "):
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

