from pytube import YouTube
import os


file_path = r'pythonProject1\file.txt'

save_path = 'Tourism videos'


def is_valid_url(url):
    return 'youtube.com/shorts/' in url


with open(file_path, 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    if not is_valid_url(url):
        print(f'Skipped invalid URL: {url}')
        continue

    try:
        yt = YouTube(url)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        # Download the video
        stream.download(output_path=save_path)
        print(f'Downloaded {url} successfully')
    except Exception as e:
        print(f'Failed to download {url}: {e}')
