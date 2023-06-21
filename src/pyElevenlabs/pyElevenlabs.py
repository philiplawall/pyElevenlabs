import requests

SpeechUrlTemplate = "https://api.elevenlabs.io/v1/text-to-speech/{}"


class pyElevenlabsClient(object):
    def __init__(self, apiKey):
        self._apiKey = apiKey
        self._headers = {"xi-api-key": self._apiKey}

    def speak(self, voice_id, text, model="eleven_monolingual_v1"):
        url = SpeechUrlTemplate.format(voice_id)

        response = requests.post(
            url, headers=self._headers, json={"text": text, "model_id": model})

        response.raise_for_status()
        return response.content
