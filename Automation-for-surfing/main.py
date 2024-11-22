import random
import time
import webbrowser
search=["pak vs afg","world cup","wc","points","table","nba","scores","israel","florida","shooting","logan","van","beek","world","cup","netanyahu","youtube","reddit","icc","world","cup","schedule","bing","ai","image","bing","image","ai","worldcup","doona","rachin","ravindra","angelo","mathews","yahoo","fantasy","basketball","image","creator","bing","bing","ai","image","generator","bing","ai","generator","totally","killer","espn","fantasy","basketball","face","login","cricket","world","cup","microsoft","bing","image","creator","weather","harrow","chatagpt","rahmanullah","gurbaz","bing","ai","art","alan","wake","world","cup","cricket","bing","ai","image","creator","hourly","weather","sugar","land","india","matches","in","world","cup","reddit","youtube","the","fall","of","the","house","of","usher","bing","create","rassie","van","der","dussen","fnaf","movie","pain","hustlers","bing","image","creator","icc","men’s","worldcup","schedule","hans","sama","devon","conway","bing","dall","e","worldcup","cricket","schedule","sssniperwolf","caroline","ellison"]
e=random.randrange(0,125)
t=random.randrange(2,5)
r=30
n=input("PRESS ENTER")
for i in range(r):
    time.sleep(t)
    e="https://www.bing.com/search?q="+search[random.randrange(0,125)]
    print(webbrowser.open_new(e))