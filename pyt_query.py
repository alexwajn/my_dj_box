import re
import requests

def ret_3_first_links(title, artist):
    input = f"http://www.youtube.com/results?search_query={title}+by+{artist}"
    html = requests.get(input)

    video_ids = re.findall(r"watch\?v=(\S{11})", html.text)
    video_ids = list(dict.fromkeys(video_ids)) #smart (or dumb) way to remove duplicates haha
    return video_ids[0:3]

#print(ret_3_first_links("californication", "rhcp"))