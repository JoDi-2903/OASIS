# OASIS

## Build and run it

### Requirements

For linux you habe to install additional packages

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

We are using the "vosk-model-small-en-us-0.15" modell for the recognizion of speech. The model is licensed under the Apache 2.0 license.
