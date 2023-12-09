import json


# Define the function to handle creating image variations
def create_image_variation(assistant, image_path, n=1, size='1024x1024'):
    """
    Creates a variation of a given image using OpenAI's image variation API.

    :param client: OAI_Assistant instance configured with API key.
    :param image_path: Path to the source PNG image for creating variations.
    :param n: The number of variations to generate. Defaults to 1.
    :param size: The size of the generated images. Defaults to '1024x1024'.
    :return: A response object containing the image variations or an error message.
    """
    try:
        with open(image_path, 'rb') as image:
            response = assistant.open_ai.images.create_variation(
                image=image,
                n=n,
                size=size
            )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
