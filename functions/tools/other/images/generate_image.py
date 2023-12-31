import json


def generate_image(assistant, prompt, model='dall-e-2', n=1, size='1024x1024', quality='standard', style='vivid', response_format='url' or 'b64_json'):
    """
    Creates an image given a prompt using OpenAI's image generation API.

    :param client: OAI_Assistant instance configured with API key.
    :param prompt: A text description of the desired image(s).
    :param model: The model to use for image generation. Defaults to 'dall-e-2', can be changed to dall-e-3
    :param n: The number of images to generate. Defaults to 1.
    :param size: The size of the generated images. Defaults to '1024x1024'. Must be one of 256x256, 512x512, or 1024x1024 for dall-e-2. Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models.
    :param quality: The quality of the image to be generated. Defaults to 'standard'.
    :param style: The style of the generated images. Defaults to 'vivid'.
    :return: A response object containing the generated images or an error message.
    """
    try:
        response = assistant.open_ai.images.generate(
            model=model,
            prompt=prompt,
            n=n,
            size=size,
            quality=quality,
            style=style,
            response_format=response_format
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
