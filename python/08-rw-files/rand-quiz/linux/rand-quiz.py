#! /usr/bin/python3

# rand-quiz.py - creates N quizzes with questions and answers in random order, along with the answer key

import os
import random

NUM_OF_QUIZZES = 10

# check if directories exist, if not create them
for directory in ['{}/quizzes'.format(os.getcwd()), '{}/answerkeys'.format(os.getcwd())]:
    if not os.path.exists(directory):
        os.makedirs(directory)

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate N quiz files
for quizNum in range(NUM_OF_QUIZZES):
    # create quiz and answer key files
    quizFile = open('./quizzes/capitalsquiz{}.txt'.format(quizNum + 1), 'w')
    answerKeyFile = open('./answerkeys/capitalsquiz_answers{}.txt'.format(quizNum + 1), 'w')

    # write out header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form {})'.format(quizNum + 1))
    quizFile.write('\n\n')

    # shuffle order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question for each
    for questionNum in range(50):
        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write question and answer options to the quiz file
        quizFile.write('{}. What is the capital of {}?\n'.format(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' {}. {}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write answer key to a file
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    # close files
    quizFile.close()
    answerKeyFile.close()
