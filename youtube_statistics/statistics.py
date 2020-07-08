import json
import re
import urllib.request

class Statistics():
    '''
    Returns diferent statistics out of a Youtube Video URL
    '''
    def __init__(self, url: str, api_key: str):
        self._url: str = url
        self._api: str = api_key
        self.refresh()

    def video_id(self):
        '''
        Takes the video id from a youtube URL
        '''
        split = self._url.split('?')
        v = split[1]
        video_ID = v.replace('v=', '')
        return video_ID

    def title(self):
        '''
        Returns the title of the video URL
        '''
        return self.dictionari['snippet']['title']

    def channel_name(self):
        '''
        Returns channel name of video URL
        '''
        return self.dictionari['snippet']['channelTitle']

    def description(self):
        '''
        Returns description of video URL
        '''
        return self.dictionari['snippet']['description']

    def channel_id(self):
        '''
        Returns channel id of video URL
        '''
        return self.dictionari['snippet']['channelId']

    def tags(self):
        '''
        Returns list of tags of video URL
        '''
        return self.dictionari['snippet']['tags']

    def views(self):
        '''
        Returns the views of the video URL
        '''
        return self.dictionari['statistics']['viewCount']

    def likes(self):
        '''
        Returns number of likes of the video URL
        '''
        return self.dictionari['statistics']['likeCount']

    def dislikes(self):
        '''
        Returns number of dislikes of the video URL
        '''
        return self.dictionari['statistics']['dislikeCount']

    def comments(self):
        '''
        Returns number of comments of the video URL
        '''
        return self.dictionari['statistics']['commentCount']

    def refresh(self):
        '''
        Refreshes the data
        '''
        video_id = self.video_id()
        url_api = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={self._api}&part=snippet'
        json_url = urllib.request.urlopen(url_api)
        data = json.loads(json_url.read())
        items = data['items']
        self.dictionari = items[0]