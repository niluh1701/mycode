#!/usr/bin/env python3

def main():

    round = 0
    answer = " "
    while round < 3 and (answer != "Brian" and answer.lower() != "honeypot"):
        round = round + 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______"\n')
        answer = answer.capitalize()
        if answer == 'Brian':
            print('Correct')
        elif round == 3:
            print('Sorry, the answer was Brian.')
        elif answer.lower() == 'honeypot':
            print('Secret found!')
        else:
            print('Sorry. Try again!')

if __name__ == '__main__':
    main()
