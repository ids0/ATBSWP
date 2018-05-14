import os, random, pyperclip
# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32',filename))
# print(totalSize)

# helloFile = open(r'D:\Drive\Code\ATBSWP\Chapter_8\hello.txt','w')
# print(helloFile.read())
# helloFile.close()
# sonnetFile = open((r'D:\Drive\Code\ATBSWP\Chapter_8\sonnet29.txt'),'a')
# print(sonnetFile.readlines())

# os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_8')
# baconFile = open('bacon.txt','w')
# baconFile.write('Hello world!\n')
# baconFile.close()

# def is1to9(item):
#     while True:
#         print('Please enter a number  between 1 and 9 for ' + item + '.' )
#         number = input()
#         if (number.isdigit()) and (1 <= int(number) <= 9) and (int(number) == float(number)):
#             break
#     return int(number)

# cube = [
#     {'L':'TL','M':'TM','R':'TR',},
#     {'L':'ML','M':'MM','R':'MR',},
#     {'L':'LL','M':'LM','R':'LR',},
#     ]
# listofValues = []
# for row in range(len(cube)):
#     listofValues += list(cube[row].values())
# print(listsss)
# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
#     'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
#     'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
#     'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
#     'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
#     'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
#     'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
#     'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
#     'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
#     'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
#     'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
#     'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
#     'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
#     'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
#     'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
#     'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
#     'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# states = list(capitals.keys())
# print(states)
# random.shuffle(states)
# print(states)
# random.shuffle(states)
# print(states)
text = input()
if text == 'run' or (8/0 < 5):
    print('Only first')

print('IT DIDN\'T CRASH!')
input()