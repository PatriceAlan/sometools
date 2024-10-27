import click
import random

@click.command()
@click.option('-max','--max-number', default=100, help='The maximum number in the guessing range.')
@click.option('-att','--attempts', default=10, help='The number of attempts allowed to guess.')
def guess_the_number(max_number, attempts):
    """Guess the Number Game
    Try to guess the secret number based on hints.
    """
    def ask_for_guess():
        while True:
            user_guess_number = click.prompt('Enter your guess', type=int)
            if 1 <= user_guess_number <= max_number:
                return user_guess_number
            click.echo(f'Please enter a number between 1 and {max_number}.')

    click.echo('\n')
    click.echo('##############--------Guess the Number Game--------##############')
    click.echo(f'I am thinking of a number between 1 and {max_number}.')

    secret_number = random.randint(1, max_number)
    
    for i in range(attempts):
        click.echo(f'You have {attempts - i} guesses left.')
        user_guess = ask_for_guess()

        if user_guess == secret_number:
            click.echo('Yay! You guessed my number!')
            return

        # Give hints
        if user_guess < secret_number:
            click.echo('Your guess is too low.')
        elif user_guess > secret_number:
            click.echo('Your guess is too high.')

    # If the user runs out of guesses
    click.echo(f'Game over. The number I was thinking of was {secret_number}.')

