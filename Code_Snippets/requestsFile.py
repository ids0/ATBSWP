import requests

res = requests.get('https://gist.githubusercontent.com/reuven/5660728/raw/ff8cfe2d80f15b6569c9cf2644163f00105d8612/test-file4.txt')
if res.status_code == requests.codes.ok:
    file = open('Test.txt', 'wb')
    for part in res.iter_content(1000):
        print('writing...')
        file.write(part)
    file.close()
    print('Work done bro')
else:
    print('Not okay, maybe 404')
input()