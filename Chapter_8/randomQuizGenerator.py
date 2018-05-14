#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os
num = random.randint(1,99999)
os.makedirs(r'D:\Drive\Code\ATBSWP\Chapter_8\New_Folder%s' % num)
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_8\New_Folder%s' % num)
#The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton','New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate N quiz files.
for quizNum in range(2):    # Number for quizzes to be generated
    # TODO: Create the quiz and answer key files.
    quizFile = open('capitalssquiz%s.txt' % (quizNum +1), 'w')  # With the 'w' argumen it creates the files 
    answerKeyFile = open('capitalssquiz_answers%s.txt' % (quizNum + 1), 'w')    # It also creates the answers files

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')     # Name and period, it can also be created with ''' '''
    quizFile.write(('' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))   # Put the quiz number on
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())  # Create a list with the keys (tha name of the state)
    random.shuffle(states)          # Shuffle that list so the first 4 are not always the same

    # TODO: Loop through all 50 states, making a question for each
    for questionNum in range(4):    # Number of questiong 
        
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]       # The correct answer is selected in the the original dictionary with the key (state name)
        wrongAnswers = list(capitals.values())              # Creates a list of the values (the capitals) of the dictionary
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # Delete the right answer from the list of values using the index, it can also be done with wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers,3)        # From the list without the correct answer takes 3 random options
        answerOptions = wrongAnswers + [correctAnswer]      # Create a list with the 3 wrong options and the correct answer
        random.shuffle(answerOptions)                       # Shuffle the options 

        # Write the questions and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
