import youtube_dl

OPTIONS = {
    "format": "bestaudio/best",
    "outtmpl": "%(id)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


class YTSCDL:
    def download_sc(self, url: str) -> str:  # returns file name
        pass
