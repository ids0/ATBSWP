#! python3
# yaleDownloader.py - Download a yale course on mp3format

import requests, bs4, os

# Basic stuffs
courseLink = 'https://oyc.yale.edu/biomedical-engineering/beng-100'
CourseName = os.path.basename(courseLink)
os.chdir(r'D:\Drive\Code\Random')
os.makedirs(CourseName, exist_ok=True)

# TODO: What todo if doesn't find any links and if file exists 

# Search for every lecture link on a course
req = requests.get(courseLink)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text,'html.parser')
sessions = soup.select('#quicktabs-tab-course-2')[0].get('href')    # Searchs for link to the course lecures
tab = os.path.split(sessions)
tabLink = tab[1][len(CourseName):-1]
fullLink = courseLink + tabLink
req = requests.get(fullLink)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text,'html.parser')
# lectures = soup.findAll('td',{'class':'views-field views-field-field-session-display-title'})
lectures = soup.select('td a')
for i in range(len(lectures)):
    lectureLink = courseLink + '/' +os.path.basename(lectures[i].get('href'))
    lectureReq = requests.get(lectureLink)
    if lectureReq.status_code == requests.codes.ok:
        lecutureSoup = bs4.BeautifulSoup(lectureReq.text,'html.parser')
        # Download and save mp3 files 
        mp3link = lecutureSoup.select('tbody > tr > td > a[href]')[1].get('href')
        print('Downloading MP3')
        mp3Path = os.path.join(CourseName,os.path.basename(mp3link))
        mp3File = open(mp3Path,'wb')
        mp3 = requests.get(mp3link)
        if mp3.status_code == requests.codes.ok:
            for chunk in mp3.iter_content(100000):
                mp3File.write(chunk)
                print('Saving %s' %os.path.basename(mp3link))
            print('Done')
            mp3File.close()
            break

    else:
        print('Link %s not working'%lectureLink)

# Regex to raname
input()


