#! python3
#! downloadPWL - Download every single Poorly Drawn Lines comic.

import os,requests,bs4

# Url and create download directory

os.makedirs('PDL', exist_ok=True)   # exist_ok checks if the directory already exists
ComicUrl = 'http://www.poorlydrawnlines.com/comic/'

# while True:
for i in range(5):
    # Download the web page
    print('Downloading %s' %ComicUrl)
    web = requests.get(ComicUrl)
    web.raise_for_status()
    soup = bs4.BeautifulSoup(web.text,'html.parser')

    # Search for the image

    image = soup.select('p img')
    if image == []:
        print('Couldn\'t find link to image')
    else:
        imageUrl = image[0].get('src')

        # Save the image

        img = requests.get(imageUrl)
        img.raise_for_status()
        imgPath = os.path.join('PDL', os.path.basename(imageUrl))
        imageFile = open(imgPath,'wb')
        for chunk in img.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Go to next page and repeats

    next = soup.find_all('a', attrs={"rel":"prev"})
    if next == []:
        print('Done for evah')
        break
    ComicUrl = next[0].get('href')
    print('Done with %s' %os.path.basename(imageUrl))
print('Done downloading')
input()