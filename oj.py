from Rabbit_hole import spotify, yt_downloader, yt_scraper
import os

if __name__ == "__main__":
  os.chdir("Rabbit_hole")
  spotify.main()
  yt_downloader.main()
  yt_scraper.main()