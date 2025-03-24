from django.shortcuts import render, redirect
from .forms import ScrapeForm
from .models import ScrapedData
from .services.scrape import scrape_spotify

def index_view(request):
    return redirect('scrape')

def scrape_view(request):
    if request.method == 'POST':
        form = ScrapeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            web_data = scrape_spotify(url)
            for item in web_data:
                ScrapedData.objects.create(
                    playlist_title=item["playlist_name"],
                    song_name=item["song_name"],
                    artist=item["artist"],
                    url=url
                )
            return redirect('scraped_data')
    else:
        form = ScrapeForm()
    return render(request, 'scraper/scrape.html', {'form': form})

def scraped_data_view(request):
    data = ScrapedData.objects.all()
    return render(request, 'scraper/scraped_data.html', {'data': data})