from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from Configurations import ckey
from Configurations import csecret
from Configurations import atoken
from Configurations import asecret
from Configurations import track_words
from Configurations import resultFile
class listener(StreamListener):

  def on_data(self,data):
    try:
      """
      tweet = json.loads(data)
      created_at = tweet["created_at"]
      tweet_id = tweet["id"]
      text = tweet["text"]
      in_reply_to_user_id = tweet["in_reply_to_user_id"]
      user_id = tweet["user"]["id"]
      user_location = tweet["user"]["location"]
      user_followers_count = tweet["user"]["followers_count"]
      user_friends_count = tweet["user"]["friends_count"]

      lang = tweet["lang"]
      if lang == "es":
        print "es"
        saveFile = open(resultFile,"a")

        saveFile.write(created_at + ":::" + str(tweet_id) + ":::" + text + ":::" + str(in_reply_to_user_id) + ":::" + str(user_id) + ":::" + user_location + ":::" + str(user_followers_count) + ":::" + str(user_friends_count)+"\n")
      """
      saveFile = open(resultFile,"a")
      saveFile.write(data)
      saveFile.close()
      return True
    except BaseException, e:
      print "failed on data",str(e)
      print data
      time.sleep(5)
  def on_error(self,status):
      print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track = track_words)

