#! python3
# linkCheck.py - Checks all links in a page
import requests, bs4, os

page = 'https://xkcd.com/'
link = requests.get(page)
if link.status_code == requests.codes.ok:
    print('Searching...')
    soup = bs4.BeautifulSoup(link.text, 'html.parser')
    links = soup.find_all('a')
    for i in range(len(links)):
        oneLink = links[i].get('href')
        # TODO: Test links
        if oneLink.endswith('''\\'''):
            # print(oneLink)
            print(oneLink[:-1])
        niceLink = os.path.join(page,os.path.basename(oneLink))
        # print(niceLink)
        test = requests.get(niceLink)
        if test.status_code == requests.codes.ok:
            print('%s is a working'%niceLink)
        else:
            print('%s is not working'%niceLink)
        # print(oneLink)
    # print(links)
else:
    print('Page is\'t working')



