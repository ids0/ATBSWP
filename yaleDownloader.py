#! python3
# yaleDownloader.py - Download a yale course on mp3format

import requests, bs4, os

# Basic stuffs
# courseLink = 'https://oyc.yale.edu/biomedical-engineering/beng-100'
courseLink = 'https://oyc.yale.edu/introduction-psychology/psyc-110'
splitLink = courseLink.split('/')
baseLink = 'https://'+ splitLink[2]
CourseName = os.path.basename(courseLink)
os.chdir(r'D:\Descargas')
os.makedirs(CourseName, exist_ok=True)

# Search for every lecture link on a course
req = requests.get(courseLink)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text,'html.parser')
sessions = soup.select('#quicktabs-tab-course-2')[0].get('href')    # Searchs for link to the course lecures
tab = os.path.split(sessions)
tabLink = tab[1][len(CourseName):]
fullLink = courseLink + tabLink
req = requests.get(fullLink)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text,'html.parser')
# lectures = soup.findAll('td',{'class':'views-field views-field-field-session-display-title'})
lectures = soup.select('td a')
for i in range(len(lectures)):
    # lectureLink = courseLink + '/' + os.path.basename(lectures[i].get('href'))
    lectureLink = baseLink + lectures[i].get('href')
    print('Downloading %s'%lectureLink)
    lectureReq = requests.get(lectureLink)
    if lectureReq.status_code == requests.codes.ok:
        lecutureSoup = bs4.BeautifulSoup(lectureReq.text,'html.parser')
        # Download and save mp3 files 
        mp3link = lecutureSoup.select('tbody > tr > td > a[href]')[1].get('href')
        if mp3link != []:
            mp3BaseName = os.path.basename(mp3link)
            mp3Path = os.path.join(CourseName,mp3BaseName)
            # If file already exists
            if os.path.isfile(mp3Path):
                print('%s already exists' %mp3BaseName)
            else:
                mp3File = open(mp3Path,'wb')
                mp3 = requests.get(mp3link)
                if mp3.status_code == requests.codes.ok:
                    print('Downloading %s'%mp3link)
                    for chunk in mp3.iter_content(100000):
                        mp3File.write(chunk)
                        if len(chunk) < 100000:
                            print('%s Downloaded Correctly' %mp3BaseName)
                    mp3File.close()
                    # break
    else:
        print('Link %s not working'%lectureLink)

# Maybe: Regex to raname

input()


