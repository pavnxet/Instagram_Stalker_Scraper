import sys
import display_graph as dgr
import data_fetch as df
import download_post as dp
import validate_account as va

def main():
    handle = input("Enter the profile name: ").strip().lstrip('@')

    if not handle:
        print("No username provided.")
        sys.exit(1)

    if va.validate_profile(handle):
        sys.exit(0)

    shortcodes = df.getPostInfo(handle)

    if not shortcodes:
        print("No posts found for this profile.")
        sys.exit(0)

    dp.downloadPost(shortcodes, handle)

    dgr.plotBargraph(shortcodes, handle)

if (__name__ == "__main__"):
    main()
