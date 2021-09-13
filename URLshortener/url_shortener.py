'''URL Shortener
Author : Lakshmi Sowjanya'''

import pyshorteners as shr

shortener = shr.Shortener()
URL = input("enter URL:")
shortened_url = shortener.tinyurl.short(URL)
print(f'Shortened URL {shortened_url}')
