import os
import requests
from bs4 import BeautifulSoup


def download_image(img_url, folder_path):
    try:
        # Send an HTTP request to get the image content
        response = requests.get(img_url)

        # Get the image file name from the URL
        img_name = os.path.basename(img_url)

        # Check if the image name has an extension
        if '.' not in img_name:
            img_name += ".jpg"  # Add .jpg extension if no extension exists

        # Save the image
        with open(os.path.join(folder_path, img_name), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {img_name}")
    except Exception as e:
        print(f"Could not download {img_url}: {e}")


def scrape_images_from_web_url(web_url, folder_path):
    # Send a GET request to fetch the content of the web page
    response = requests.get(web_url)

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Extract the image URLs from the 'src' attribute
    img_urls = [img['src'] for img in img_tags if img.has_attr('src')]

    # Make sure folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    count = 0  # Initialize counter

    # Download each image
    for img_url in img_urls:
        if img_url.startswith('http'):  # Ensure it's a full URL
            download_image(img_url, folder_path)
            count += 1  # Increment counter

     # Completion statement after web scraping, downloading, and renaming all images
    print(
        f"\nAll images have been web scraped, downloaded, and saved in the folder: {folder_path}")
    print(f"Total images downloaded: {count}")


# Web page URL
# chage this to url you want to scrape images from
web_url = "https://www.google.com/"
# Folder to save the images
folder_path = "path_to_your_directory"  # change this to your directory path

scrape_images_from_web_url(web_url, folder_path)
