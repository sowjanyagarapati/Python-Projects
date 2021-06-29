#import module
import instaloader

ig = instaloader.Instaloader()
dp = input("enter username")

ig.download_profile(dp, profile_pic_only=True)
print("Downloaded")
