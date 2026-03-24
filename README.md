# Instagram_stalker-scrapper-
Fetch data from any **public** Instagram profile (updated for March 2026)

### What this does
1. Validates that the target account exists and is public.
2. Fetches metadata (likes, comments, type) for every post.
3. Downloads all posts (images, videos, carousels) into `./insta_img/<username>/`.
4. Displays a bar graph of likes per post from oldest to newest.

> **Note:** Instagram no longer exposes a public JSON API (`?__a=1`) or unauthenticated
> GraphQL endpoints. This project now uses **[instaloader](https://instaloader.github.io/)**,
> a well-maintained library that handles authentication, rate-limiting, and Instagram's
> current API surface automatically.

---

## Prerequisites

- **Python 3.9+**
- **pip**

Install all dependencies at once:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install instaloader requests matplotlib
```

---

## How to Run

```bash
cd src
python driver.py
```

Enter a username when prompted (with or without the leading `@`):

```
Enter the profile name: natgeo
```

Downloaded files are saved to `./insta_img/natgeo/`.

---

## Optional: Log in to Instagram

Instaloader can optionally use your credentials to avoid stricter rate-limits on
unauthenticated sessions. To save a session:

```bash
instaloader --login YOUR_USERNAME
```

The session cookie is stored automatically and reused by the scraper.

---

## Resources

- [Instaloader documentation](https://instaloader.github.io/)
- [Requests library](https://docs.python-requests.org/)
- [Matplotlib](https://matplotlib.org/stable/gallery/index.html)

