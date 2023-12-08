from typing import *
import json
import sys
import time
import subprocess
import traceback
from tempfile import NamedTemporaryFile
from PIL import Image
import requests
import openai


def generate_image(prompt, n:int=1, size:str="1024x1024"):
    """
    Generates an image using a machine learning model based on a given text prompt.

    Parameters:
    prompt (str): The text prompt based on which the image is to be generated.
    n (int, optional): The number of images to generate. Defaults to 1.
    size (str, optional): The size of the generated image. Defaults to "1024x1024".

    Returns:
    str: URL of the generated image.

    Notes:
    The function uses a machine learning client to generate an image based on the provided prompt.
    The generated image is temporarily saved and then read for display.
    The URL of the generated image is returned.
    """


    global client
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size=size,
      quality="standard",
      n=1
    )

    image_url = response.data[0].url

    im = Image.open(requests.get(image_url, stream=True).raw)
    im.save("temp.png")

    


    return image_url
