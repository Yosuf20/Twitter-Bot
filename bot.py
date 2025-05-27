import tweepy
import requests
from bs4 import BeautifulSoup

api_key = "kMMzN3rd4yvVspZWh5U57dGcT"
api_key_secret = "5QSOk9moRBWsJrJTuc4Q7AhcBr01YuihxpIRt72ixTIdb3l1Ft"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAB8Y2AEAAAAAlbxPzQrOcOi%2FTBXmDuLognAZ3Ls%3DddNGobFP7aaEvOWaOqySCW4YkNTbK2MCbORDxkimByGnnzoOla"
access_token = "1927021220941185024-IUgEFwnTBy68Q3Nzqz0Jkb9QVpbLWA"
access_token_secret = "dk5Nv4cs4DSTDwKh2AgqmKSDcGhjCGa7wVADT01EzK5UK"

client = tweepy.Client(bearer_token, api_key,api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# client.create_tweet(text="1st Tweet Using a Bot")

# client.like("1927287436767379792")
client.retweet("1927287436767379792")