#Directed by: William Liu
#Special thanks to: William Liu

import random

#Generate gibberish:
i = 0
randWord = ""
vowel = "aeiou"
exceptu = "aeio"
while i < 10:
    randNum = random.randint(97, 122)
    randLet = str(chr(randNum))

    if i % 2 == 0 and randLet not in vowel:

        #At least in English, the pattern for q's is generally q + u + (vowel that isn't u). Due to this exception
        #and how I generate gibberish, words with 'q' will be 1 character longer. Sorry.
        if randLet == 'q':
            randWord = randWord + randLet + 'u' + random.choice(exceptu)
            i += 2
        else:
            randWord = randWord + randLet
            i += 1
    elif i % 2 == 1:
        randLet = random.choice(vowel)
        randWord = randWord + randLet
        i += 1

print(randWord)
print(len(randWord))

#Start the game.
print("Welcome to Gibberish Hangman. Good luck.")
print("Here's the word: ", end="")
for j in range(len(randWord)):
    print("_ ", end="")
print()

win = False
patience = 5
limbs = ['left leg.', 'right leg.', 'left arm.', 'right arm.']


#Initialize guess container:
currentProgress = list(range(len(randWord)))
for i in currentProgress:
    currentProgress[i] = '_'

guess = ''
guessContainer = ''
snarky = 1
pain = ['Oof.', 'Ouch.', 'Owie.']
while not win:

    if patience == 0:
        print("I'm done.")
        break

    guess = input("Guess a letter: ")

    #Filtering user input:
    if not guess.isalpha():

        # Easter egg:
        if guess.lower() == 'easter egg':
            print("You've found an Easter Egg!")
            continue

        print("Think you're clever, buddy? ")
        patience -= 1
        continue

    if len(guess) != 1:

        #Win condition 1:
        if guess == randWord:
            win = True
            break

        print("Only one letter at a time (unless it's exactly the full word).")
        patience -= 1
        continue

    if guess.isupper():
        guess = guess.lower()

    #Stores valid guesses:
    if guess not in guessContainer:
        guessContainer += guess
    else:
        print("You've already guessed that letter.")
        continue

    ##For correct guess:
    if guess in randWord:

        for index in range(len(randWord)):
            if guess == randWord[index]:
                currentProgress[index] = randWord[index]

        #Win condition 2:
        if ''.join(currentProgress) == randWord:
            win = True
            break

        print("Good Guess!")

    #Incorrect guess:
    else:

        #Losing head will always be last, and will result in loss.
        if len(limbs) == 0:
            print("And off goes your head. You lose! The word was obviously " + randWord + ".")
            break

        #Incorrect guesses prior to loss of head results in random removal of limb
        limbChoice = random.randint(1, len(limbs)) - 1
        painChoice = random.randint(1, len(pain)) - 1
        print("Incorrect. You've lost your " + limbs[limbChoice] + " " + pain[painChoice])
        limbs.remove(limbs[limbChoice])

        #Loss of arms:
        limbsString = ''.join(limbs)
        if limbsString.count('arm') == 0 and snarky == 1:
            print("Good luck typing without those.")
            snarky = 0

        #If the player has lost three or more limbs, they get a free letter (all instances)
        if len(limbs) == 1 or len(limbs) == 0:
            print("Seems like you're having a little trouble. Here's a hint: ")
            for k in range(len(randWord)):
                if currentProgress[k] != randWord[k]:
                    currentProgress[k] = randWord[k]
                    for l in range(len(randWord)):
                        if currentProgress[k] == randWord[l]:
                            currentProgress[l] = randWord[l]
                            guessContainer += randWord[l]

                    break

    #Prints out current progress:
    print("Current progress: ", end='')
    for j in range(len(currentProgress)):
        print(currentProgress[j], end='')
        print(' ', end='')
    print()

if win:
    print('The word is indeed "' + randWord + '". Congratulations! What now?')