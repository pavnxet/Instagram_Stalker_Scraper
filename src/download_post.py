import requests
import os

# Download all the posts (video, image(s))
# Store them in the ./insta_img/{username} directory

_HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/134.0.0.0 Safari/537.36'
    ),
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.instagram.com/',
}

def _download_file(url, filepath):
    response = requests.get(url, headers=_HEADERS, stream=True, timeout=60)
    response.raise_for_status()
    with open(filepath, 'wb') as fh:
        for chunk in response.iter_content(chunk_size=8192):
            fh.write(chunk)

def downloadPost(shortcodes, username):
    save_dir = os.path.join('./insta_img', username)
    os.makedirs(save_dir, exist_ok=True)

    print(f"\nDownloading posts for @{username} → {save_dir}/")

    # shortcodes are newest-first; iterate in reverse so post1 = oldest
    for i, post in enumerate(reversed(shortcodes)):
        post_num = i + 1

        if post['is-video']:
            filepath = os.path.join(save_dir, f"post{post_num}.mp4")
            url = post.get('video_url', post['display-url'])
            try:
                _download_file(url, filepath)
                print(f"  [video]  post{post_num}.mp4")
            except Exception as e:
                print(f"  [error]  post{post_num} ({post['shortcode']}): {e}")

        elif post['typename'] == 'GraphSidecar' and 'sidecar_urls' in post:
            for j, item in enumerate(post['sidecar_urls']):
                ext = '.mp4' if item['is_video'] else '.jpg'
                filepath = os.path.join(save_dir, f"post{post_num}_{j+1}{ext}")
                try:
                    _download_file(item['url'], filepath)
                    print(f"  [sidecar] post{post_num}_{j+1}{ext}")
                except Exception as e:
                    print(f"  [error]  post{post_num}_{j+1}{ext}: {e}")

        else:
            filepath = os.path.join(save_dir, f"post{post_num}.jpg")
            try:
                _download_file(post['display-url'], filepath)
                print(f"  [image]  post{post_num}.jpg")
            except Exception as e:
                print(f"  [error]  post{post_num} ({post['shortcode']}): {e}")

    print(f"\nDownloads complete → {save_dir}/")
