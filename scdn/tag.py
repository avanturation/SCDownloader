import mutagen
import requests
from mutagen.id3 import (
    ID3,
    TIT2,
    TALB,
    TPE1,
    TORY,
    TYER,
    APIC,
    TRCK,
    USLT,
    TPE2,
)


class AddTag:
    def _get_bin(self, url: str):
        data = requests.get(url)
        return data.content

    def add_tag(self, metadata, filename: str, lyrics: bool):
        album = self._get_bin(metadata["thumbnail"])
        try:
            mp3 = ID3(filename)
        except mutagen.id3.ID3NoHeaderError:
            mp3 = mutagen.File(filename)
            mp3.add_tags()
        mp3["TIT2"] = TIT2(3, metadata["title"])
        mp3["TPE1"] = TPE1(3, metadata["uploader"])
        mp3["TPE2"] = TPE2(3, metadata["uploader"])
        mp3["TALB"] = TALB(3, metadata["title"])
        mp3["TRCK"] = TRCK(3, "1")
        mp3["TYER"] = TYER(3, metadata["upload_date"])
        mp3["APIC"] = APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc="Album Cover",
            data=album,
        )

        mp3.save(v2_version=3)
        if lyrics:
            mp3["USLT"] = USLT(3, desc="", text=metadata["description"].strip())
