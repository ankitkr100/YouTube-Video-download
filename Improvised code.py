from pytube import YouTube
import concurrent.futures
from concurrent.futures import TimeoutError

file_path = 'file.txt'
save_path = '/home/akash/PycharmProjects/pythonProject1/videos'


def is_valid_url(url):
    return 'youtube.com/shorts/' in url


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        # Download the video
        stream.download(output_path=save_path)
        print(f'Downloaded {url} successfully')
    except Exception as e:
        print(f'Failed to download {url}: {e}')


with open(file_path, 'r') as file:
    urls = file.readlines()

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        url = url.strip()
        if not is_valid_url(url):
            print(f'Skipped invalid URL: {url}')
            continue

        # Submitting the download task to the executor
        future = executor.submit(download_video, url)
        futures.append(future)

    for future in concurrent.futures.as_completed(futures, timeout=40): # change the number accordingly
        try:
            future.result()
        except TimeoutError:
            print("Download exceeded 40 seconds and was skipped.")
