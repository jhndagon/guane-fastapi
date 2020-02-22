import requests

def get_dog_picture_url():
    """
    Get a image from a dof API
    :return: url: string if not then null
    """
    request = requests.get("https://dog.ceo/api/breeds/image/random")
    if request.status_code == 200:
        request_to_json = request.json()
        return request_to_json['message']
    return ""