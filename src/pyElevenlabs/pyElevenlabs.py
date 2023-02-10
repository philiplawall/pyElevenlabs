import requests

SpeechUrlTemplate = "https://api.elevenlabs.io/v1/text-to-speech/{}"


class pyElevenlabs(object):
    def __init__(self, apiKey):
        self._apiKey = apiKey
        self._headers = {"xi-api-key": self._apiKey}

    def speak(self, voice_id, text):
        url = SpeechUrlTemplate.format(voice_id)

        response = requests.post(
            url, headers=self._headers, json={"text": text})

        response.raise_for_status()
        return response.content
