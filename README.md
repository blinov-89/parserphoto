# Parserphoto

Парсер фото из интернета по ключевому слову с указанием количества.

google_crawler = GoogleImageCrawler(storage={'root_dir': 'photo'})

google_crawler.crawl(keyword='скейтборд', max_num=200)

