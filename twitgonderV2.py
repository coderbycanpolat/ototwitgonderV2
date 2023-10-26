#canpolatgkky
from requests_oauthlib import OAuth1Session
import os
import json
from datetime import datetime
import schedule
import time
import random

# Twitter API kimlik bilgilerinizi buraya ekleyin V2'ye Göre Alın
consumer_key = "consumerapiyapistir"
consumer_secret = "consumersecretyapistir"
access_token = "acsestokeniyapistir"
access_token_secret = "acsesstokensecretiyapistir"

# Tweet metinlerini içeren bir liste oluşturur 
tweet_texts = [
    "Merhaba Dünya",
    "Test Mesajı",
    "@canpolatgkky",
]

# Tweet atacak olan işlevi günceller
def tweet():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    # Rasgele iki tweet metni seçer
    selected_tweets = random.sample(tweet_texts, 2)
    # Twit Metnini Ve Saati Gönderir( Saati Gönderme Amacı Aynı Twit Atılınca Hata Almasını Önlemek )
    for tweet_text in selected_tweets:
        tweet_text = f"{tweet_text}\n{current_time}"
        payload = {"text": tweet_text}

        # OAuth1Session ile oturumu açar
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

        # Tweeti at
        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                "Hata: {} {}".format(response.status_code, response.text)
            )

        print("Tweet gönderildi - Zaman: {}".format(current_time))

# Süreleyiciyi ayarlayın
schedule.every(30).minutes.do(tweet)  # Her 30 dakikada bir çalışacak şekilde ayarlandı (Twitter V2'nin Ücretsiz Süresine Göre Ayarlandı Her Gün Limit 50 Tane Bu 48 Tane Atıyor Günde)

# Sürekli çalışacak şekilde başlatalım
while True:
    schedule.run_pending()
    time.sleep(1)
