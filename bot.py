import tweepy
import requests
from bs4 import BeautifulSoup

api_key = "kMMzN3rd4yvVspZWh5U57dGcT"
api_key_secret = "FcWuIxoiCc98cNKrsUamQtTGABWJAHJNQsIJvFKHv4qCQVTAtm"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAB8Y2AEAAAAAK1NP%2BPHrgWslr34H%2B28rt69uqf4%3Dm9twB1DOK2tmHQONtYGEt1nt5cDABeUp9w6s1GVGTnyGHaZLA7"
access_token = "1927021220941185024-moKAATpL3gTMVc6x469aRon4QV5XKU"
access_token_secret = "UIkADpfAP8I2NRl8du47a5b2bKpSl81bmwVfkZFmW1ZKx"

client = tweepy.Client(bearer_token, api_key,api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Hashtag Generator Function
def generate_hashtags(topic):
    """Generate hashtags based on a given topic."""
    base_hashtags = [
        "#Trending", "#BreakingNews", "#LatestUpdate", "#TechNews", "#Viral", "#AI", "#Python",
        "#Innovation", "#Sports", "#Entertainment", "#Finance", "#Crypto", "#Gaming"
    ]
    # Scrape Twitter for relevant hashtags (example using BeautifulSoup)
    url = f"https://twitter.com/search?q={topic}&src=typed_query"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
        
    hashtags = [tag.text for tag in soup.find_all("a") if "#" in tag.text]
        
    suggested_hashtags = list(set(base_hashtags + hashtags))
    return random.sample(suggested_hashtags, min(5, len(suggested_hashtags)))


# Example usage
topic = "Conference League"
hashtags = generate_hashtags(topic)

tweet_text = f"Excited for the {topic}! {', '.join(hashtags)}"

client.create_tweet(text=tweet_text)

# tweet_id = "1927287436767379792"
# client.like(tweet_id)
# client.retweet(tweet_id)


client.create_tweet(text="1st Tweet Using a Bot")

client.like("1927287436767379792")

client.retweet("1927287436767379792")

client.create_tweet(in_reply_to_tweet_id=1927059292584054815, text="true he deserves")

for tweet in api.home_timeline():
    print(tweet.text)

person = client.get_user(username="FabrizioRomano").data.id

for tweet in client.get_users_tweets(person).data:
    print(tweet.text)

keyword = "Conference League"

client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAB8Y2AEAAAAAlbxPzQrOcOi%2FTBXmDuLognAZ3Ls%3DddNGobFP7aaEvOWaOqySCW4YkNTbK2MCbORDxkimByGnnzoOla",
    wait_on_rate_limit=True  # waits automatically when rate-limited
)


response = client.search_recent_tweets(query=keyword, max_results=5)

for tweet in response.data:
    print(f'-{tweet.text}\n')

print("Tweet posted successfully with hashtags!")
