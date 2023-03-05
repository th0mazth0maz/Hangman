#Stored images in 3D array/matrix
image = [[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['-', ' ', ' ', ' ']],
[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', ' ', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', 'O'], [' ', '|', ' ', ' '], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', 'O'], [' ', '|', ' ', '|'], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', 'O'], [' ', '|', ' ', '+'], [' ', '|', ' ', ' '], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', 'O'], [' ', '|', ' ', '+'], [' ', '|', ' ', '/'], ['-', '-', '-', ' ']], 
[[' ', '|', '-', '|'], [' ', '|', ' ', 'O'], [' ', '|', ' ', '+'], [' ', '|', ' ', 'n'], ['-', '-', '-', ' ']]]

#Introduction with word input
print('Welcome to Hang Man!')
print('Shortly, you will be asked for a word...')
print('This should be 6 or less characters!')
print('You will have 10 attempts to guess your word otherwise...')
print('Hang Man!')
word = input('Enter word:')
#While loop ensures that input is 6 or less characters
while len(word) > 6:
    word = input('Word is larger than 6 characters, please retry:')

#Establish score and failAttampt varaibles, this tracks the number of successful and unsuccessful attemps respectively.
score = 0
failAttempt = 0

#Establish wordArray array, this tracks which of the characters has been guessed, safeguard for repeated character words
wordArray = [False for i in range(len(word))]

#Establish while loop to ensure that only 11 failed attampts are allowed during the game
while failAttempt < 11:
    #Lets player enter their character guess
    character = input('Input guess character here: ')
    #for loop will cycle through each character of the word stored in the word variable
    for j in range (0, len(word)):
        #Establish match variable
        match = False
        #Will be triggered for match, print match, increment score, and set match to true for later events
        if character == word[j] and wordArray[j] == False:
            print('There is a match!')
            wordArray[j] = True
            score = score + 1
            match = True
            #Response for win (when all characters are guessed), gives score, and breaks for loop
            if score == len(word):
                print('You won!')
                print('You scored {}'.format(score))
                break
        #for loop will break when match is found
        if match == True:
            break
        #Text and image printed after unsuccessul attempt, when for loop has finished, also for loop broken on specific loop
        if match == False and j == len(word) - 1:
            print('There is no match')
            print(image[failAttempt][0][0], image[failAttempt][0][1], image[failAttempt][0][2], image[failAttempt][0][3])
            print(image[failAttempt][1][0], image[failAttempt][1][1], image[failAttempt][1][2], image[failAttempt][1][3])
            print(image[failAttempt][2][0], image[failAttempt][2][1], image[failAttempt][2][2], image[failAttempt][2][3])
            print(image[failAttempt][3][0], image[failAttempt][3][1], image[failAttempt][3][2], image[failAttempt][3][3])
            print(image[failAttempt][4][0], image[failAttempt][4][1], image[failAttempt][4][2], image[failAttempt][4][3])
            failAttempt = failAttempt + 1
    #Ensures for loop is broken at the end of the for loop
    if score == len(word):
        break
#Response for Hang Man, also gives the score
if score != len(word):
    print('You ran out of turns...')
    print('Hang Man!')
    print('You scored {}'.format(score))