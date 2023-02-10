import requests
import logging

_LOGGER = logging.getLogger(__name__)

SpeechUrlTemplate = "https://api.elevenlabs.io/v1/text-to-speech/{}"


class pyElevenlabs(object):
    def __init__(self, apiKey):
        self._apiKey = apiKey
        self._headers = {"xi-api-key": self._apiKey}

        _LOGGER.debug("Connection Initialized OK")

    def speak(self, voice_id, text):
        _LOGGER.debug("Speak: %s", text)

        url = SpeechUrlTemplate.format(voice_id)
        _LOGGER.debug("URL: %s", url)

        response = requests.post(
            url, headers=self._headers, json={"text": text})
        _LOGGER.debug("Response: %s", response)

        if response.ok:
            return response.content
        else:
            raise Exception(response.text)
