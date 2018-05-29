import sys, bs4, webbrowser, requests
 

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    search = 'beautiful soup'
    googleLink = 'https://www.google.com/search?q=' + search
    results = requests.get(googleLink)
    results.raise_for_status()
    results = bs4.BeautifulSoup(results.text,"html.parser")
    link = results.select('.r a')
    for i in range(3):
        url = 'https://www.google.com' + link[i].get('href')
        print('opening %s...' % url)
        # webbrowser.open(url)
    print('Done')