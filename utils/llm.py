"""
Models available in the Gemini API:
models/gemini-2.5-flash
models/gemini-2.5-pro
models/gemini-2.0-flash
models/gemini-2.0-flash-001
models/gemini-2.0-flash-lite-001
models/gemini-2.0-flash-lite
models/gemini-2.5-flash-preview-tts
models/gemini-2.5-pro-preview-tts
models/gemma-4-26b-a4b-it
models/gemma-4-31b-it
models/gemini-flash-latest
models/gemini-flash-lite-latest
models/gemini-pro-latest
models/gemini-2.5-flash-lite
models/gemini-2.5-flash-image
models/gemini-3-pro-preview
models/gemini-3-flash-preview
models/gemini-3.1-pro-preview
models/gemini-3.1-pro-preview-customtools
models/gemini-3.1-flash-lite-preview
models/gemini-3.1-flash-lite
models/gemini-3-pro-image-preview
models/gemini-3-pro-image
models/nano-banana-pro-preview
models/gemini-3.1-flash-image-preview
models/gemini-3.1-flash-image
models/gemini-3.1-flash-lite-image
models/gemini-3.5-flash
models/gemini-omni-flash-preview
models/lyria-3-clip-preview
models/lyria-3-pro-preview
models/gemini-3.1-flash-tts-preview
models/gemini-robotics-er-1.5-preview
models/gemini-robotics-er-1.6-preview
models/gemini-2.5-computer-use-preview-10-2025
models/antigravity-preview-05-2026
models/deep-research-max-preview-04-2026
models/deep-research-preview-04-2026
models/deep-research-pro-preview-12-2025
models/gemini-embedding-001
models/gemini-embedding-2-preview
models/gemini-embedding-2
models/aqa
models/imagen-4.0-generate-001
models/imagen-4.0-ultra-generate-001
models/imagen-4.0-fast-generate-001
models/veo-3.1-generate-preview
models/veo-3.1-fast-generate-preview
models/veo-3.1-lite-generate-preview
models/gemini-2.5-flash-native-audio-latest
models/gemini-2.5-flash-native-audio-preview-09-2025
models/gemini-2.5-flash-native-audio-preview-12-2025
models/gemini-3.1-flash-live-preview
models/gemini-3.5-live-translate-preview
"""

"""
models/gemini-3.5-flash
-> Text generation.

Pollination Ai
-> Image generation.
"""
import os
import time
import requests

from urllib.parse import quote

from dotenv import load_dotenv
from google import genai

import wave

from piper import (
    PiperVoice,
)

load_dotenv()


TEXT_MODEL = "models/gemini-3.5-flash"

VOICE_MODEL = (
    "models/"
    "en_US-lessac-medium.onnx"
)


# IMAGE GENERATION
# ----------------
# Currently uses Pollinations AI.
# Can be switched to Gemini or any other
# image generation model in the future.


def get_api_key():
    """
    Loads the Gemini API key.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found in the .env file."
        )

    return api_key


def initialize_client():
    """
    Initializes the Gemini client.
    """

    api_key = get_api_key()

    return genai.Client(
        api_key=api_key,
    )


def generate_response(prompt, retries=3):
    """
    Generates text responses using Gemini.
    """

    client = initialize_client()

    for attempt in range(retries):

        try:
            response = client.models.generate_content(
                model=TEXT_MODEL,
                contents=prompt,
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text

        except Exception as error:

            print(
                f"[TEXT] Attempt {attempt + 1} failed : {error}"
            )

            if attempt < retries - 1:
                time.sleep(2)

    raise RuntimeError(
        "Failed to generate a text response from Gemini."
    )


def generate_image(
    prompt,
    output_path,
    retries=3,
):
    """
    Generates images using Pollinations AI.
    """

    for attempt in range(retries):

        try:

            image_url = (
                "https://image.pollinations.ai/prompt/"
                + quote(prompt)
            )

            print(
                image_url,
            )

            response = requests.get(
                image_url,
                timeout=120,
            )

            if response.status_code != 200:

                print(
                    f"Status Code : {response.status_code}"
                )

                print(
                    response.text,
                )

                raise RuntimeError(
                    "Failed to generate the image."
                )

            with open(
                output_path,
                "wb",
            ) as image_file:

                image_file.write(
                    response.content
                )

            return output_path

        except Exception as error:

            print(
                f"[IMAGE] Attempt {attempt + 1} failed : {error}"
            )

            if attempt < retries - 1:
                time.sleep(2)

    raise RuntimeError(
        "Failed to generate an image."
    )

def generate_voiceover(
    script,
    output_path,
):
    """
    Generates a voiceover using Piper.
    """

    try:

        voice = PiperVoice.load(
            VOICE_MODEL,
        )

        with wave.open(

            str(output_path),
            "wb",

        ) as audio_file:

            voice.synthesize_wav(

                script,
                audio_file,

            )

        return output_path


    except Exception as error:

        raise RuntimeError(
            "Failed to generate the voiceover."
        ) from error