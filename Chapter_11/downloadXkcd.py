#! python3
# download Xkcd.py - Downloads every single XKCD comic.
import requests, os, bs4, webbrowser

url = 'http://xkcd.com'     # starting url
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #Find the url of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev buttons's url.
    break
print('Done.')
input()