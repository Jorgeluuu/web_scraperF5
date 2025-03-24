from django.core.management.base import BaseCommand
from scraper.services.scrape import scrape_spotify
from dotenv import load_dotenv
from scraper.models import ScrapedData

class Command(BaseCommand):
    help = "Run the web scraper"

    def handle(self, *args, **kwargs):
        load_dotenv()
        url = "https://open.spotify.com/playlist/6MuB2lGArnfbF6U61uQjqE"
        web_data = scrape_spotify(url)
        print("Scraped Data:", web_data)

        for item in web_data:
            ScrapedData.objects.create(
                playlist_title=item["playlist_name"],
                song_name=item["song_name"],
                artist=item["artist"],
                url=url
            )

        self.stdout.write(self.style.SUCCESS("Scraping completed!"))