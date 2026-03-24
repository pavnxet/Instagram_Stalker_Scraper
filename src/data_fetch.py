import instaloader
import time

# Fetches all the data of all the posts using instaloader

def getPostInfo(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    shortcodes = []
    print(f"\nFetching post data for @{username}...")

    for post in profile.get_posts():
        info = {}
        info['shortcode'] = post.shortcode
        info['likes'] = post.likes if post.likes is not None else 0
        info['comments'] = post.comments if post.comments is not None else 0
        info['display-url'] = post.url
        info['is-video'] = post.is_video
        info['typename'] = post.typename

        if post.is_video:
            info['video_url'] = post.video_url
        elif post.typename == 'GraphSidecar':
            sidecar_urls = []
            for node in post.get_sidecar_nodes():
                if node.is_video:
                    sidecar_urls.append({'url': node.video_url, 'is_video': True})
                else:
                    sidecar_urls.append({'url': node.display_url, 'is_video': False})
            info['sidecar_urls'] = sidecar_urls

        shortcodes.append(info)
        print(f"  Fetched post {post.shortcode}  |  likes: {info['likes']}")

    print(f"\nTotal posts fetched: {len(shortcodes)}")
    return shortcodes
