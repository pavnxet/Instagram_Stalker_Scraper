# Validate the account
# Only Fetch data for Public Account

import instaloader

def validate_profile(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        if profile.is_private:
            print("This Account is Private")
            return True
        print(f"Profile found: @{profile.username} ({profile.full_name})")
        print(f"Followers: {profile.followers}  |  Posts: {profile.mediacount}")
        return False
    except instaloader.exceptions.ProfileNotExistsException:
        print("Invalid username")
        return True
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
        return True
    except Exception as e:
        print(f"Error validating profile: {e}")
        return True
