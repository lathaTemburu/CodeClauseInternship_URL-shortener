import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def main():
    original_url = input("Enter the URL you want to shorten: ")
    shortened_url = shorten_url(original_url)
    print(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
        main()