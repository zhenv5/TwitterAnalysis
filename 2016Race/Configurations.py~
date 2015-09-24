#ckey,csecret,atoken,asecret
ckey = "6unqTB1FUaQh7UaLkpg9MzF6G"
csecret = "IpHhTu8T0JgnTigBHlPsMBc4O4RNzPHG9DIrjGI5q9yQDKmYdR"
atoken = "3745565674-ghOsDSzHesz6wjrzvaqEVfam6XyYlK6sw9spOmu"
asecret = "1QXkHRefgPMFJP4SuuRecLo7I7Zf76JJm2OalUnJqSedW"

#dataset
resultFile = "RawData/TwitterElectionData.txt"

# get track words for filtering
def get_Track_Words():
    track_words = [line.strip() for line in open("election-keywords.txt","r").readlines()]
    name_list = [line.strip() for line in open("election-names.txt","r").readlines()]
    for name in name_list:
        for item in name.split():
            track_words.append(item)
    return track_words

track_words = get_Track_Words()
#print track_words
