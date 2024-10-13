import re
import os
import requests

example_content = """I found three clips related to the impact of the degree of difficulty on the judge\'s 
score in Olympic Gymnastics. Here are the details along with images for each clip:\n\n1. **Clip 1:**\n   - **Start 
Time:** 499.33 seconds\n   - **End Time:** 567.90 seconds\n   - **Description:** "From start to finish, this is one
of the most difficult pieces of gymnastics I\'ve ever witnessed. Get the gold medals ready again."\n   - 
**Thumbnail:** ![Clip 1 
Thumbnail](https://project-one-thumbnail.s3.us-west-2.amazonaws.com/66f1b1eeae10e5f05781c7b0/500.jpeg?X-Amz-Algorit
hm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHRXELGFWS%2F20241013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=202
41013T062507Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=c74f58009405b96a63826abb
621c6d49568c838ee3f97027c19a7b017dd08bd5)\n\n2. **Clip 2:**\n   - **Start Time:** 579.80 seconds\n   - **End 
Time:** 599.20 seconds\n   - **Description:** "However, her difficulty score is going to be impacted because 
normally she combines those four elements, the switch leap onto the balance beam, then the switch half, and then a 
back pike."\n   - **Thumbnail:** ![Clip 2 
Thumbnail](https://project-one-thumbnail.s3.us-west-2.amazonaws.com/66f1b1f14e302ab9f2e7ef22/580.jpeg?X-Amz-Algorit
hm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHRXELGFWS%2F20241013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=202
41013T062507Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=3178ed1f61f526c7dd8a0cc2
ae8d264a8979e4ed969aa5edd3f8aebce89d6ba3)\n\n3. **Clip 3:**\n   - **Start Time:** 567.90 seconds\n   - **End 
Time:** 627.15 seconds\n   - **Description:** "From start to finish, this is one of the most difficult pieces of 
gymnastics I\'ve ever witnessed. Get the gold medals ready again."\n   - **Thumbnail:** ![Clip 3 
Thumbnail](https://project-one-thumbnail.s3.us-west-2.amazonaws.com/66f1b1eeae10e5f05781c7b0/568.jpeg?X-Amz-Algorit
hm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYRWJPOVHRXELGFWS%2F20241013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=202
41013T062507Z&X-Amz-Expires=604799&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=13531c4ec299ac9947ffd3c7
e5b6a4af925042c85e05de2d3ced1eec3aa47780)\n\nThese clips should help you create a compelling video on the topic. 
Let me know if you need further assistance!"""

def extract_url(content):
    pattern = r'\((https:\/\/[\s\S]*?)\)'
    print(f"Extracting...")

    # Find all matches in the msg content
    raw_urls = re.findall(pattern, content)

    # Clean up
    urls = []
    for url in raw_urls:
        clean_url = ''.join(url.split())
        urls.append(clean_url)

    # for url in raw_urls:
    #     print(f"Found {url}")
    return urls

def download_video(urls, start=1):

    if not urls:
        print("No thumbnail URLs found")
        return

    # Create a directory to save the images
    os.makedirs('../thumbnails', exist_ok=True)

    # Download each image
    for idx, url in enumerate(urls, start=1):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            # Save the image with a filename like 'thumbnail1.jpeg'
            image_filename = f'../thumbnails/thumbnail{idx}.jpeg'
            with open(image_filename, 'wb') as f:
                f.write(response.content)

            print(f"Downloaded {image_filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image from {url}: {e}")


def main():
    urls = extract_url(example_content)
    download_video(urls)

if __name__ == "__main__":
    main()