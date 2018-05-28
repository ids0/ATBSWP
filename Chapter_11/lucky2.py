import sys, bs4, webbrowser, requests
 

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    googleLink = 'https://www.google.com/search?q=' + search
    results = requests.get(googleLink)
    results.raise_for_status()
    results = bs4.BeautifulSoup(results.text,"html.parser")
    print(type(results))