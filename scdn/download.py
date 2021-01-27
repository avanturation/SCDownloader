import youtube_dl

OPTIONS = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


class YTSCDL:
    def download_sc(self, url: str):  # returns file name
        if isinstance(url, str):
            url = [url]

        with youtube_dl.YoutubeDL(OPTIONS) as ytdl:
            info_dict = ytdl.extract_info(url[0], download=True)
            filename = ytdl.prepare_filename(info_dict)
            return (info_dict, filename)
