from random import randint
from brain_games.cli import is_question
from brain_games.cli import is_answer
from brain_games.cli import is_correct
from brain_games.cli import is_wrong_answer
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def random_digit():
    global digit
    digit = randint(1, 100)
    return digit


def play_even():
    answer = digit % 2
    if answer == 1:
        return 'no'
    if answer == 0:
        return 'yes'


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(NUMBER_OF_ATTEPTS):
        is_question(random_digit())
        print(is_answer(), end='')
        entered_response = input()
        if entered_response == play_even():
            is_correct()
        else:
            is_wrong_answer(entered_response, play_even())
            try_again_user()
            break
    else:
        congratulate_user()


def main():
    random_digit()
    play_even()
    is_even


if __name__ == '__main__':
    main()
