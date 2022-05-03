import os
import re
import json
import warnings
from typing import Dict
from datetime import datetime

import requests


"""
1. 打开浏览器F12, 切换到Network栏目
2. 使用浏览器将 youtube 的 playlist 全部加载完.
3. 回到浏览器F12, Save all as HAR.
4. python3 youtube_playlist_downloader.py --har_file=/home/user/Download/filename.har
5. 下载的视频将会存放在当前目录.
"""


FORMAT = "%Y-%m-%d %H:%M:%S"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Host": "yt1s.com",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://yt1s.com",
    "Referer": "https://yt1s.com/en273"
}


class VideoInfo:

    def __init__(self,
                 vid: str,
                 title: str,
                 time: str,
                 author: str,
                 links: Dict[str, str]):
        self.vid = vid
        self.title = title
        self.time = time
        self.author = author
        self.mp4_links: Dict = links.get("mp4", {})
        self.mp4_720p_key = self.get_720_pixels_key()

        if not self.mp4_links:
            warnings.warn(f"警告: 视频 {self.title}({self.vid}) 没有mp4格式.")

    def get_720_pixels_key(self):
        if not self.mp4_links:
            return

        if not self.mp4_links.get("22"):
            warnings.warn(f"警告: 视频 {self.title}({self.vid}) 没有720p选项.")
            return

        return self.mp4_links["22"]["k"]


def get_video_info(youtube_link):
    url = "https://yt1s.com/api/ajaxSearch/index"
    resp = requests.post(url=url, headers=HEADERS, data={"q": youtube_link, "vt": "home"})
    content = resp.json()
    return VideoInfo(vid=content["vid"],
                     title=content["title"],
                     time=content["t"],
                     author=content["a"],
                     links=content["links"])


def get_download_link(vid, key):
    url = "https://yt1s.com/api/ajaxConvert/convert"
    resp = requests.post(url=url, headers=HEADERS, data={"vid": vid, "k": key})
    content = resp.json()
    return content["dlink"]


def parse_har_to_get_links(har_file):
    links = []
    with open(har_file) as f:
        resp = json.load(f)
        for entry in resp["log"]["entries"]:
            if (entry["response"]["status"] // 100) != 2: continue

            text = entry["response"]["content"]["text"]
            text = text.replace("\\u0026", "&")
            if "watch?" in text:
                watches = re.findall(r"watch\?v=(\S+?)&", text)
                for watch_uid in watches:
                    links.append(f"https://www.youtube.com/watch?v={watch_uid}")
    return links


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def download_video(url, save_to):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"}
    resp = requests.get(url, headers=headers)
    with open(save_to, "wb") as f:
        f.write(resp.content)


def main():
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "xingainian_1_playlist.har")
    youtube_links = parse_har_to_get_links(har_file=filename)
    print(len(youtube_links))
    for index, youtube_link in enumerate(youtube_links):

        # 断点续传
        if index < 8: continue

        video_info = get_video_info(youtube_link)
        download_link = get_download_link(video_info.vid, video_info.mp4_720p_key)

        print(f"[{current_time()}][{index}] {video_info.title:<30} 开始下载 {download_link}")
        download_video(download_link, f"{video_info.title}.mp4")
        print(f"[{current_time()}][{index}] {video_info.title:<30} 下载结束")


if __name__ == '__main__':
    main()
