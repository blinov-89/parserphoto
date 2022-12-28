from icrawler.builtin import GoogleImageCrawler
from bing_image_downloader import downloader
# downloader.download('скейтборд', limit=200,  output_dir='photo', adult_filter_off=True,
#                     force_replace=False, timeout=60, filter=['photo'], verbose=True)

google_crawler = GoogleImageCrawler(storage={'root_dir': 'photo'})
google_crawler.crawl(keyword='скейтборд', max_num=200)