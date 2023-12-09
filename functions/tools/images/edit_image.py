import json

def edit_image(assistant, image_path, mask_path, prompt, n=1, size='1024x1024'):
    """
    Creates an edited or extended image given an original image and a prompt.

    :param client: OAI_Assistant instance configured with API key.
    :param image_path: Path to the original PNG image to be edited.
    :param mask_path: Path to the mask PNG image defining areas to be edited.
    :param prompt: A text description of the changes to be made to the image.
    :param n: The number of images to generate. Defaults to 1.
    :param size: The size of the generated images. Defaults to '1024x1024'.
    :return: A response object containing the edited images or an error message.
    """
    try:
        with open(image_path, 'rb') as image, open(mask_path, 'rb') as mask:
            response = assistant.open_ai.images.edit(
                image=image,
                mask=mask,
                prompt=prompt,
                n=n,
                size=size
            )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
