import requests

# Replace 'client_id' with your actual Imgur client ID
client_id = '48fdd4bed67d763'

def upload_image_to_imgur(image_path):
    url = 'https://api.imgur.com/3/image'
    headers = {'Authorization': f'Client-ID {client_id}'}
    with open(image_path, 'rb') as f:
        payload = {'image': f.read()}
        response = requests.post(url, headers=headers, files=payload)
        data = response.json()
        if response.status_code == 200:
            return data['data']['link']
        else:
            return None

image_path = 'test.jpg'
image_url = upload_image_to_imgur(image_path)
print("Image URL:", image_url)
