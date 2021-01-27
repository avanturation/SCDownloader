import argparse
from scdn import *


if __name__ == "__main__":
    Downloader = download.YTSCDL()
    Tagger = tag.AddTag()
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="The url of soundcloud song")
    parser.add_argument(
        "--with-lyrics", "-L", help="Include lyrics", action="store_true"
    )
    args = parser.parse_args()
    Result = Downloader.download_sc(args.url)
    print(Result[0])
    Tagger.add_tag(Result[0], Result[1], args.with_lyrics)
