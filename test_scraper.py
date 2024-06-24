from app.scraper import scrape


def main():
    soup = scrape()
    print(soup.prettify())

if __name__ == '__main__':
    main()