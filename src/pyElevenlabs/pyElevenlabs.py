import requests
import logging

_LOGGER = logging.getLogger(__name__)

SpeechUrlTemplate = "https://api.elevenlabs.io/v1/text-to-speech/{}"


class pyElevenlabs(object):
    def __init__(self, apiKey):
        self._apiKey = apiKey

        headers = {"xi-api-key": self._apiKey}
        _LOGGER.debug("Connection Initialized OK")
